import random
from abc import ABC, abstractmethod
from unit import ParseResult


class Strategy(ABC):
    @abstractmethod
    def execute(self, presult: ParseResult) -> str: ...


class Sameness(Strategy):
    def execute(self, presult: ParseResult) -> str:
        return presult.reconstruct()


class Deletion(Strategy):
    def __init__(self, percent: float, seed=None):
        super().__init__()
        self.percent = percent
        self.rng = random.Random(seed)

    def execute(self, presult: ParseResult) -> str:
        values = list(presult.index)
        sample = set(self.rng.sample(values, k=int(len(values) * self.percent)))
        output = presult.reconstruct(select=presult.index - sample)

        return output


class Replacement(Strategy):
    def __init__(self, seed=None):
        super().__init__()
        self.rng = random.Random(seed)

    def execute(self, presult: ParseResult) -> str:
        pseq = list(presult.iter())
        unique = list(set(pseq))
        self.rng.shuffle(unique)
        encode = {w: i for i, w in enumerate(unique)}
        output = "".join(
            list(
                map(
                    lambda c: "%010d" % encode[c] if c in encode else c,
                    presult.sequence,
                )
            )
        )
        return output


class RandomCharReplacementUnic(Strategy):
    def __init__(self, percent: float, seed=None):
        super().__init__()
        self.percent = percent
        self.rng = random.Random(seed)

    def execute(self, presult: ParseResult) -> str:
        chars = list(presult.sequence)
        non_space_indices = [i for i, char in enumerate(chars) if not char.isspace()]
        num_to_replace = int(len(non_space_indices) * self.percent)
        indices_to_replace = self.rng.sample(non_space_indices, num_to_replace)

        for idx in indices_to_replace:
            # Gerar um caractere Unicode aleatório (excluindo emojis)
            new_char = chr(self.rng.randint(0x0021, 0xFFFF))
            while 0x1F600 <= ord(new_char) <= 0x1F64F:  # Excluir emojis
                new_char = chr(self.rng.randint(0x0021, 0xFFFF))
            chars[idx] = new_char

        return ''.join(chars)


class WordShuffle(Strategy):
    def __init__(self, seed=None):
        super().__init__()
        self.rng = random.Random(seed)

    def execute(self, presult: ParseResult) -> str:
        words = list(presult.iter())
        self.rng.shuffle(words)

        result = []
        word_index = 0
        for i, s in enumerate(presult.sequence):
            if i in presult.index:
                result.append(words[word_index])
                word_index += 1
            else:
                result.append(s)

        return ''.join(result)
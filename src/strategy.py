import random

from IPython.core.inputtransformer import assign_from_system
from unit import ParseResult
from abc import ABC, abstractmethod


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
        if "\n" in presult.sequence:
            return output  # manter a quebrada
        else:
            return " ".join(output.split())  # tira espaços
        #return output



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
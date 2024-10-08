import unit as U
import strategy as S


class Degrader:
    __strategies = {
        "deletion": S.Deletion,
        "replacement": S.Replacement,
        "sameness": S.Sameness,

    }
    __units = {
        "chars": U.Chars(),
        "words": U.NotChar("\s"),
        "lines": U.NotChar("\n"),
    }

    def __init__(self, strategy: S.Strategy, unit: U.UnitParser):
        self.unit = unit
        self.strategy = strategy

    @classmethod
    def new(cls, strategy: str, unit: str, **strategy_arguments):
        unit = cls.__units[unit]
        strategy = cls.__strategies[strategy](**strategy_arguments)
        return cls(strategy, unit)

    def degrade(self, text: str) -> str:
        presult = self.unit.parse(text)
        output = self.strategy.execute(presult)
        return output

# TESTES COD NOVO

#TESTE 1:
texto1 = "Primeiro verso.\nSegundo verso.\nTerceiro verso.\nQuarto verso."
def testeVerseRemoverN(text, seed, percent):
    deletion_strategy = S.Deletion(percent=percent, seed=seed)
    unit_lines = U.NotChar("\n")
    verse_remover = Degrader(deletion_strategy, unit_lines)
    result = verse_remover.degrade(text)
    #print("\n")
    #print(text)
    #print("RandomVerseRemover:", result)
    return result


#TESTE 2
texto2 = "Este é um exemplo de texto com várias palavras para remover aleatoriamente."
def testeWordRemoverN(text, seed, percent):
    deletion_strategy = S.Deletion(percent=percent, seed=seed)
    unit_words = U.NotChar("\s")
    word_remover = Degrader(deletion_strategy, unit_words)
    result = word_remover.degrade(text)
    #print("\n")
    #print(text)
    #print("RandomWordRemover:", word_remover.degrade(text))
    return result

#TESTE 3
texto3 = "Texto com caracteres diversos, incluindo espaços e pontuação!"
def testeCharRemoverN(text, seed, percent):
    deletion_strategy = S.Deletion(percent=percent, seed=seed)
    unit_chars = U.Chars()
    char_remover = Degrader(deletion_strategy, unit_chars)
    result = char_remover.degrade(text)
    #print("\n")
    #print(text)
    #print("RandomCharRemover:", result)
    return result


# Teste 4: Substituição de Palavras por Índices Aleatórios
texto4 = "Transforme cada palavra em um índice aleatório."
def testeWordToIndexN(text, seed):
    replacement_strategy = S.Replacement(seed=seed)
    unit_words = U.NotChar(r"\s")
    word_to_index = Degrader(replacement_strategy, unit_words)
    result = word_to_index.degrade(text)
    #print("\n")
    #print(text)
    #print("RandomWordToIndex:", result)
    return result

seed = 42
percent = 0.5
#print(testeVerseRemoverN(texto1, seed, percent))
#print(testeWordRemoverN(texto2, seed, percent))
#print(testeCharRemoverN(texto3, seed, percent))
#print(testeWordToIndexN(texto4))
from abc import ABC, abstractmethod
from unicodedata import category as cat

from algorithm import Sampler, Shuffler, remove_join
from text.tokenizer import tokens, lines
from text.translit import Transliterator as Tr


class AbstractDegrader(ABC):
    @abstractmethod
    def degrade(self, text: str) -> str:
        pass


class RandomVerseRemover(AbstractDegrader, Sampler):
    def degrade(self, text: str) -> str:
        verses = lines(text)
        indexes = self.randomize(verses)
        degraded = remove_join(verses, set(indexes), "\n")
        return degraded


class RandomWordRemover(AbstractDegrader, Sampler):
    def degrade(self, text: str) -> str:
        words = tokens(text)
        indexes = self.randomize(words)
        degraded = remove_join(words, set(indexes), " ")
        return degraded


class RandomCharRemover(AbstractDegrader, Sampler):
    def degrade(self, text: str) -> str:
        notspaces = [i for i, c in enumerate(text) if not cat(c).startswith("Z")]
        indexes = self.randomize(notspaces)
        degraded = remove_join(text, set(indexes), "")
        return degraded


class RandomWordToIndex(AbstractDegrader, Shuffler):
    def degrade(self, text: str) -> str:
        words = tokens(text)
        tr = Tr.from_list(self.randomize(words))
        degraded = " ".join(
            map(lambda t: t[0] % t[1], zip([f"%010d"] * len(words), tr.encode(words)))
        )
        return degraded


class DoNothing(AbstractDegrader):
    def degrade(self, text: str) -> str:
        return text






# TESTES
import random


#TESTE 1
texto1 = "Primeiro verso.\nSegundo verso.\nTerceiro verso.\nQuarto verso."
def testeVerseRemoverO(text, rng, percent):
    verse_remover = RandomVerseRemover(rng=rng, percent=percent)
    resultado = verse_remover.degrade(text)
    #print("\n")
    #print(text)
    #print("RandomVerseRemover:")
    #print(resultado)
    return resultado


#TESTE 2
texto2 = "Este é um exemplo de texto com várias palavras para remover aleatoriamente."
def testeWordRemoverO(text, rng, percent):
    word_remover = RandomWordRemover(rng=rng, percent=percent)
    resultado = word_remover.degrade(text)
    #print("\n")
    #print(text)
    #print("RandomWordRemover:", resultado)
    return resultado


#TESTE 3
texto3 = "Texto com caracteres diversos, incluindo espaços e pontuação!"
def testeCharRemoverO(text, rng, percent):
    char_remover = RandomCharRemover(rng=rng, percent=percent)
    resultado = char_remover.degrade(text)
    #print("\n")
    #print(text)
    #print("RandomCharRemover:", resultado)
    return resultado



#TESTE 4
texto4 = "Transforme cada palavra em um índice aleatório."
def testeWordToIndexO(text, rng):
    # Supondo que Shuffler também requer um rng
    rng = random.Random(seed)
    word_to_index = RandomWordToIndex(rng=rng)
    resultado = word_to_index.degrade(text)
    #print("\n")
    #print(text)
    #print("RandomWordToIndex:", resultado)
    return resultado

seed = 42
rng = random.Random(seed)
percent = 0.5

#print(testeVerseRemoverO(texto1,rng, percent))
print(testeWordRemoverO(texto2, rng, percent))
#print(testeCharRemoverO(texto3, rng, percent))
#print(testeWordToIndexO(texto4))
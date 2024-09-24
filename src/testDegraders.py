import unittest
import unit as U
import strategy as S
from degrader import Degrader
import degraderAntigo
from src.degrader import *
from src.degraderAntigo import *



class MyTestCase(unittest.TestCase):
    def test_Verse_Remove(self):
        seed = 42
        rng = random.Random(seed)
        percent = 0.5
        texto1 = "Primeiro verso.\nSegundo verso.\nTerceiro verso.\nQuarto verso."
        self.assertEqual(testeVerseRemoverN(texto1,seed, percent), testeVerseRemoverO(texto1, rng, percent))  # add assertion here

    def test_Word_Remove(self):
        seed = 42
        rng = random.Random(seed)
        percent = 0.5
        texto2 = "Este é um exemplo de texto com várias palavras para remover aleatoriamente."
        self.assertEqual(testeWordRemoverN(texto2,seed, percent), testeWordRemoverO(texto2, rng, percent))  # add assertion here

    def test_Char_Remove(self):
        seed = 42
        rng = random.Random(seed)
        percent = 0.5
        texto3 = "Texto com caracteres diversos, incluindo espaços e pontuação!"

        self.assertEqual( testeCharRemoverN(texto3, seed, percent), testeCharRemoverO(texto3, rng, percent))  # add assertion here


if __name__ == '__main__':
    unittest.main()

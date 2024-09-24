import unittest

from src.degrader import *
from src.degraderAntigo import *

seed = 42
rng = random.Random(seed)
percent = 0.1
texto = [
    "Primeiro      verso.\nSegundo verso.\nTerceiro verso.\nQuarto verso.",
    "Primeiro verso.\nSegundo verso.\nTerceiro verso.\nQuarto verso.",
    "  Texto com TAB no começo e no final  ",
    "  Texto com TAB no começo",
    "Texto com TAB no final",
    "Texto com 2 espaços  aqui no meio",
    "Texto com caractéres diversos @*(@#*(@# jijasdj 2#@#89822+-02><",
    "Texto     com  alguns     espaços     ",
    " Texto com quebras e espaços antes e depois e no meio.\n  Espaços Segundo verso.\n   Terceiro verso.\nQuarto verso.     "
]

class MyTestCase(unittest.TestCase):
    def test_Verse_Remove(self):
        for i in range(len(texto)):
            self.assertEqual(testeVerseRemoverN(texto[i],seed, percent), testeVerseRemoverO(texto[i], rng, percent))

    def test_Word_Remove(self):
        for i in range(len(texto)):
            self.assertEqual(testeWordRemoverN(texto[i], seed, percent), testeWordRemoverO(texto[i], rng, percent))

    def test_Char_Remove(self):
        for i in range(len(texto)):
            self.assertEqual( testeCharRemoverN(texto[i], seed, percent), testeCharRemoverO(texto[i], rng, percent))

    def test_Word_to_Index(self):
        for i in range(len(texto)):
            self.assertEqual(testeWordToIndexN(texto[i], seed), testeWordToIndexO(texto[i], rng))

if __name__ == '__main__':
    unittest.main()

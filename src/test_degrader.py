import math
import unittest
from degrader import Degrader


class testDegrader(unittest.TestCase):

    def test_deletion_char(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        p = 0.1
        q = 1 - p
        d = Degrader.new("deletion", "chars", percent=p)
        o = d.degrade(s)

        len_degraded = len(o)
        len_expected = math.ceil(len(s) * q)

        self.assertEqual(len_degraded, len_expected)

    def test_deletion_lines(self):
        st = "abcdefghijklmnopqrstuvwxyz"
        s = "\n".join(st)
        p = 0.1
        q = 1 - p
        d = Degrader.new("deletion", "lines", percent=p)
        o = d.degrade(s)

        len_degraded = len(o)
        len_expected = len(s) - int(len(st) * p)
        self.assertEqual(len_degraded, len_expected)

    def test_deletion_word(self):
        s = " ".join("abcdefghijklmnopqrstuvwxyz")
        p = 0.1
        q = 1 - p
        d = Degrader.new("deletion", "words", percent=p)
        o = d.degrade(s)

        len_degraded = len(o.split())
        len_expected = math.ceil(len(s.split()) * q)
        self.assertEqual(len_degraded, len_expected)

    def test_replace_char(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        d = Degrader.new("replacement", "chars")
        o = d.degrade(s)

        len_degraded = len(o)
        len_expected = 10 * len(s)
        self.assertEqual(len_degraded, len_expected)

    def test_replace_word(self):
        s = " ".join("abcdefghijklmnopqrstuvwxyz")
        d = Degrader.new("replacement", "words")
        o = d.degrade(s)

        len_degraded = len(o.split())
        len_expected = len(s.split())
        self.assertEqual(len_degraded, len_expected)

    def test_replace_lines(self):
        s = "\n".join("abcdefghijklmnopqrstuvwxyz")
        d = Degrader.new("replacement", "lines")
        o = d.degrade(s)

        len_degraded = len(o.split("\n"))
        len_expected = len(s.split("\n"))
        self.assertEqual(len_degraded, len_expected)

    def test_sameness(self):
        s = "".join("abcdefghijklmnopqrstuvwxyz")
        d1 = Degrader.new("sameness", "chars")
        self.assertEqual(s, d1.degrade(s))

        s = " ".join("abcdefghijklmnopqrstuvwxyz")
        d2 = Degrader.new("sameness", "words")
        self.assertEqual(s, d2.degrade(s))

        s = "\n".join("abcdefghijklmnopqrstuvwxyz")
        d3 = Degrader.new("sameness", "lines")
        self.assertEqual(s, d3.degrade(s))

    def test_random_char_replacementUnic(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        p = 0.1
        d = Degrader.new("random_char_replacementUnic", "chars", percent=p)
        o = d.degrade(s)

        # Verifica se o comprimento da string não mudou
        self.assertEqual(len(o), len(s))

        # Verifica se a porcentagem de caracteres alterados está próxima do esperado
        changed_chars = sum(1 for a, b in zip(s, o) if a != b)
        expected_changes = int(len(s) * p)
        self.assertAlmostEqual(changed_chars, expected_changes, delta=1)

        # Verifica se todos os caracteres alterados são diferentes dos originais
        for a, b in zip(s, o):
            if a != b:
                self.assertNotEqual(a, b)

    def test_word_shuffle(self):
        s = "The quick brown fox jumps over the lazy dog"
        d = Degrader.new("word_shuffle", "words")
        o = d.degrade(s)

        # Verifica se o número de palavras não mudou
        self.assertEqual(len(o.split()), len(s.split()))

        # Verifica se todas as palavras originais estão presentes no resultado
        self.assertEqual(set(o.split()), set(s.split()))

        # Verifica se a ordem das palavras é diferente (a menos que por acaso seja igual)
        self.assertNotEqual(o, s)

    def test_word_shuffle_with_newlines(self):
        s = "First line\nSecond line\nThird line"
        d = Degrader.new("word_shuffle", "words")
        o = d.degrade(s)

        # Verifica se o número de linhas não mudou
        self.assertEqual(o.count('\n'), s.count('\n'))

        # Verifica se o número total de palavras não mudou
        self.assertEqual(len(o.split()), len(s.split()))

        # Verifica se todas as palavras originais estão presentes no resultado
        original_words = set(s.split())
        result_words = set(o.split())
        self.assertEqual(result_words, original_words)

        # Verifica se a estrutura de quebras de linha foi preservada
        self.assertEqual([len(line.split()) for line in s.split('\n')],
                         [len(line.split()) for line in o.split('\n')])

        # Verifica se pelo menos uma linha foi embaralhada
        self.assertNotEqual(s.split('\n'), o.split('\n'))


if __name__ == "__main__":
    unittest.main()

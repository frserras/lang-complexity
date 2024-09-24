import math
import unittest
from src.degrader import Degrader


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


if __name__ == "__main__":
    unittest.main()

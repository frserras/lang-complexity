from functools import partial
from operator import ne
from random import Random

from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(kw_only=True)
class Randomizer(ABC):
    rng: Random

    @abstractmethod
    def randomize(self, l: list) -> list:
        pass


@dataclass(kw_only=True)
class Sampler(Randomizer):
    percent: float

    def randomize(self, l: list) -> list:
        length = len(l)
        indexes = self.rng.sample(range(length), k=int(length * self.percent))
        return indexes


class Shuffler(Randomizer):
    def randomize(self, l: list) -> list:
        self.rng.shuffle(l)
        return l


def apply_at_indexes(func, elements, indexes):
    ret = [(func(e) if i in indexes else e) for (i, e) in enumerate(elements)]
    return ret


def replace_at_indexes(sequence, indexes, e):
    return apply_at_indexes(lambda x: e, sequence, indexes)


def delete_at_indexes(sequence, indexes):
    ret = (e for (i, e) in enumerate(sequence) if i not in indexes)
    return ret


def map_at_indexes(sequence, indexes, d):
    return apply_at_indexes(lambda x: d[x], sequence, indexes)


def remove_empty(seq):
    return filter(partial(ne, ""), seq)


def remove_by(seq, by):
    return filter(partial(ne, by), seq)


def join(sequence, sep):
    return sep.join(sequence)


def remove_join(what, at, sep):
    sequence = delete_at_indexes(what, at)
    ret = join(sequence, sep)
    return ret

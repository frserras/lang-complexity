from degrader import Degrader
from compressor import Compressor

from abc import ABC, abstractmethod
from collections.abc import Callable


class Metric(ABC):
    @abstractmethod
    def compute(self, input: str) -> float: ...


class DegradeAndCompress(Metric):
    def __init__(
        self,
        degrader: Degrader,
        compressor: Compressor,
        kernel: Callable[[int, int], float],
    ):
        super().__init__()
        self.degrader = degrader
        self.compressor = compressor
        self.kernel = kernel

    def compute(self, input: str) -> float:
        degraded_input = self.degrader.degrade(input)
        compressed_input = self.compressor.compress(input)
        compressed_degraded_input = self.compressor.compress(degraded_input)
        output = self.kernel(len(compressed_input), len(compressed_degraded_input))
        return output

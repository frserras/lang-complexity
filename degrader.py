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

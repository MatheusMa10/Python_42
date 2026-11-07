from ex3.ex3.creature_factory import CreatureFactory
from ex3.ex3.flame_factory import FlameFactory
from ex3.ex3.transform_factory import TransformCreatureFactory

from ex4.battle_strategy import (
    BattleStrategy,
    InvalidStrategyError
)

from ex4.normal_strategy import NormalStrategy
from ex4.aggressive_strategy import AggressiveStrategy


Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:

        for i in range(len(opponents)):

            for j in range(i + 1, len(opponents)):

                factory_a, strategy_a = opponents[i]
                factory_b, strategy_b = opponents[j]

                creature_a = factory_a.create_base()
                creature_b = factory_b.create_base()

                print("* Battle *")
                print(creature_a.describe())
                print("vs.")
                print(creature_b.describe())
                print("now fight!")

                strategy_a.act(creature_a)
                strategy_b.act(creature_b)

    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:

    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()

    # Tournament 0
    print("Tournament 0 (basic)")

    opponents_0: list[Opponent] = [
        (flame_factory, normal),
        (transform_factory, aggressive)
    ]

    print("[ (Flameling+Normal), (Shiftling+Aggressive) ]")

    battle(opponents_0)

    print()

    # Tournament 1
    print("Tournament 1 (error)")

    opponents_1: list[Opponent] = [
        (transform_factory, aggressive),
        (flame_factory, aggressive)
    ]

    print("[ (Shiftling+Aggressive), (Flameling+Aggressive) ]")

    battle(opponents_1)


if __name__ == "__main__":
    main()
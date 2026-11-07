from ex3 import FlameFactory, TransformCreatureFactory
from ex3.creature_factory import CreatureFactory


def demonstrate_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("\n=== Base Creature ===")
    print(base.describe())
    print(base.attack())

    print("\n=== Evolved Creature ===")
    print(evolved.describe())
    print(evolved.attack())


def battle_factories(
    factory1: CreatureFactory,
    factory2: CreatureFactory
) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print("\n=== Battle ===")
    print(creature1.describe())
    print(creature2.describe())

    print("\n=== Attacks ===")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    print("=== Factory Demonstration ===")

    demonstrate_factory(flame_factory)
    demonstrate_factory(transform_factory)

    print("\n=== Creature Battle ===")

    battle_factories(flame_factory, transform_factory)


if __name__ == "__main__":
    main()

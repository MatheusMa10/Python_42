from ex3 import TransformCreatureFactory


def test_transformation(
    factory: TransformCreatureFactory
) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Creature with transform capability")

    print("\nBase:")
    print(base.describe())
    print(base.attack())

    base.transform()
    print(base.attack())
    base.revert()

    print("\nEvolved:")
    print(evolved.describe())
    print(evolved.attack())

    evolved.transform()
    print(evolved.attack())
    evolved.revert()


def main() -> None:
    transform_factory = TransformCreatureFactory()
    test_transformation(transform_factory)


if __name__ == "__main__":
    main()
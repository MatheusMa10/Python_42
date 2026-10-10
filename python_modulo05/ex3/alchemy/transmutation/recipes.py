from elements import create_air
from ..potions import strength_potion
from elements import create_fire

def lead_to_gold():
    air = create_air()
    strength = strength_potion()
    fire = create_fire()

    return (
        f"Recipe transmuting Lead to Gold: brew '{air}' "
        f"and '{strength}' mixed with '{fire}'"
    )
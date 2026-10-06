import random
def  gen_player_achievements():
    all_achieviments = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor',
    'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer']
    rand_int = random.randint(1, len(all_achieviments))
    choices = set(random.sample(all_achieviments, k=rand_int))

    return (choices)

if __name__ == "__main__":
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    all = set.union(alice, bob, charlie, dylan)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    print(f"All distinct achievements: {all}")
    print()
    print(f"Common achievements: {set.intersection(alice, bob, charlie, dylan)}")
    print()
    print(f"Only Alice has: {set.difference(alice, bob, charlie, dylan)}")
    print(f"Only Bob has: {set.difference(bob, alice, charlie, dylan)}")
    print(f"Only Charlie has: {set.difference(charlie, alice, bob, dylan)}")
    print(f"Only Dylan has: {set.difference(dylan, alice, bob, charlie)}")
    print()
    print(f"Alice is missing: {all.difference(alice)}")
    print(f"Bob is missing: {all.difference(bob)}")
    print(f"Charlie is missing: {all.difference(charlie)}")
    print(f"Dylan is missing: {all.difference(dylan)}")
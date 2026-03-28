import random


def gen_player_achievements() -> set:
    achievements = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Unstoppable",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
    ]
    return set(random.sample(achievements,
                             random.randint(1, len(achievements))))


def ft_achievement_tracker() -> None:

    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()

    all_uniqe_achiev = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_uniqe_achiev}")
    print()

    common_to_all = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements {common_to_all}")
    print()

    only_alice = alice.difference(bob, charlie, dylan)
    print(f"Only Alice has: {only_alice}")

    only_bob = bob.difference(alice, charlie, dylan)
    print(f"Only Bob has: {only_bob}")

    only_charlie = charlie.difference(alice, bob, dylan)
    print(f"Only Charlie has: {only_charlie}")

    only_dylan = dylan.difference(alice, bob, charlie)
    print(f"Only Dylan has: {only_dylan}")

    alice_missing = (bob.union(charlie, dylan)).difference(alice)
    print(f"Alice is missing: {alice_missing}")

    bob_missing = (alice.union(charlie, dylan)).difference(bob)
    print(f"Bob is missing: {bob_missing}")

    charlie_missing = (alice.union(bob, dylan)).difference(charlie)
    print(f"Charlie is missing: {charlie_missing}")

    dylan_missing = (alice.union(bob, charlie)).difference(dylan)
    print(f"Dylan is missing: {dylan_missing}")


if __name__ == "__main__":
    ft_achievement_tracker()

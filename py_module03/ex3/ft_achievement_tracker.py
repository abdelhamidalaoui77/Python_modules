
def remove_duplicates(achievements: list) -> set:
    return set(achievements)


def ft_achievement_tracker() -> None:

    print("=== Achievement Tracker System ===\n")

    data1 = ['first_kill', 'first_kill', 'level_10', 'treasure_hunter',
             'treasure_hunter', 'speed_demon']
    data2 = ['first_kill', 'level_10', 'boss_slayer', 'collector',
             'level_10', 'collector']
    data3 = ['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
             'perfectionist', 'perfectionist']

    alice = remove_duplicates(data1)
    bob = remove_duplicates(data2)
    charlie = remove_duplicates(data3)

    print(f"player alice achievments: {alice}")
    print(f"player bob achievments: {bob}")
    print(f"player charlie achievments: {charlie}")
    print()

    print("=== Achievement Analytics ===")
    all_uniqe_achiev = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_uniqe_achiev}")
    print(f"Total unique achievements: {len(all_uniqe_achiev)}\n")

    common_to_all = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_to_all}")

    rare_achiev = (
        (alice.difference(bob).difference(charlie))
        .union(bob.difference(alice).difference(charlie))
        .union(charlie.difference(alice).difference(bob))
    )

    print(f"Rare achievements (1 player): {rare_achiev}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    ft_achievement_tracker()

import random


def gen_player_achievements() -> set:
    achivements = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
    ]
    return set(random.sample(achivements, random.randint(1, len(achivements))))


def main():
    print("=== Achievement Tracker System ===\n")
    player_alice = gen_player_achievements()
    player_bob = gen_player_achievements()
    player_charlie = gen_player_achievements()
    player_dylan = gen_player_achievements()
    print(f"Player Alice: {player_alice}")
    print(f"Player Bob: {player_bob}")
    print(f"Player Charlie: {player_charlie}")
    print(f"Player Dylan: {player_dylan}\n")
    print(
        f"All distinct achievements: "
        f"{player_alice | player_bob | player_charlie | player_dylan}"
    )
    print(
        f"Common achievements: "
        f"{player_alice & player_bob & player_charlie & player_dylan}"
    )
    others_but_alice = player_bob | player_charlie | player_dylan
    others_but_bob = player_alice | player_charlie | player_dylan
    others_but_charlie = player_alice | player_bob | player_dylan
    others_but_dylan = player_alice | player_bob | player_charlie
    print(f"Only Alice has: {player_alice - others_but_alice}")
    print(f"Only Bob has: {player_bob - others_but_bob}")
    print(f"Only Charlie has: {player_charlie - others_but_charlie}")
    print(f"Only Dylan has: {player_dylan - others_but_dylan}\n")
    print(f"Alice is missing: {others_but_alice - player_alice}")
    print(f"Bob is missing: {others_but_bob - player_bob}")
    print(f"Charlie is missing: {others_but_charlie - player_charlie}")
    print(f"Dylan is missing : {others_but_dylan - player_dylan}")


if __name__ == "__main__":
    main()

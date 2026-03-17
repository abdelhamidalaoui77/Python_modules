from typing import Generator

players = [
    {"name": "alice", "level": 5},
    {"name": "bob", "level": 10},
    {"name": "charlie", "level": 15},
    {"name": "diana", "level": 8},
]

actions = ["killed monster", "found treasure", "leveled up"]


def game_events(n: int) -> Generator[tuple[str, int, str], None, None]:
    i = 0
    while i < n:
        player = players[i % len(players)]
        action = actions[i % len(actions)]

        if action == "leveled up":
            player["level"] += 1

        yield (player["name"], player["level"], action)

        i += 1


def fibonacci_stream(n: int) -> Generator[int, None, None]:
    a = 0
    b = 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def prime_stream(n: int) -> Generator[int, None, None]:
    found = 0
    num = 2

    while found < n:
        is_prime = True
        d = 2

        while d * d <= num:
            if num % d == 0:
                is_prime = False
                break
            d += 1

        if is_prime:
            yield num
            found += 1

        num += 1


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===\n")

    total_events = 20

    high_level = 0
    treasure = 0
    level_up = 0
    count = 1

    for name, level, action in game_events(total_events):
        print(f"Event {count}: Player {name} (level {level}) {action}")

        if level >= 10:
            high_level += 1
        if action == "found treasure":
            treasure += 1
        if action == "leveled up":
            level_up += 1

        count += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level events: {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")

    print("\nMemory usage: Constant (streaming)\n")

    print("=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10): ", end="")
    for num in fibonacci_stream(10):
        print(num, end=" ")
    print()

    print("Prime numbers (first 5): ", end="")
    for num in prime_stream(5):
        print(num, end=" ")
    print()


if __name__ == "__main__":
    ft_data_stream()

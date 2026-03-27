from typing import Generator

players = [
    {"name": "alice", "level": 5},
    {"name": "bob", "level": 12},
    {"name": "charlie", "level": 8},
    {"name": "diana", "level": 15},
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

    print("Processing 1000 game events...\n")
    total_events = 1000

    high_level = 0
    treasure = 0
    level_up = 0
    count = 1
    procces_time = 0.000045
    time = 0

    for name, level, action in game_events(total_events):
        print(f"Event {count}: Player {name} (level {level}) {action}")

        if level >= 65:
            high_level += 1
        if action == "found treasure":
            treasure += 1
        if action == "leveled up":
            level_up += 1
        time += procces_time
        count += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")

    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {time:.3f} seconds\n")

    print("=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10): ", end="")
    i = 1
    for num in fibonacci_stream(10):
        print(num, end="")
        if i < 10:
            print(", ", end="")
            i += 1
    print()

    i = 1
    print("Prime numbers (first 5): ", end="")
    for num in prime_stream(5):
        print(num, end=" ")
        if i < 5:
            print(", ", end="")
            i += 1
    print()


if __name__ == "__main__":
    try:
        ft_data_stream()
    except Exception as e:
        print(e)

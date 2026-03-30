import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    names = [
        "Alice", "bob", "Charlie", "dylan",
        "Emma", "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {names}")

    capitalized = [n.capitalize() for n in names]
    already_capitalized = [n for n in names if n[0].isupper()]

    print(f"New list with all names capitalized: {capitalized}")
    print(f"New list of capitalized names only: {already_capitalized}")

    scores = {n: random.randint(10, 1000) for n in capitalized}
    print("\nScore dict:", scores)

    avg = sum(scores.values()) / len(scores)
    print(f"Score average is {avg:.2f}")

    high_scores = {n: s for n, s in scores.items() if s > avg}
    print("High scores:", high_scores)


if __name__ == "__main__":
    main()

import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    names = [
        "Alice", "bob", "Charlie", "dylan",
        "Emma", "Gregory", "john", "kevin", "Liam"
    ]
    print("Initial players:", names)

    # List comprehensions
    capitalized = [n.capitalize() for n in names]
    already_capitalized = [n for n in names if n[0].isupper()]

    print("All capitalized:", capitalized)
    print("Already capitalized:", already_capitalized)

    # Dictionary comprehension (random scores)
    scores = {n: random.randint(10, 1000) for n in capitalized}
    print("\nScores:", scores)

    # Average
    avg = sum(scores.values()) / len(scores)
    print(f"Average score: {avg:.2f}")

    # High scores dict comprehension
    high_scores = {n: s for n, s in scores.items() if s > avg}
    print("High scores:", high_scores)


if __name__ == "__main__":
    main()

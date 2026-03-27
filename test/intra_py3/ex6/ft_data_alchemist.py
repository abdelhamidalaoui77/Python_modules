import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    initial_list = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print(f"Initial list of players: {initial_list}")
    list_capitalize = [x.capitalize() for x in initial_list]
    list_only = [x for x in initial_list if x == x.capitalize()]
    print(f"New list with all names capitalized: {list_capitalize}")
    print(f"New list of capitalized names only: {list_only}\n")
    score_dict = {name: random.randint(10, 1000) for name in list_capitalize}
    print(f"Score dict: {score_dict}")
    score_average = sum(list(score_dict.values())) / len(score_dict)
    print(f"score average is {round(score_average, 2)}")
    hight_score = {
        key: value for key, value in
        score_dict.items() if value > score_average
    }
    print(f"High scores: {hight_score}")


if __name__ == "__main__":
    main()

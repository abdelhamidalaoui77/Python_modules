import sys


def handle_invalid_inputs(arguments: list[str]) -> list[int]:
    values = []
    for e in arguments:
        try:
            num = int(e)
            values.append(num)
        except Exception:
            print(f"Invalid parameter: '{e}'")
    return values


def main():
    print("=== Player Score Analytics ===")
    if (len(sys.argv) == 1):
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        scores = handle_invalid_inputs(sys.argv[1:])
        if not scores:
            print("No scores provided. Usage: python3 ft_score_analytics.py "
                  "<score1> <score2> ...")
        else:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()

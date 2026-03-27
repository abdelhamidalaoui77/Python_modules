import sys


def handle_invalid_inputs(values: list) -> list | None:
    values = []
    for e in values:
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
        is_error = 0
        try:
            global scores
            scores = handle_invalid_inputs(sys.argv[1:])
        except Exception:
            is_error = 1
        if is_error != 1:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("An error occured while executing !!!")

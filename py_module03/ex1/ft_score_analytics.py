import sys


def handle_invalid_inputs(values) -> None:
    for e in values:
        try:
            int(e)
        except ValueError:
            raise ValueError("Invalid number")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if (len(sys.argv) == 1):
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        is_error = 0
        try:
            handle_invalid_inputs(sys.argv[1:])
        except ValueError as e:
            is_error = 1
            print(e)
        if is_error != 1:
            scores = []
            for arg in sys.argv[1:]:
                value = int(arg)
                scores.append(value)
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")

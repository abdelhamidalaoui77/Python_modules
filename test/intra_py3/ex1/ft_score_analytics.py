import sys


def score_analyst(argv: list) -> None:
    print("=== Player Score Analytics ===")
    score = []
    if len(argv) == 1:
        print(
            "No scores provided. Usage: python3"
            "ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        for arg in argv[1:]:
            try:
                score.append(int(arg))
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
        if len(score) == 0:
            print(
                "No scores provided. Usage: python3 "
                "ft_score_analytics.py <score1> <score2> ..."
            )
        else:
            total_player = len(score)
            total_score = sum(score)
            hight_score = max(score)
            low_score = min(score)
            print(f"Scores processed: {score}")
            print(f"Total players: {total_player}")
            print(f"Total score: {total_score}")
            print(f"Average score: {total_score/total_player}")
            print(f"High score: {hight_score}")
            print(f"Low score: {low_score}")
            print(f"Score range: {hight_score - low_score}")


if __name__ == "__main__":
    score_analyst(sys.argv)

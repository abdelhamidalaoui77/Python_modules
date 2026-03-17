players = ["alice", "bob", "charlie", "diana"]

scores = {
    "alice": 3500,
    "bob": 1800,
    "charlie": 4200,
    "diana": 2500
}

achievements = [
    ("alice", "First Kill"),
    ("alice", "Treasure Hunter"),
    ("charlie", "Champion"),
    ("charlie", "Master"),
    ("diana", "Survivor")
]


def ft_analytics_dashboard() -> None:

    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")

    high_players = [name for name in scores if scores[name] > 2000]
    print("High scorers (>2000):", high_players)

    double_scores = [scores[name] * 2 for name in scores]
    print("Scores doubled:", double_scores)

    active_players = [name for name in players if name in scores]
    print("Active players:", active_players)

    print("\n=== Dictionary Comprehension Examples ===")

    player_scores = {name: scores[name] for name in scores}
    print("Player scores:", player_scores)

    score_levels = {
        name: ("high" if scores[name] > 3000 else "low")
        for name in scores
    }
    print("Score categories:", score_levels)

    achievement_total = {
        name: sum(1 for p, _ in achievements if p == name)
        for name in players
    }
    print("Achievement counts:", achievement_total)

    print("\n=== Set Comprehension Examples ===")

    players_with_achievements = {p for p, _ in achievements}
    print("Players with achievements:", players_with_achievements)

    achievement_names = {a for _, a in achievements}
    print("Unique achievements:", achievement_names)

    regions = {"north", "east", "central"}
    print("Active regions:", regions)

    print("\n=== Combined Analytics ===")

    total_players = len(players)
    print("Total players:", total_players)

    total_achievements = len(achievements)
    print("Total achievements:", total_achievements)

    total_score = sum(scores.values())
    average_score = total_score / len(scores)
    print("Average score:", average_score)

    top_player = max(scores, key=scores.get)
    top_score = scores[top_player]
    top_achievements = sum(1 for p, _ in achievements if p == top_player)

    print(
        "Top performer:",
        top_player,
        f"({top_score} points, {top_achievements} achievements)"
    )


if __name__ == "__main__":
    try:
        ft_analytics_dashboard()
    except Exception as err:
        print(f"Caught error: {err}")

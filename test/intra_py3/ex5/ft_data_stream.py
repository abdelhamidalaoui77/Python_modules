import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grap",
               "move", "climp", "swim", "release"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(arr: list) -> Generator[tuple[str, str], None, None]:
    while len(arr) > 0:
        removed = random.choice(arr)
        arr.remove(removed)
        yield removed


def main():
    print("=== Game Data Stream Processor ===")
    tup = gen_event()
    for i in range(1000):
        event = next(tup)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    ten_events = [next(tup) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")
    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()

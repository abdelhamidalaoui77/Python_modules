import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    users = ["bob", "alice", "dylan", "charlie"]
    activities = ["run", "eat", "sleep", "grap",
                  "move", "climb", "swim", "release"]

    while True:
        user = random.choice(users)
        activity = random.choice(activities)
        yield (user, activity)


def consume_event(events: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        removed = random.choice(events)
        events.remove(removed)
        yield removed


def main() -> None:
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    for i in range(1000):
        user, action = next(stream)
        print(f"Event {i}: Player {user} did action {action}")

    buffer = [next(stream) for _ in range(10)]
    print("\nBuilt list of 10 events:", buffer)

    consumer = consume_event(buffer)

    for event in consumer:
        print(f"Got event from list: {event}")
        print(f"Remains in list: {buffer}")


if __name__ == "__main__":
    main()

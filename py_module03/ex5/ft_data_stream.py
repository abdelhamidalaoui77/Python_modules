import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    users = ["neo", "trinity", "morpheus", "smith"]
    activities = ["jump", "hack", "fight", "escape"]

    while True:
        user = random.choice(users)
        activity = random.choice(activities)
        yield (user, activity)


def consume_event(events: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:
    while events:
        idx = random.randrange(len(events))
        yield events.pop(idx)


def main() -> None:
    print("=== Stream Wizard ===")

    stream = gen_event()

    # 1000 events using next()
    for i in range(1000):
        user, action = next(stream)
        print(f"Event {i}: {user} performs {action}")

    # Build list of 10 events
    buffer = [next(stream) for _ in range(10)]
    print("\nBuffered events:", buffer)

    # Consume generator
    print("\nConsuming events:")
    consumer = consume_event(buffer)

    for event in consumer:
        print(f"Processed: {event}")
        print(f"Remaining: {buffer}")


if __name__ == "__main__":
    main()

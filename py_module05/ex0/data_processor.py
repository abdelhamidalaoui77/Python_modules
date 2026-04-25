from abc import ABC, abstractmethod
from typing import Any, List, Tuple


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[Tuple[int, str]] = []
        self._counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> Tuple[int, str]:
        if not self._storage:
            raise IndexError("No data to output")

        rank, value = self._storage.pop(0)
        return rank, value


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: int | float | List[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for x in data:
                self._storage.append((self._counter, str(x)))
                self._counter += 1
        else:
            self._storage.append((self._counter, str(data)))
            self._counter += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | List[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for x in data:
                self._storage.append((self._counter, x))
                self._counter += 1
        else:
            self._storage.append((self._counter, data))
            self._counter += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self._valid_dict(data)

        if isinstance(data, list):
            return all(isinstance(x, dict) and self._valid_dict(x) for x in data)

        return False

    def _valid_dict(self, d: dict) -> bool:
        return (
            isinstance(d.get("log_level"), str)
            and isinstance(d.get("log_message"), str)
        )

    def ingest(self, data: dict[str, str] | List[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for d in data:
                value = f"{d['log_level']}: {d['log_message']}"
                self._storage.append((self._counter, value))
                self._counter += 1
        else:
            value = f"{data['log_level']}: {data['log_message']}"
            self._storage.append((self._counter, value))
            self._counter += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    num = NumericProcessor()
    txt = TextProcessor()
    log = LogProcessor()

    print("Testing Numeric Processor...")
    print("Trying to validate input '42':", num.validate(42))
    print("Trying to validate input 'Hello':", num.validate("Hello"))

    test = "foo"
    print(f"\nTesting invalid ingestion of string '{test}' without prior validation:")
    try:
        num.ingest(test)
    except Exception as e:
        print("Got exception:", e)

    num.ingest([1, 2, 3, 4, 5])
    txt.ingest(["Hello", "Nexus", "World"])
    log.ingest([
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
    ])

    print("\nExtracting Numeric:")
    for _ in range(3):
        rank, value = num.output()
        print(f"Numeric value {rank}: {value}")

    print("\nExtracting Text:")
    rank, value = txt.output()
    print(f"Text value {rank}: {value}")

    print("\nExtracting Logs:")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()

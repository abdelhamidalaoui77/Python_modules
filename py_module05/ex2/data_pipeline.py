from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Protocol


# =========================================================
# ================= DATA PROCESSORS (ex0) ==================
# =========================================================

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

        return self._storage.pop(0)


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


# =========================================================
# ================= DATA STREAM (ex1) ======================
# =========================================================

class DataStream:
    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []
        self._total_processed: dict[DataProcessor, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
        self._total_processed[proc] = 0

    def process_stream(self, stream: List[Any]) -> None:
        for element in stream:
            handled = False

            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    self._total_processed[proc] += self._count_items(element)
                    handled = True

            if not handled:
                print(f"DataStream error - Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            remaining = len(proc._storage)  # allowed
            total = self._total_processed[proc]
            name = proc.__class__.__name__.replace("Processor", " Processor")

            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )

    def _count_items(self, data: Any) -> int:
        if isinstance(data, list):
            return len(data)
        return 1

    # ================== EX2 ==================

    def output_pipeline(self, nb: int, plugin: "ExportPlugin") -> None:
        for proc in self._processors:
            extracted: List[Tuple[int, str]] = []

            for _ in range(nb):
                try:
                    extracted.append(proc.output())
                except IndexError:
                    break

            if extracted:
                plugin.process_output(extracted)


# =========================================================
# ================= EXPORT PLUGINS =========================
# =========================================================

class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        ...


class CSVPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        values = [value for _, value in data]
        print("CSV Output:")
        print(",".join(values))


class JSONPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        print("JSON Output:")
        items = [f'"item_{rank}": "{value}"' for rank, value in data]
        print("{" + ", ".join(items) + "}")


# =========================================================
# ========================== MAIN ==========================
# =========================================================

def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    ds = DataStream()

    print("Initialize Data Stream...\n")
    ds.print_processors_stats()

    print("\nRegistering Processors...\n")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Use ssh instead"},
            {"log_level": "INFO", "log_message": "User connected"}
        ],
        42,
        ["Hi", "five"]
    ]

    print("Send first batch:\n")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nSend 3 processed data to CSV plugin:\n")
    ds.output_pipeline(3, CSVPlugin())
    ds.print_processors_stats()

    print("\nSend another batch:\n")
    ds.process_stream([
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE", "log_message": "Certificate expires"}
        ],
        [32, 42, 64, 84],
        "World hello"
    ])
    ds.print_processors_stats()

    print("\nSend 5 processed data to JSON plugin:\n")
    ds.output_pipeline(5, JSONPlugin())
    ds.print_processors_stats()


if __name__ == "__main__":
    main()

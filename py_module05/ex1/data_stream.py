from typing import Any, List
from ex0.data_processor import DataProcessor


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
            remaining = self._remaining(proc)
            total = self._total_processed[proc]
            name = proc.__class__.__name__.replace("Processor", " Processor")

            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )

    # ---------- Helpers ---------- #

    def _count_items(self, data: Any) -> int:
        if isinstance(data, list):
            return len(data)
        return 1

    def _remaining(self, proc: DataProcessor) -> int:
        return len(proc._storage)  # type: ignore

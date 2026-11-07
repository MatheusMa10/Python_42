from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.datas: list[Any] = []
        self.output_position = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.datas:
            raise IndexError("No data available")
        last_data = self.datas.pop(0)
        rank = self.output_position
        self.output_position += 1
        return rank, last_data


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False

        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            for item in data:
                if isinstance(item, bool) \
                   or not isinstance(item, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for i in data:
                self.datas.append(str(i))
        else:
            self.datas.append(str(data))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self.datas.append(item)
        else:
            self.datas.append(data)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True

        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False

                for key, value in item.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for item in data:
                self.datas.append(self._format_log(item))
        else:
            self.datas.append(self._format_log(data))

    def _format_log(self, log: dict[str, str]) -> str:
        level = log.get("log_level", "")
        message = log.get("log_message", "")
        return f"{level}: {message}"


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        print("CSV Output:")
        print(", ".join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")

        items = []

        for rank, value in data:
            items.append(f'"item_{rank}": "{value}"')

        print(f"{{ {', '.join(items)} }}")


class DataStream:
    def __init__(self) -> None:
        self.list_processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.list_processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        if not stream:
            raise IndexError("No data available")
        for element in stream:
            processed: bool = False
            for proc in self.list_processors:
                if proc.validate(element):
                    proc.ingest(element)
                    processed = True
                    break
            if not processed:
                print(
                    f"DataStream error: This {element} "
                    "element can not processed"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self.list_processors:
            print("No processor found, no data")
            return

        for proc in self.list_processors:
            total: int = proc.output_position + len(proc.datas)
            remaining: int = len(proc.datas)

            print(
                f"{proc.__class__.__name__}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if nb < 0:
            raise ValueError("nb cannot be negative")

        for proc in self.list_processors:
            processed_data: list[tuple[int, str]] = []

            amount = min(nb, len(proc.datas))

            for _ in range(amount):
                processed_data.append(proc.output())

            plugin.process_output(processed_data)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")

    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("Registering Processors")

    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()

    data_stream.register_processor(numeric_processor)
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)

    stream: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {stream}")
    data_stream.process_stream(stream)
    data_stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    data_stream.output_pipeline(3, csv_plugin)
    data_stream.print_processors_stats()

    stream2: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"Send another batch of data: {stream2}")
    data_stream.process_stream(stream2)
    data_stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    data_stream.output_pipeline(5, json_plugin)
    data_stream.print_processors_stats()

from abc import ABC, abstractmethod
from typing import Any


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


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    # Numeric Processor
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()

    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as error:
        print(f"Got exception: {error}")

    numbers = [1, 2, 3, 4, 5]
    print(f"Processing data: {numbers}")
    numeric.ingest(numbers)

    print("Extracting 3 values...")
    for i in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {i}: {value}")

    # Text Processor
    print("\nTesting Text Processor...")
    text = TextProcessor()

    print(f"Trying to validate input '42': {text.validate(42)}")

    words = ["Hello", "Nexus", "World"]
    print(f"Processing data: {words}")
    text.ingest(words)

    print("Extracting 1 value...")
    for i in range(1):
        rank, value = text.output()
        print(f"Text value {i}: {value}")

    # Log Processor
    print("\nTesting Log Processor...")
    logs = LogProcessor()

    print(f"Trying to validate input 'Hello': {logs.validate('Hello')}")

    entries = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server"
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!"
        }
    ]

    print(f"Processing data: {entries}")
    logs.ingest(entries)

    print("Extracting 2 values...")
    for i in range(2):
        rank, value = logs.output()
        print(f"Log entry {rank}: {value}")

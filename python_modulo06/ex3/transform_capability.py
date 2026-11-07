from abc import ABC, abstractmethod


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.is_transformed: bool = False

    @abstractmethod
    def transform(self) -> None:
        pass

    @abstractmethod
    def revert(self) -> None:
        pass

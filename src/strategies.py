from abc import ABC, abstractmethod

class ProcessingStrategy(ABC):
    @abstractmethod
    def process(self, data: list) -> list:
        pass

class EncryptionStrategy(ProcessingStrategy):
    def __init__(self, key: str):
        self.key = key

    def process(self, data: list) -> list:
        # Strategy A: XOR encryption using hex string parsed into an integer
        int_key = int(self.key, 16)
        return [val ^ int_key for val in data]

class CompressionStrategy(ProcessingStrategy):
    def __init__(self, factor: float):
        self.factor = factor

    def process(self, data: list) -> list:
        # Strategy B: Compression factor scaling
        return [round(val * self.factor, 2) for val in data]

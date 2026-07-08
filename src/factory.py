from src.strategies import EncryptionStrategy, CompressionStrategy

class StrategyFactory:
    @staticmethod
    def get_strategy(strategy_type: str, **kwargs):
        if strategy_type.lower() == "encryption":
            return EncryptionStrategy(key=kwargs.get("key", "004F"))
        elif strategy_type.lower() == "compression":
            return CompressionStrategy(factor=kwargs.get("factor", 0.85))
        else:
            raise ValueError(f"Unknown strategy type: {strategy_type}")

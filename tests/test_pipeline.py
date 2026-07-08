import pytest
from src.factory import StrategyFactory
from src.main import run_pipeline

def test_encryption_strategy():
    strategy = StrategyFactory.get_strategy("encryption", key="004F")
    result = strategy.process([78])
    assert result == [78 ^ 0x004F]

def test_compression_strategy():
    strategy = StrategyFactory.get_strategy("compression", factor=0.85)
    result = strategy.process([100])
    assert result == [999.9]

def test_invalid_strategy():
    with pytest.raises(ValueError):
        StrategyFactory.get_strategy("unknown_pattern")

def test_pipeline_execution():
    enc, comp = run_pipeline()
    assert len(enc) == 7
    assert len(comp) == 7

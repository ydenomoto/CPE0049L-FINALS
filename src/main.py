from src.factory import StrategyFactory

def run_pipeline():
    # Mandatory Dataset Parameters from assignment requirements
    dataset = [78, 82, 91, 65, 40, 99, 88]
    
    # Resolve and apply Strategy A (Encryption) with Key: 004F
    crypto_tool = StrategyFactory.get_strategy("encryption", key="004F")
    encrypted_data = crypto_tool.process(dataset)
    
    # Resolve and apply Strategy B (Compression) with Factor: 0.85
    compress_tool = StrategyFactory.get_strategy("compression", factor=0.85)
    compressed_data = compress_tool.process(dataset)
    
    return encrypted_data, compressed_data

if __name__ == "__main__":
    enc, comp = run_pipeline()
    print(f"Original:  [78, 82, 91, 65, 40, 99, 88]")
    print(f"Encrypted: {enc}")
    print(f"Compressed: {comp}")

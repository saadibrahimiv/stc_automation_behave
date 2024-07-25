
try:
    from utils.config import load_config
    config = load_config()
    print("Configuration loaded successfully")
    print(config)
except Exception as e:
    print(f"Error loading configuration: {e}")

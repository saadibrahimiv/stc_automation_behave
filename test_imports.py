
try:
    from utils.config import load_config
    print("Import load_config from utils.config successful")
except ImportError as e:
    print(f"Failed to import load_config from utils.config: {e}")

try:
    from utils.browser_factory import get_browser_instance
    print("Import get_browser_instance from utils.browser_factory successful")
except ImportError as e:
    print(f"Failed to import get_browser_instance from utils.browser_factory: {e}")

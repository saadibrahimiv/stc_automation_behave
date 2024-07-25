import importlib

class BrowserFactory:
    def __init__(self, browser_name="chrome", config=None):
        self.browser_name = browser_name.lower()
        self.browser_config = config['browsers'][self.browser_name] if config else {}

    def get_browser(self):
        driver_class = self.browser_config['driver_class']
        service_class = self.browser_config['service_class']
        driver_manager_class = self.browser_config['driver_manager']
        options_class = self.browser_config['options_class']
        options_list = self.browser_config.get('options', [])

        driver_class = self._dynamic_import(driver_class)
        service_class = self._dynamic_import(service_class)
        driver_manager_class = self._dynamic_import(driver_manager_class)
        options_class = self._dynamic_import(options_class)

        options = options_class()
        for option in options_list:
            options.add_argument(option)

        driver_manager = driver_manager_class().install()
        service = service_class(driver_manager)
        return driver_class(service=service, options=options)

    def _dynamic_import(self, class_path):
        module_path, class_name = class_path.rsplit('.', 1)
        module = importlib.import_module(module_path)
        return getattr(module, class_name)

def get_browser_instance(browser_name, config):
    factory = BrowserFactory(browser_name, config)
    return factory.get_browser()

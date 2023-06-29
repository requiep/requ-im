import os
import importlib


class RequPlug(object):
    def __init__(self, returned_data: dict = None) -> None:
        self.plugins_directory = "plugins"
        self.returned_data = returned_data

    def init_plug(self) -> None:
        plugins = []
        for plugin_file in os.listdir(self.plugins_directory):
            if plugin_file.endswith(".py"):
                plugin_name = os.path.splitext(plugin_file)[0]
                module = importlib.import_module(f"{self.plugins_directory}.{plugin_name}")
                try:
                    plugin = module.Plugin()
                    plugins.append(plugin)
                except Exception:
                    pass
        for plugin in plugins:
            try:
                plugin.init(self.returned_data)
            except Exception:
                pass

from .json_serializer import JsonSerializer
from .yaml_serializer import YamlSerializer
from .toml_serializer import TomlSerializer

class Factory:

    @staticmethod
    def create_serializer(type):
        if type == "json":
            return JsonSerializer()
        elif type == "yaml":
            return YamlSerializer()
        elif type == "toml":
            return TomlSerializer()

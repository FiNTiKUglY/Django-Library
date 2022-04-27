from .general_serializer import BaseSerializer as bs
from types import NoneType
import inspect
import toml

class TomlSerializer(bs):
    def dumps(self, data):
        dict_toml = {}
        if isinstance(data, (float, int, str, bool, list, tuple, set)):
            dict_toml["value"] = data
            string = toml.dumps(dict_toml)
        elif isinstance(data, NoneType):
            string = "value = null"
        elif isinstance(data, dict):
            string = toml.dumps(data)
        else:
            dict_toml = self.get_dict(data)
            string = toml.dumps(dict_toml)
        return string

    def get_dict(self, data):
        dict_values = {}
        temp_list = []
        if inspect.isfunction(data):
            dict_values = self.function_to_dict(data)
        elif inspect.ismethod(data):
            dict_values = self.function_to_dict(data.__func__)
        elif inspect.isclass(data):
            dict_values = self.class_to_dict(data)
            for name, value in dict_values["__dict__"].items():
                dict_values["__dict__"][name] = self.get_dict(value)
            for value in dict_values["__bases__"]:
                temp_list.append(self.get_dict(value))
            dict_values["__bases__"] = temp_list
        elif isinstance(data, (int, float, str, NoneType, bool, dict, tuple, list, set, bytes)):
            return data
        else:
            dict_values = self.object_to_dict(data)
            for key, value in dict_values.items():
                dict_values[key] = self.get_dict(value)
        return dict_values

    def set_dict(self, data):
        if len(data) == 1 and "value" in data:
            return data["value"]
        if "__code__" in data:
            data["__code__"]["co_code"] = bytes(data["__code__"]["co_code"])
            data["__code__"]["co_lnotab"] = bytes(data["__code__"]["co_lnotab"])
            data = bs.dict_to_function(data)
        elif "__bases__" in data:
            data = bs.dict_to_class(data)
        else:
            for key, value in data.items():
                if isinstance(value, dict):
                    data[key] = self.set_dict(value)
        return data

    def loads(self, string):
        if string == "value = null":
            data = None
        else:
            data = toml.loads(string)
            data = self.set_dict(data)
        return data
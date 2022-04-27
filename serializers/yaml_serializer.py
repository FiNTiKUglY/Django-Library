from .general_serializer import BaseSerializer as bs
from types import NoneType
import inspect
import yaml
from yaml.loader import FullLoader

class YamlSerializer(bs):
    def dumps(self, data):
        dict_yaml = {}
        if isinstance(data, (float, int, str, bool, NoneType, dict, list, tuple, set)):
            string = yaml.dump(data)
        else:
            dict_yaml = self.get_dict(data)
            string = yaml.dump(dict_yaml)
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
        if "__code__" in data:
            data = bs.dict_to_function(data)
        elif "__bases__" in data:
            data = bs.dict_to_class(data)
        else:
            for key, value in data.items():
                if isinstance(value, dict):
                    data[key] = self.set_dict(value)
        return data

    def loads(self, string):
        data = yaml.load(string, Loader=FullLoader)
        if isinstance(data, dict):
            data = self.set_dict(data)
        return data
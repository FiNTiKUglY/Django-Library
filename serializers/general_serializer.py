import inspect
from types import NoneType

class BaseSerializer():

    @staticmethod
    def object_to_dict(obj):
        dict_values = {}
        if inspect.isclass(obj):
            for name, value in inspect.getmembers(obj):
                if inspect.ismethod(value):
                    continue
                if not name.startswith("__"):
                    dict_values[name] = value
        elif inspect.isfunction(obj):
            return 0
        else:
            for name, value in inspect.getmembers(obj):
                if not name.startswith("__"):
                    dict_values[name] = value
        return dict_values
        
    @staticmethod
    def function_to_dict(func): #no globals and bytes
        function_members = {}
        function_code = {}

        for name, value in inspect.getmembers(func):
            if name == "__code__" or name == "__name__" or name == "__defaults__":
                function_members[name] = value
        for name, value in inspect.getmembers(function_members["__code__"]):
            if (not name.startswith("__") 
                    and isinstance(value, (int, float, str, bool, NoneType, tuple, dict, list, bytes, set))):
                function_code[name] = value

        function_members["__code__"] = function_code
        return function_members

    @staticmethod
    def dict_to_function(self):
        pass

    @staticmethod
    def dict_to_object(dict_values):
        for key, value in dict_values.items():
            if isinstance(value, dict):
                if dict_values['__code__']:
                    dict_values[key] = BaseSerializer.dict_to_functuion(value)
        return type("obj", (), dict_values)()


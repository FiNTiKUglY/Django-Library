import inspect
from os import stat
from types import NoneType, FunctionType, CodeType

class BaseSerializer():
    @staticmethod
    def class_to_dict(obj):
        class_values = {}
        bases = []
        dict_values = {}
        for name, value in inspect.getmembers(obj):
            if not name.startswith("__"):
                dict_values[name] = value
            elif name == "__init__":
                dict_values["__init__"] = value
        class_values["__dict__"] = dict_values
        class_values["__name__"] = obj.__name__
        mro = inspect.getmro(obj)
        for i in range(1, len(mro) - 1):
            bases.append(mro[i])
        class_values["__bases__"] = bases
        return class_values


    @staticmethod
    def object_to_dict(obj):
        dict_values = {}
        for name, value in inspect.getmembers(obj):
            if not name.startswith("__"):
                dict_values[name] = value
        return dict_values
        
    @staticmethod
    def function_to_dict(func):
        function_members = {}
        function_code = {}
        function_globals = {}

        for key, value in inspect.getmembers(func):
            if key == "__code__" or key == "__name__" or key == "__defaults__" or key == "__globals__":
                function_members[key] = value
        for key, value in inspect.getmembers(function_members["__code__"]):
            if (not key.startswith("__") and key != 'co_linetable'
                    and isinstance(value, (int, float, str, bool, NoneType, tuple, dict, list, bytes, set))):
                function_code[key] = value

        if function_members["__defaults__"] == None:
            function_members["__defaults__"] = []

        for elem in function_code["co_names"]:
            if elem in function_members["__globals__"]:
                value = function_members["__globals__"][elem]
            else:
                continue

            if elem == function_members["__name__"]:
                function_globals[elem] = elem

            elif isinstance(value, (int, float, bool, bytes, str, NoneType, dict, list, tuple, set)):
                function_globals[elem] = value

            elif inspect.ismodule(value):
                function_globals[value.__name__] = "__module__"

            elif inspect.isclass(value):
                function_globals[elem] = BaseSerializer.class_to_dict(value)

            elif inspect.isfunction(value):
                function_globals[elem] = BaseSerializer.function_to_dict(value)

            elif inspect.ismethod(value):
                function_globals[elem] = BaseSerializer.function_to_dict(value.__func__)

            else:
                function_globals[elem] = BaseSerializer.object_to_dict(value)
        
        function_members["__code__"] = function_code
        function_members["__globals__"] = function_globals
        return function_members

    @staticmethod
    def dict_to_function(func_values):
        func_code = {"co_argcount": None, "co_posonlyargcount": None, "co_kwonlyargcount": None, "co_nlocals": None,
                     "co_stacksize": None, "co_flags": None, "co_code": None, "co_consts": None, "co_names": None,
                     "co_varnames": None, "co_filename": None, "co_name": None, "co_firstlineno": None,
                     "co_lnotab": None, "co_freevars": (), "co_cellvars": ()}
        for key, value in func_values['__code__'].items():
            if isinstance(value, list):
                value = tuple(value)
            func_code[key] = value

        for key, value in func_values['__globals__'].items():
            if value == func_values['__name__']:
                continue

            elif value == "__module__":
                func_values["__globals__"][key] = __import__(key)

            if isinstance(value, dict):
                for name in value.keys():

                    if name == "__bases__":
                        func_values['__globals__'][key] = BaseSerializer.dict_to_class(value)

                    if name == "__code__":
                        func_values["__globals__"][key] = BaseSerializer.dict_to_function(value)

        code_list = [value for key, value in func_code.items()]
        code = CodeType(*code_list)
        func = FunctionType(code, func_values['__globals__'], func_values['__name__'], tuple(func_values['__defaults__']))
        return func

    @staticmethod
    def dict_to_class(class_values):
        bases = []
        for key, value in class_values["__dict__"].items():
            if "__code__" in value:
                class_values["__dict__"][key] = BaseSerializer.dict_to_function(value)
        for value in class_values["__bases__"]:
            bases.append(BaseSerializer.dict_to_class(value))

        return type(class_values["__name__"], tuple(bases), class_values["__dict__"])

    def dumps(self, obj):
        pass

    def dump(self, obj, fp):
        with open(fp, "w") as file:
            file.write(self.dumps(obj))

    def loads(self, string):
        pass

    def load(self, fp):
        with open(fp, "r") as file:
            return self.loads(file.read())
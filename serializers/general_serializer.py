import inspect

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
    def function_to_dict(func):
        result_code = {}
        result_globals = {}

        attributes = dict(inspect.getmembers(func))
        attributes_code = dict(inspect.getmembers(attributes['__code__']))

        for key, value in attributes_code.items():
            if key[0] != "_" and key != "replace" and key != "co_lines" and key != 'co_linetable':
                if isinstance(value, str) and len(value) == 0:
                    result_code[key] = None
                else:
                    result_code[key] = value

        for element in attributes_code["co_names"]:
            if element in attributes["__globals__"]:
                value = attributes["__globals__"][element]
            else:
                continue

            if element == attributes["__name__"]:
                result_globals[element] = element

            elif isinstance(value, (int, float, bool, bytes, str)):
                result_globals[element] = value

            elif isinstance(value, dict):
                result_globals[element] = value

            elif isinstance(value, (list, set, frozenset, tuple)):
                result_globals[element] = value

        return {"__code__": result_code, "__globals__": result_globals, "__name__": attributes['__name__'],
                "__defaults__": attributes['__defaults__'], }

    @staticmethod
    def dict_to_function(self):
        pass

    @staticmethod
    def dict_to_object(dict_values):
        for key, value in dict_values.items():
            if isinstance(value, dict):
                if dict_values['__code__']:
                    dict_values[key] = BaseSerializer.dict_to_functuion(value)
        return type("mytype", (), dict_values)()


import inspect

class BaseSerializer():
    def object_to_dict(self, obj):
        list = []
        dict = {}
        if inspect.isclass(obj):
            for name, data in inspect.getmembers(obj):
                if inspect.ismethod(data):
                    continue
                if not name.startswith("__"):
                    list.append((name, data))
            dict.update(list)
        elif inspect.isfunction(obj):
            return 0
        else:
            for name, data in inspect.getmembers(obj):
                if inspect.ismethod(data):
                    continue
                elif not name.startswith("__"):
                    list.append((name, data))
            dict.update(list)
        return dict
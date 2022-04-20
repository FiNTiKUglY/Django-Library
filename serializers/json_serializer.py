from .general_serializer import BaseSerializer

class JsonSerializer(BaseSerializer):
    def list_to_str(self, list):
        string = ''
        for row in list:
            string = string + row + '\n'
        string = string[:-1]
        return string

    def get_simple_value(self, value):
        if type(value) == bool:
            row = str(value).lower()
        elif type(value) == str:
            row = f"\"{value}\""
        elif type(value) == float or type(value) == int:
            row = str(value)
        elif value is None:
            row = "null"
        return row + ','

    def get_dict(self, data, indent):
        rows = []
        indent += 4
        for key, value in data.items():
            row = ' ' * indent + f"\"{key}\": "
            if isinstance(value, (float, int, str, bool)) or value is None:
                row += self.get_simple_value(value)
                rows.append(row)
            elif isinstance(value, (dict)):
                rows.append(row + "{")
                row = self.get_dict(value, indent)
                rows = rows + row
            elif isinstance(value, (list, tuple, set)):
                rows.append(row + "[")
                row = self.get_list(value, indent)
                rows = rows + row
            else:
                rows.append(row + "{")
                value = self.object_to_dict(value)
                row = self.get_dict(value, indent)
                rows = rows + row
        indent -= 4
        rows[-1] = rows[-1][:-1]
        rows.append(' ' * indent + '},')
        return rows

    def get_list(self, data, indent):
        rows = []
        indent += 4
        for value in data:
            if isinstance(value, (float, int, str, bool)):
                row = ' ' * indent + self.get_simple_value(value)
                rows.append(row)
            elif isinstance(value, (dict)):
                rows.append(' ' * indent + "{")
                row = self.get_dict(value, indent)
                rows = rows + row
            elif isinstance(value, (list, tuple, set)):
                rows.append(' ' * indent + "[")
                row = self.get_list(value, indent)
                rows = rows + row
            else:
                rows.append(' ' * indent + "{")
                value = self.object_to_dict(value)
                row = self.get_dict(value, indent)
                rows = rows + row
        indent -= 4
        rows[-1] = rows[-1][:-1]
        rows.append(' ' * indent + '],')
        return rows

    def dumps(self, data, indent = 0):
        rows = []
        if isinstance(data, (float, int, str, bool)):
            string = self.get_simple_value(data)
            string = string[:-1]
        elif isinstance(data, dict):
            rows.append('{')
            row = self.get_dict(data, indent)
            rows = rows + row
            rows[-1] = rows[-1][:-1]
            string = self.list_to_str(rows)
        elif isinstance(data, (tuple, list, set)):
            rows.append('[')
            row = self.get_list(data, indent)
            rows = rows + row
            rows[-1] = rows[-1][:-1]
            string = self.list_to_str(rows)
        else:
            data = self.object_to_dict(data)
            rows.append('{')
            row = self.get_dict(data, indent)
            rows = rows + row
            rows[-1] = rows[-1][:-1]
            string = self.list_to_str(rows)
        return string

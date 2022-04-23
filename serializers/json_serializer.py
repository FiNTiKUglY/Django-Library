import inspect
from multiprocessing.context import set_spawning_popen
import re
from types import NoneType
from xml.etree.ElementTree import tostring
from .general_serializer import BaseSerializer

class JsonSerializer(BaseSerializer):
    def list_to_str(self, list):
        string = ''
        for row in list:
            string = string + row + '\n'
        string = string[:-1]
        return string

    def get_simple_value(self, value):
        if isinstance(value, bool):
            row = str(value).lower()
        elif isinstance(value, str):
            row = f"\"{value}\""
        elif isinstance(value, (int, float)):
            row = str(value)
        elif value is None:
            row = "null"
        elif isinstance(value, bytes):
            row = 'bytes' 
        return row + ','
    
    def set_simple_value(self, string):
        if string[0] == '\"':
            value = re.sub(r'["]', '', string)
        elif string == 'null':
            value = None
        elif string == 'true':
            value = True
        elif string == 'false':
            value = False
        elif re.search(r'[.]', string):
            value = float(string)
        else:
            value = int(string)
        return value

    def get_dict(self, data, indent):
        rows = []
        indent += 4
        for key, value in data.items():
            row = ' ' * indent + f"\"{key}\": "
            if isinstance(value, (float, int, str, bool, NoneType)):
                row += self.get_simple_value(value)
                rows.append(row)
            elif isinstance(value, (dict)):
                if not value:
                    rows.append(row + "{" + "},")
                else:
                    rows.append(row + "{")
                    row = self.get_dict(value, indent)
                    rows = rows + row
            elif isinstance(value, (list, tuple, set)):
                if not value:
                    rows.append(row + "[" + "],")
                else:
                    rows.append(row + "[")
                    row = self.get_list(value, indent)
                    rows = rows + row
            elif isinstance(value, bytes):
                rows.append(row + 'bytes')
            elif inspect.isfunction(value):
                rows.append(row + '{')
                temp = self.function_to_dict(value)
                row = self.get_dict(temp, indent)
                rows = rows + row
            elif inspect.ismethod(value):
                rows.append(row + '{')
                temp = self.function_to_dict(value.__func__)
                row = self.get_dict(temp, indent)
                rows = rows + row
            else:
                rows.append(row + "{")
                temp = self.object_to_dict(value)
                row = self.get_dict(temp, indent)
                rows = rows + row
        indent -= 4
        rows[-1] = rows[-1][:-1]
        rows.append(' ' * indent + '},')
        return rows

    def set_dict(self, rows, index):
        dict_values = {}
        for row in rows:
            if rows[index] == '}':
                return dict_values, index + 1
            items = rows[index].split(":")
            key = re.sub(r'["]', '', items[0])
            if items[1] == '[':
                value, index = self.set_list(rows, index + 1)
                dict_values[key] = value
            elif items[1] == '{':
                value, index = self.set_dict(rows, index + 1)
                dict_values[key] = value
            else:
                dict_values[key] = self.set_simple_value(items[1])
                index += 1

    def get_list(self, data, indent):
        rows = []
        indent += 4
        for value in data:
            if isinstance(value, (float, int, str, bool, NoneType)):
                row = ' ' * indent + self.get_simple_value(value)
                rows.append(row)
            elif isinstance(value, (dict)):
                if not value:
                    rows.append(' ' * indent + "{" + "},")
                else:
                    rows.append(' ' * indent + "{")
                    row = self.get_dict(value, indent)
                    rows = rows + row
            elif isinstance(value, (list, tuple, set)):
                if not value:
                    rows.append(' ' * indent + "[" + "],")
                else:
                    rows.append(' ' * indent + "[")
                    row = self.get_list(value, indent)
                    rows = rows + row
            else:
                rows.append(' ' * indent + "{")
                temp = self.object_to_dict(value)
                row = self.get_dict(temp, indent)
                rows = rows + row
        indent -= 4
        rows[-1] = rows[-1][:-1]
        rows.append(' ' * indent + '],')
        return rows

    def set_list(self, rows, index):
        list_values = []
        for row in rows:
            if rows[index] == '[':
                result, index = self.set_list(rows, index + 1)
                list_values.append(result)
            elif rows[index] == '{':
                result, index = self.set_dict(rows, index + 1)
                list_values.append(result)
            elif rows[index] == ']':
                return list_values, index + 1
            else:
                list_values.append(self.set_simple_value(rows[index]))
                index += 1

    def dumps(self, data, indent = 0):
        rows = []
        if isinstance(data, (float, int, str, bool, NoneType)):
            string = self.get_simple_value(data)
            string = string[:-1]
        elif isinstance(data, dict):
            rows.append('{')
            if not data:
                rows[-1] = '{' + '}'
            else:
                row = self.get_dict(data, indent)
                rows = rows + row
                rows[-1] = rows[-1][:-1]
            string = self.list_to_str(rows)
        elif isinstance(data, (tuple, list, set)):
            rows.append('[')
            if not data:
                rows[-1] = '[' + ']'
            else:
                row = self.get_list(data, indent)
                rows = rows + row
                rows[-1] = rows[-1][:-1]
            string = self.list_to_str(rows)
        elif inspect.isfunction(data):
            rows.append('{')
            temp = self.function_to_dict(data)
            row = self.get_dict(temp, indent)
            rows += row
            rows[-1] = rows[-1][:-1]
            string = self.list_to_str(rows)
        elif inspect.ismethod(data):
            rows.append('{')
            temp = self.function_to_dict(data.__func__)
            row = self.get_dict(temp, indent)
            rows += row
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
    
    def loads(self, string):
        rows = string.split('\n')
        for i in range(len(rows)):
            rows[i] = re.sub(r'[ |,]', '', rows[i])
        if rows[0] == '[':
            data, temp = self.set_list(rows, 1)
        elif rows[0] == '{':
            data, temp = self.set_dict(rows, 1)
        else:
            data = self.set_simple_value(rows[0])
        return data
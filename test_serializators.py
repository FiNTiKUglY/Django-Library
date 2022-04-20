from serializers.json_serializer import JsonSerializer
import json
from test_values import TestClassWithMethods, TestFullClass, TestFullClassWithMethods, test_int, \
                        test_float, test_bool, test_str, test_func, test_none, test_dict, test_list

obj = TestFullClass()
ser = JsonSerializer()
test1 = ser.dumps(obj)
print(test1)
test_ = ser.object_to_dict(obj)
print(test_)
test2 = json.dumps(test_, indent=4)
print(test2)
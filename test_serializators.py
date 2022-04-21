from serializers.json_serializer import JsonSerializer
#from serializers.toml_serializer import TomlSeriaizer
#from serializers.yaml_serializer import YamlSeriaizer
from serializers.general_serializer import BaseSerializer as bs

import json
from test_values import TestClassWithMethods, TestFullClass, TestFullClassWithMethods, test_int, \
                        test_float, test_bool, test_str, test_func, test_none, test_dict, test_list

test_class_methods = TestClassWithMethods()
test_fullclass = TestFullClass()
test_fullclass_methods = TestFullClassWithMethods()
ser_json = JsonSerializer()

print(json.dumps(test_int, indent=4) == ser_json.dumps(test_int))
print(json.dumps(test_float, indent=4) == ser_json.dumps(test_float))
print(json.dumps(test_bool, indent=4) == ser_json.dumps(test_bool))
print(json.dumps(test_str, indent=4) == ser_json.dumps(test_str))
print(json.dumps(test_none, indent=4) == ser_json.dumps(test_none))
print(json.dumps(test_dict, indent=4) == ser_json.dumps(test_dict))
print(json.dumps(test_list, indent=4) == ser_json.dumps(test_list))
print(json.dumps(bs.object_to_dict(test_fullclass), indent=4) == 
                       ser_json.dumps(test_fullclass))

print("--------------------------------------------------------------------------")

print(test_int == ser_json.loads(json.dumps(test_int, indent=4)))
print(test_float == ser_json.loads(json.dumps(test_float, indent=4)))
print(test_str == ser_json.loads(json.dumps(test_str, indent=4)))
print(test_bool == ser_json.loads(json.dumps(test_bool, indent=4)))
print(test_none == ser_json.loads(json.dumps(test_none, indent=4)))
print(test_dict == ser_json.loads(json.dumps(test_dict, indent=4)))
print(test_list == ser_json.loads(json.dumps(test_list, indent=4)))
print(bs.object_to_dict(test_fullclass) == 
        ser_json.loads(json.dumps(bs.object_to_dict(test_fullclass), indent=4)))

from serializers.json_serializer import JsonSerializer
#from serializers.toml_serializer import TomlSeriaizer
from serializers.yaml_serializer import YamlSerializer
from serializers.general_serializer import BaseSerializer as bs

from test_values import TestFullClass, TestFullClassWithMethods, test_int, test_bytes, \
                        test_float, test_bool, test_str, test_func, test_none, test_dict, test_list

test_fullclass = TestFullClass()
test_fullclass_methods = TestFullClassWithMethods()
ser_json = JsonSerializer()
ser_yaml = YamlSerializer()

print(test_int == ser_json.loads(ser_json.dumps(test_int)))
print(test_float== ser_json.loads(ser_json.dumps(test_float)))
print(test_bool == ser_json.loads(ser_json.dumps(test_bool)))
print(test_str == ser_json.loads(ser_json.dumps(test_str)))
print(test_none == ser_json.loads(ser_json.dumps(test_none)))
print(test_dict == ser_json.loads(ser_json.dumps(test_dict)))
print(test_list == ser_json.loads(ser_json.dumps(test_list)))
print(test_bytes == ser_json.loads(ser_json.dumps(test_bytes)))
print(bs.object_to_dict(test_fullclass) == ser_json.loads(ser_json.dumps(test_fullclass)))
print(test_func() == ser_json.loads(ser_json.dumps(test_func))())
print(test_func(51) == ser_json.loads(ser_json.dumps(test_func))(51))

print("--------------------------------------------------------------------------")

print(test_int == ser_yaml.loads(ser_yaml.dumps(test_int)))
print(test_float== ser_yaml.loads(ser_yaml.dumps(test_float)))
print(test_bool == ser_yaml.loads(ser_yaml.dumps(test_bool)))
print(test_str == ser_yaml.loads(ser_yaml.dumps(test_str)))
print(test_none == ser_yaml.loads(ser_yaml.dumps(test_none)))
print(test_dict == ser_yaml.loads(ser_yaml.dumps(test_dict)))
print(test_list == ser_yaml.loads(ser_yaml.dumps(test_list)))
print(test_bytes == ser_yaml.loads(ser_yaml.dumps(test_bytes)))
print(bs.object_to_dict(test_fullclass) == ser_yaml.loads(ser_yaml.dumps(test_fullclass)))
print(test_func() == ser_yaml.loads(ser_yaml.dumps(test_func))())
print(test_func(51) == ser_yaml.loads(ser_yaml.dumps(test_func))(51))


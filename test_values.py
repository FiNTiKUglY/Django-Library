class TestFullClass():
    def __init__(self):
        self.creation = True
        self.age = 15
        self.weigth = 65.5
        self.name = "BB23A"
        self.list = [[11, 12], [12, [13, 14, [{"aboba" : 12, "neaboba" : 14}, 16]]], [13, 14, 15]]
        self.quest = None


class TestFullClassWithMethods():
    def __init__(self):
        self.creation = True
        self.age = 15
        self.weigth = 65.5
        self.name = "BB23A"
        self.list = [[11, 12], [12, [13, 14, [{"aboba" : 12, "neaboba" : 14}, 16]]], [13, 14, 15]]
        self.quest = None
    
    def zark(iz):
        if iz is None:
            print("ill")
        else:
            iz = 2
        return iz


class TestClassWithMethods():
    def zark(iz):
        if iz is None:
            print("ill")
        else:
            iz = 2
        return iz

test_int = 11
test_float = 12.2
test_str = "hello1"
test_bool = False
test_none = None
test_list = [12, [13, [14, 15]]]
test_dict = {"first" : 1, "second" : {"third": "3", "fourth" : True}}

def test_func(s = 5):
    i = 1
    for j in range(s, test_int):
        i *= 2
    return i
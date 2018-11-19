def sort_asc_dsc_dict(input_dict):
    sorted_asc=sorted(input_dict.items(),key=lambda x:x[1] ,reverse=True)
    sorted_dsc=sorted(input_dict.items(),key=lambda x:x[1])

    return dict(sorted_asc),dict(sorted_dsc)

def add_key_dict(input_dict):
    input_dict[2]=30
    return input_dict

def concatenate_dict(dict1,dict2,dict3):
    return dict(dict1.items()+dict2.items()+dict3.items())

def key_exist_dict(dict,str):
    if str in dict:
        return True
    return False

def forloop_over_dict(dict):
    for x in dict.values():
        print(x)
def generate_dict(number):
    dic={}
    for i in range(1,number+1):
        dic[i]=i**2

    return dic
def key_value_square():
    dic={}
    for i in range(1,16):
        dic[i]=i**2

    return dic
def merge_dict(dict1,dict2):
     dict1.update(dict2)
     return dict1

def sum_item_dict(dic):
    return sum(dic.values())


def multiply_items_dict(dic):
    mul=1
    for x in dic.values():
        mul=mul*x
    return mul

def remove_key_dict(dic,key):
    del dic[key]
    return dic

def map_twolists_dict(key,value):
    final_dict=dict(zip(key,value))
    return final_dict

def sort_dict_through_key(dic):
    sort_key_dict=sorted(dic.items(),key=lambda x:x[0])
    return dict(sort_key_dict)

def max_min_dict(dic):
    return max(dic.values()),min(dic.values())

def remove_duplicate(dic):
    tups=list(set(dic.items()))
    di={}
    di=dict(tups)
    return di

def check_empty_dict(dic):
    if len(dic)!=0:
        return False
    return True
def test_sort_asc_dsc_dict():
    assert ({'model': 'Mustang', 'brand': 'Ford', 'color': 'red'},{'brand': 'Ford', 'model': 'Mustang', 'color': 'red'}) ==sort_asc_dsc_dict({"brand": "Ford","model": "Mustang","color":"red"})

def test_add_key():
    assert {0: 10, 1: 20, 2: 30}==add_key_dict({0: 10, 1: 20})

def test_concatenate_dict():
    assert {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}==concatenate_dict({1:10, 2:20},{3:30, 4:40},{5:50,6:60})


def test_exist_key_dict():
    assert True==key_exist_dict({"brand": "Ford","model": "Mustang","color":"red"},"color")

def test_forloop_over_dict():
    forloop_over_dict({"brand": "Ford","model": "Mustang","color":"red"})

def test_generate_dict():
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}==generate_dict(5)

def test_key_value_square():
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}==key_value_square()

def test_merge_dict():
    assert {"brand": "ford","model": "mustang","color":"Red","house" : "Haus", "cat":"Katze"}==merge_dict({"brand": "ford","model": "mustang","color":"Red"},{"house" : "Haus", "cat":"Katze"})

def test_sum_dict():
    assert 793==sum_item_dict({'data1':100,'data2':-54,'data3':247,'data4':500})

def test_multiply_dict():
    assert 60000==multiply_items_dict({'data1':10,'data2':4,'data3':30,'data4':50})

def test_remove_key_dict():
    assert {"brand": "Ford","model": "Mustang"}==remove_key_dict({"brand": "Ford","model": "Mustang","color":"red"},"color")

def test_map_twolists_dict():
    assert {'color1':'red','color2':'green','color3':'blue'}==map_twolists_dict(['color1','color2','color3'],['red','green','blue'])

def test_sort_dict_usingkey():
  assert {'color': 'Red', 'brand': 'ford', 'model': 'mustang'}== sort_dict_through_key({"brand": "ford","model": "mustang","color":"Red"})

def test_max_min_dict():
    assert (500,-54)==max_min_dict({'data1':100,'data2':-54,'data3':247,'data4':500})

def test_dictionary_object_field():
    class dictObj(object):
        def __init__(self):
            self.x = 'red'
            self.y = 'Yellow'
            self.z = 'Green'

        def do_nothing(self):
            pass

    test=dictObj()
    print(test.__dict__)

def test_remove_dict():
    assert {'color': 'Red', 'brand': 'ford', 'model': 'mustang'}==remove_duplicate({'color': 'Red', 'brand': 'ford', 'model': 'mustang','color': 'Red'})

def test_empty_dict():
    assert True==check_empty_dict({})
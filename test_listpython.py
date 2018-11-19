
def sum_all_Items(input_list):
    sum=0
    for n in input_list:
        sum+=n
    return sum


def mul_all_items(input_list):
    mul=1
    for n in input_list:
        mul*=n
    return mul


def largest_and_smallest_list(input_list):
    list=[]
    maximum=max(input_list)
    mininmum=min(input_list)
    list.append(maximum)
    list.append((mininmum))
    return list


def check_Palindrome(str):
    return (str==''.join(reversed(str)))


def count_fisrt_last_char_same(input_list):
    count=0
    for str in input_list:

        if str[0]==str[-1]:
            count+=1

    return count

def sort_tuple_list_by_lastelement(input_list):
    sortedlist=sorted(input_list, key=lambda x:x[-1])
    return sortedlist


def remove_duplicates(input_list):

    uniquelist=[]
    [uniquelist.append(ele) for ele in input_list if ele not in uniquelist]
    return uniquelist


def check_list_empty(input_list):
    if len(input_list)!=0:
        return False

    return True


def clone_or_copy(input_list):
    listItems=input_list[:]
    return  listItems

def list_word_longer_number(str,num):
    str=str.split(" ")
    items=[]
    [items.append(word) for word in str if len(word)>num]
    return items

def find_common_lists(input_list1,input_list2):
    for member in input_list1:
        if member in input_list2:
            return True
    return False
def remove_position_even(input_list):

    del input_list[5]
    del input_list[4]
    del input_list[2]
    del input_list[0]

    return input_list

def remove_nonalphbets(str):

    alphastr=[ch for ch in str if ch.isalpha() or ch.isdigit()]
    return ''.join(alphastr)

def remove_evennumbers(input_list):
    for x in input_list:
        if x%2==0:
            input_list.remove(x)

    return input_list

from random import shuffle
def shuffle_list(input_list):
    shuffle(input_list)
    print(input_list)

def fisrt_last_five_elements():
    li=[]
    for i in range(1,31):
        li.append(i**2)

    return li[:5],li[-5:]

def except_fisrt_five_elements():
    li=[]
    for i in range(6,31):
        li.append(i**2)

    print(li)

import itertools
def permutation_list(input_list):
    return list(itertools.permutations(input_list))


def difference_two_lists(input_list1,input_list2):
    return list(set(input_list1)-set(input_list2))


def index_list(input_list,str):

    return input_list.index(str)

def char_convert_string(input_list):

    return ''.join(input_list)


def item_list_usingindex(input_list,num):
    return input_list[num]

def remove_adjacent_duplicates(input_list,length):
    li=[]
    for i in range(0,length-1):
        if(input_list[i]!=input_list[i+1]):
            li.append(input_list[i])

    li.append(input_list[length-1])
    return li


def append_list1_to_list2(input_list1,input_list2):
    return input_list1+input_list2

import random
def random_list(input_list):
    print(random.choice(input_list))


def check_circular_list(input_list1,input_list2):
    return (''.join(map(str,input_list2)) in ''.join(map(str,input_list1*2)))

def test_sum_list():
    assert 1==sum_all_Items([1])
    assert 10 == sum_all_Items([1,3,4,2])
    assert 20 == sum_all_Items([10,5,3,9,-7])

def test_multi_list():
    assert 20==mul_all_items([1,2,5,2])
    assert 10 == mul_all_items([2, 1, 1, 5])
    assert 30 == mul_all_items([2, 3, 5, 1])

def test_largest_smallest():
    assert[5,1]==largest_and_smallest_list([1,5,4,3,2])
    assert [70, 10] == largest_and_smallest_list([20, 50, 40, 30, 10,70])
    assert [9, 0] == largest_and_smallest_list([1, 9, 0, 3, 2])

def test_check_palindrome():
    assert True==check_Palindrome("madam")
    assert False==check_Palindrome("Hello")
    assert  True==check_Palindrome("level")
    assert  True==check_Palindrome("racecar")
    assert False==check_Palindrome("python")

def test_first_last_char_same():
    assert 2==count_fisrt_last_char_same(['abc', 'xyz', 'aba', '1221'])
    assert 5== count_fisrt_last_char_same(['aba', 'xyx', 'aba', '1221','131'])
    assert 0==count_fisrt_last_char_same(['abc', 'xyz', 'abd', '1220'])

def test_sort_list_tuple_lastelement():
    assert [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]==sort_tuple_list_by_lastelement([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
    assert [(1, 1), (3, 4), (3, 7), (8, 7), (2, 9)]==sort_tuple_list_by_lastelement([(3, 4),(1, 1),(3, 7),(2, 9),(8, 7)])

def test_remove_duplicates():
    assert [1,3,2,4]==remove_duplicates([1,3,2,1,3,1,4])
    assert [0, 5, 3, 4] == remove_duplicates([0, 5, 5, 0, 3, 0, 3, 5, 4])

def test_list_empty():
    assert True==check_list_empty([])
    assert False == check_list_empty([1,2,3])

def test_clone_copy():
    assert [1,2,3,4]==clone_or_copy([1,2,3,4])

def test_list_word_longer_n():
    assert ["quick","brown","jumps","over","lazy"]==list_word_longer_number("The quick brown fox jumps over the lazy dog",3)

def test_one_common_member_twolists():
    assert True==find_common_lists([1,2,5,3,4],[1,3,4,6,7,8])
    assert False == find_common_lists([1,2,3,4,5], [6,7,8,9])

def test_remove_position_even():
    assert ['Green', 'Black']==remove_position_even(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])

def test_remove_nonalphbets():
    assert "ab2344"==remove_nonalphbets("ab$23#44")

def test_remove_evennumber():
    assert [1,3,5,7,9]==remove_evennumbers([1,2,3,4,5,6,7,8,9])

def test_shuffle_list():
    shuffle_list(["Red","green","black","yellow"])


def test_fisrt_last_five_element():
    assert ([1,4,9,16,25],[676,729,784,841,900])==fisrt_last_five_elements()

def test_except_first_five_elements():
    except_fisrt_five_elements()

def test_permutation_list():
    assert [(1,2),(2,1)]==permutation_list([1,2])
    assert [(1, 2, 3),(1, 3, 2),(2, 1, 3),(2, 3, 1),(3, 1, 2),(3, 2, 1)] == permutation_list([1, 2, 3])

def test_difference_two_lists():
    assert ["green","red"]==difference_two_lists(["red","yellow","green","white"],["yellow","white"])

def test_index_list():
    assert 1==index_list(["foo","bar","red","green","yellow"],"bar")

def test_char_convert_string():
    assert "manoj"==char_convert_string(['m','a','n','o','j'])

def test_item_list():
    assert "bar"==item_list_usingindex(["foo","bar","red","green","yellow"],1)

def test_remove_adjacent_duplicates():
    assert [1,2,5,2,6,3,2,6,9]==remove_adjacent_duplicates([1,2,2,5,2,6,6,6,3,2,6,9],12)

def test_append_list1_to_list2():
    assert ["red","green","yellow","white"]==append_list1_to_list2(["red","green"],["yellow","white"])

def test_random_list():
    random_list([1,2,3,4,5,6,7,8,9])

def test_circular_list():
    assert True==check_circular_list([10,10,0,0,10],[10,10,10,0,0])
    assert False==check_circular_list([10,10,0,0,10],[1,10,10,0,0])
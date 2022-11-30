# NAVI SINGH
# Cite any sources you used to help with the homework including TAs and classmates:
# https://www.geeksforgeeks.org/python-list-sort-method/
# https://www.guru99.com/find-average-list-python.html

def string3(string):
    new_string = string[len(string)-2:]
    return new_string * 3

    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
    The string length will be at least 2.
    """


def has123(nums):
    for i in range(0, len(nums) - 2):
        if nums[i] == 1:
            if nums[i+1] == 2:
                if nums[i+2] == 3:
                    return True
    return False
    
    """
    Given an list of ints, return True if the sequence of numbers
    1, 2, 3 appears in the list somewhere.
    """


# string 2 count_code
def hascode(string):
    count = 0
    index = 0

    word = ["co" + i + "e" for i in string.lower()]
    for i in word:
        if i in string[index:]:
            index = string.find(i) + 1
            count += 1

    return count

    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except we'll accept any letter for the 'd', so "cope" and "cooe" count.
    """


def samecatdog(string):
    cat_index = 0;
    dog_index = 0;

    for i in string:
        if "cat" in string:
            cat_index+=1
            #return cat_index
        if "dog" in string:
            dog_index+=1
            #return dog_index

    if cat_index == dog_index:
        return True
    return False

    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    *** This can be simplfied using a Python string method ***
    """


def centered_avg(nums):
    length = len(nums)
    last = length - 1
    
    nums.sort()    
    nums.remove(nums[last]) # removes the last integer
    nums.remove(nums[0]) # removes the first integer
    
    # Compute the average:
    add = sum(nums)
    avg = add // len(nums)
    return avg

    """
    Return the "centered" average of a list of ints, which we'll say is the mean average of the
    values, except ignoring the largest and smallest values in the list. If there are
    multiple copies of the smallest value, use just one copy, and likewise for the largest value.
    Use floor division to produce the final average. You may assume that the list is length 3 or more.
    """


# Test functions
assert string3("Hello") == 'lololo', 'string3(Hello) expected lololo'
print("correct")
assert string3("ab") == 'ababab', 'string3(ab) expected ababab'
print("correct")
assert string3("Hi") == 'HiHiHi', 'string3(Hi) expected HiHiHi'
print("correct")

assert has123([1, 1, 2, 3, 1]) is True, '[1, 1, 2, 3, 1] has 123'
print("correct")
assert has123([1, 1, 2, 4, 1]) is False, '[1, 1, 2, 4, 1] does not have 123'
print("correct")
assert has123([1, 1, 2, 1, 2, 3]) is True, '[1, 1, 2, 1, 2, 3] has 123'
print("correct")

assert hascode("aaacodebbb") == 1, 'aaacodebbb has code'
print("correct")
assert hascode("aaacodebbb") == 1, 'codexxcode has code'
print("correct")
assert hascode("cozexxcope") == 2, 'cozexxcope has code'
print("correct")

assert samecatdog("catdog") is True, 'catdog appear same number of times'
print("correct")
assert samecatdog("catcat") is False, 'catcat does not appear same number of times'
print("correct")
assert samecatdog("1cat1cadodog") is True, '1cat1cadodog appear the same number of times'
print("correct")

assert centered_avg([1, 2, 3, 4, 100]) == 3, 'average [1, 2, 3, 4, 100] is 3'
print("correct")
assert centered_avg([1, 1, 5, 5, 10, 8, 7]) == 5, 'average [1, 1, 5, 5, 10, 8, 7] is 5'
print("correct")
assert centered_avg([-10, -4, -2, -4, -2, 0]) == -3, 'average [-10, -4, -2, -4, -2, 0] is -3'
print("correct")


# Problems found on https://codingbat.com/python
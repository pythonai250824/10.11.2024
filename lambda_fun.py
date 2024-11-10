
# function is_negative, that gets int number param and returns bool
# return True if its negative otherwise return False
# -5 True, because it is negative
# 3 False, because it is not negative
# 0 False, because it is not negative

def is_negative(num: int) -> bool:
    if num < 0:
        return True
    else:
        return False
    # return num < 0

is_negative_lm = lambda num: num < 0

print(is_negative_lm(-5), is_negative(-5))
print(is_negative_lm(3), is_negative(3))
print(is_negative_lm(0), is_negative(0))

# write fun gets int return int
#     which returns number power 2 , hint: x ** 2
# write it again with lambda
# execute both with 0, 3, 9

def power2(num: int) -> int:
    return num ** 2

power2_lm = lambda num: num ** 2

print(power2(0), power2_lm(0))
print(power2(3), power2_lm(3))
print(power2(9), power2_lm(9))

is_zero = lambda x: x == 0

inc_one = lambda x: x + 1

# list_num: list[int] = [-4, 0, 2, -1, 3, 9]
# result_list only positive numbers of list_num
list_num: list[int] = [-4, 0, 2, -1, 3, 9]
result_list: list[int] = []
for i in list_num:
    if i > 0:
        result_list.append(i)

# filter map sorted
print(list(range(10)))
print(list(filter(lambda x: x > 0, [-4, 0, 2, -1, 3, 9])))
# [-4, 0, 2, -1, 3, 9]
# filter: elements which are not zero
print(list(filter(lambda x: x != 0, [-4, 0, 2, -1, 3, 9])))
# filter: elements which are even
print(list(filter(lambda x: x % 2 == 0, [-4, 0, 2, -1, 3, 9])))
# filter: elements which are even and positive
print(list(filter(lambda x: x > 0 and x % 2 == 0, [-4, 0, 2, -1, 3, 9])))

print(list(filter(lambda x: True, [-4, 0, 2, -1, 3, 9])))
print(list(filter(lambda x: False, [-4, 0, 2, -1, 3, 9])))
# if x -------> if x != 0
print(list(filter(lambda word: word.upper().startswith("A"),
                  ["apple", "Anaconda", "banana", "pine-apple", "coconut", "Am-pm"])))

# list( filter (who do i want? , [ ... ] ) )
# filter (who do i want? , [ ... ] )
# filter ( lambda , [ .. ] )
# filter ( lambda x: x > 0, [ .. ] )
# make a new list using filter with words longer than 6 letters
print(list(filter(lambda word: len(word) > 6,
                  ["apple", "Anaconda", "banana", "pine-apple", "coconut", "Am-pm"])))
# make a new list using filter with words that contains - (minus)
print(list(filter(lambda word: '-' in word,
                  ["apple", "Anaconda", "banana", "pine-apple", "coconut", "Am-pm"])))

# map
list_num: list[int] = [-4, 0, 2, -1, 3, 9]
result_list: list[int] = []
for i in list_num:
    result_list.append(i ** 2)
print(list_num)
print(result_list)

# list(map ( how to change? , [ .. ] ))
# list(map ( lambda x: x , [ .. ] ))
print('map1', list(map(lambda x: x, [-4, 0, 2, -1, 3, 9] )))
print('map2', list(map(lambda x: x ** 2, [-4, 0, 2, -1, 3, 9] )))
print('    ',[54, 20, 12, 133, 83, 9989])
print('map3', list(map(lambda x: x % 10, [54, 20, 12, 133, 83, 9989] )))
print('map4', list(map(lambda x: x % 2 == 0, [54, 20, 12, 133, 83, 9989] )))

# ["zzzzz", "b", "abc", "cccc", "bb", "t"] --> list of len
#   5        1     3     4        2    1
print('    ', ["zzzzz", "b", "abc", "cccc", "bb", "t"])
print('map5', list(map(lambda w: len(w), ["zzzzz", "b", "abc", "cccc", "bb", "t"])) )

# [54, 20, 12, 13, 83, 99] --> list of asarot
#  5   2   1    1  8   9
print('    ', [54, 20, 12, 13, 83, 99])
print('map6', list(map(lambda x: (x // 10) % 10,  [54, 20, 12, 13, 83, 99])))

# ** Bonus: zugi e-zugi
#    [54, 20, 12, 133, 83, 9989]
#    "even", "even", "even", "odd" ...
print('    ', [54, 20, 12, 133, 83, 9989])
print('map7', list(map(lambda x: "even" if x % 2 == 0 else "odd",  [54, 20, 12, 133, 83, 9989])))

def zugi(x: int) -> str:
    if x % 2 == 0 :
        return "even"
    else:
        return "odd"
    return "even" if x % 2 == 0 else "odd"
    return "even" if x % 2 == 0 else "odd"

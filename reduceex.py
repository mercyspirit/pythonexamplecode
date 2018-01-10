import functools

lst = [34,23,24,24,100,2333,2,11]

print(max(lst))

max_find = lambda a,b: a if(a > b) else b

print(functools.reduce(max_find, lst))
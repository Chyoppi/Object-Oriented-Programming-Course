from functools import reduce

numbers = [1, 2, 3, 4, 5]
words = ["apple", "banana", "cherry", "date"]

map_result = list(map(lambda x: x * 2, numbers))

def map_function(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

map_loop = map_function(lambda x: x * 2, numbers)

filter_result = list(filter(lambda x: x % 2 == 0, numbers))

def filter_function(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result

filter_loop = filter_function(lambda x: x % 2 == 0, numbers)

reduced_result = reduce(lambda x, y: x + y, numbers)

def reduce_function(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for item in it:
        value = func(value, item)
    return value

reduced_loop = reduce_function(lambda x, y: x + y, numbers)

sorted_result = sorted(words, key=lambda x: len(x))

def sorted_function(iterable, key=None, reverse=False):
    result = list(iterable)
    for i in range(len(result)):
        for j in range(len(result) - i - 1):
            if (key(result[j]) if key else result[j]) > (key(result[j + 1]) if key else result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
    if reverse:
        result.reverse()
    return result

sort_loop = sorted_function(words, key=lambda x: len(x))

enumerated_result = list(enumerate(words, start=0))

def enumerate_function(iterable, start=0):
    index = start
    result = []
    for item in iterable:
        result.append((index, item))
        index += 1
    return result

enumerated_loop = enumerate_function(words)

# Tests
print("Testing map:")
print("Lambda:", map_result)
print("Loop:", map_loop)

print("\nTesting filter:")
print("Lambda:", filter_result)
print("Loop:", filter_loop)

print("\nTesting reduce:")
print("Lambda:", reduced_result)
print("Loop:", reduced_loop)

print("\nTesting sorted:")
print("Lambda:", sorted_result)
print("Loop:", sort_loop)

print("\nTesting enumerate:")
print("Lambda:", enumerated_result)
print("Loop:", enumerated_loop)
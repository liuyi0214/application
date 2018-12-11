import collections
# a = [1, 2, 3, 2, 1, 5, 7, 5, 6, 3]
# b = [1, 2, 3, 0, 1, 5, 7, 5, 6, 3]
# c = [1, 2, 3, 2, 0, 5, 7, 5, 3, 3]
# print([item for item, count in collections.Counter(a+b+c).items() if count > 1])
a = "12345678"
b = "23456789"
print([item for item, count in collections.Counter(list(a+b)).items() if count > 1])
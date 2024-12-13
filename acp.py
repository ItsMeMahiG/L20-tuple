def tuple(tuple_nums):
    product = 1
    for num in tuple_nums :
        product *= num
    return product

tup = (2, 3, 4, 5)
result = tuple(tup)
print(result)
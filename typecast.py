#Program for typecasting

#typecast tuple to list

tup = (1,2,3,4,5,6)
print("tuple: ", tup)
tup = list(tup)
print("list: ", tup)

#typecast list to tuple

li = [1,2,3,4,5,6]
print("list: ", li)
li = tuple(li)
print("tuple: ", li)

#to change value of tuple using list

tup = (1,2,3,4,5,6)
tup = list(tup)
tup[1] = 7
tup = tuple(tup)
print("After changing the value: tuple: ", tup)

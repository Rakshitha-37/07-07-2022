#program to illustrate slicing

str = "thundersoft"
print("String is: ", str)
new = str[0:4]
print("After slicing: {0}".format(new))

li = [1, 2, 3, 4, 5, 6]
print("List is: ", li)
new = li[4:]
print("After slicing: {0}".format(new))

tup = (1,2,3,4,5,6)
print("Tuple: ", tup)
new = tup[:4]
print("After slicing: {0}".format(new))

#to reverse string using slicing

str = "thundersoft"
print("String is: ", str)
new = str[::-1]
print("After reversing: {0}".format(new))

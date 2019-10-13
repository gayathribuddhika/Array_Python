from array import  *

numbers = array("i", [5, 8, -3, 4, 6])  # cannot use float numbers
print(numbers)

numbers = array("I", [5, 8, 3, 4, 6])  # cannot use negative and float numbers
print(numbers)

numbers = array("i", [5, 8, -3, 4, 6])
print(numbers.buffer_info())  # In this code's output gives the address and number of elements that array has
                                # (address, num of elements)

numbers = array("i", [5, 8, -3, 4, 6])  # gives the type of the elements
print(numbers.typecode)

numbers = array("i", [5, 8, -3, 4, 6])
print(numbers[2])

print()

numbers = array("i", [5, 8, -3, 4, 6])
for i in range(5):
    print(numbers[i], end=" ")
    # print(numbers[i])

print()

numbers = array("i", [5, 8, -3, 4, 6])
for i in range(len(numbers)):
    print(numbers[i], end=" ")

print()

numbers = array("u", ["a", "e", "i"])
for x in numbers:
    print(x)

numbers = array("i", [5, 8, 3, 4, 6])
newArray = array(numbers.typecode, (y*y for y in numbers))

i = 0
while i < len(newArray):
    print(newArray[i])
    i += 1



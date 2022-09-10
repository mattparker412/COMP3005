print("1 --------------------------------")
x = (5 + 3 / 5 * (4 - 10))
print(x)
print(type(x))

y = 17 // 3 ** 4
print(y)
print(type(y))

print("2 --------------------------------")
print(15 % 4 < 20 / 3)
print(False or not (False or True) and True)
print(3/4 == 0 or 5 < 6)

a = True
b = True
c = False

print("3 --------------------------------")
print(a and not b)
print(b or c)
print(not b == c)
print(a and not c)
print(b or c and not a)
print(a != b or b!= c)

print("5 --------------------------------")
lenSquare = 5
perimeterSquare = lenSquare * 4
areaSquare = lenSquare ** 2
print("Side length = " + str(lenSquare))
print("Perimeter = " + str(perimeterSquare) + " Area = " + str(areaSquare))

print("6 --------------------------------")
numSeconds = 4503
numHours = numSeconds // 3600
numMinutes = numSeconds % 3600 // 60
numSecondsFinal = numSeconds % 3600 % 60
print("Total seconds: " + str(numSeconds))
print("Hours: " + str(numHours) + " Minutes: " + str(numMinutes) + " Seconds: " + str(numSecondsFinal))
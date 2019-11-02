#        Variables
# x = 5
# y = "Hello"
# print(x)
# print(y)

#       Functions
def add(x, y):
    return x + y


print(add(3, 4))

#       If Else

x = 18
if x < 18:
    print("You are under 18")
elif x > 18:
    print("You are more than 18 years old ")
else:
    print("You are 18!")

#       While Loop
p = 0
while p < 10:
    print(p)
    p += 1

#       For Loop
for i in range(5):
    print("Number is:", i)

l = [1, 2, 5, 4, 7]
for i in l:
    print(i)

#       Dictionaries
d = {
    1: "One",
    2: "two"
}
print("For key 1, value is:", d[1])
print(d.items())  # output all keys and values..
for k, v in d.items():
    print(k, v)
print(tuple(d.items()))  # casting .. but its now immutable
print(list(d.keys()))

#       Zip feature
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 0]
merged = list(zip(a, b))
print(merged)

field = ["id", "name", "Location"]
values = ["6113", "Ahmad", "Peshawar"]
record = dict(zip(field, values))
print(record)

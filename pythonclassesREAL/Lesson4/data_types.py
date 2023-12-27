# String data type
import math
#Literal Assignment
first = "Aarav"
last = "Menon"
# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Pizza = str("Pepperoni")
# print(type(Pizza))
# print(type(Pizza) == str)
# print(isinstance(Pizza, str))

# Fullname = first + " " + last
# Fullname += "!"
# print(Fullname)

# decade = str(1980)
# print(type(decade))
# print(decade)

# Statement = "I like rock music from the " + decade + "'s."
# print(Statement)

multiline = '''
Hello, How are you?

Yeah, I'm good.
'''
print(multiline)

print(first)
print(first.lower())
print(first.upper())

print(multiline.title())
print(multiline.replace("good", "Ok"))

print(len(multiline))
multiline += "                              "
multiline = "              " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

gpa = 3.28
y = float(1.14)
print(type(gpa))

comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))


print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))
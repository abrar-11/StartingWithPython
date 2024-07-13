print("Ezzy Pzzy Lemon Squzyy.")

# ===String Data type===

# Literal Assignment
firstName = "Bruce"
lastName = "Wayne"

print(type(firstName))
print(type(firstName) == str)
print(isinstance(firstName, str))


# constructor function
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))


# Concatenation
fullName = firstName + " " + lastName


# Casting a number to a string

decade = str(1980)
print((type(decade)))
print(decade)


statement = "Heyy! I am " + fullName + " from Gotham"
print(statement)

# Multiple Lines
multiline = """
Heyy! how are you?

I was just checking .
                Is everythingg alright!?
"""

# == Esacaping Special Characters == 
sentence = "I'm a Full Stack Developer!\n\n Heyyy!"


# ==  String Methods == 
print(firstName.lower())
print(firstName.lower())

print("--multiline.title--")
print(multiline.title())
print("--multiline.replace alright with ok--")
print(multiline.replace("alright", "ok"))
print("--Length")
print(multiline.len())

print("Remove whitespace")
print(multiline.strip())
print(multiline.ltrip())  #Left spaces
print(multiline.rtrip())  #Right spaces


# == string index values == 
print(firstName[1])
# Last Value
print(firstName[-1])
# Last Value
print(firstName[1:-1])
print(firstName[1:])

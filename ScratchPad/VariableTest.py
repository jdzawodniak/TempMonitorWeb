


shepherd = "Mary"
age = 32
stuff_in_string = "Shepherd {} is {} years old.".format(shepherd, age)
print(stuff_in_string)

shepherd = "Martha"
age = 34
# Note f before first quote of string
stuff_in_string = "Shepherd %s is %d years old." % (shepherd, age)
print(stuff_in_string)
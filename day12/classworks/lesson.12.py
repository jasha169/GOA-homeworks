# not
# not True -> False
# not False -> True

# or
# True or True -> True
# True or False -> True
# False or True -> True
# False or False -> False

# and
# True and True -> True
# True and False -> False
# False and True -> False
# False and False -> False

# ყველა კომბინაცია:
a = True
b = False

print("not a:", not a)  # not True -> False
print("not b:", not b)  # not False -> True

print("a or a:", a or a)  # True or True -> True
print("a or b:", a or b)  # True or False -> True
print("b or a:", b or a)  # False or True -> True
print("b or b:", b or b)  # False or False -> False

print("a and a:", a and a)  # True and True -> True
print("a and b:", a and b)  # True and False -> False
print("b and a:", b and a)  # False and True -> False
print("b and b:", b and b)  # False and False -> False

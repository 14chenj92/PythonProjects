# def stay_at_home(school_day, holiday):
#     if not school_day or holiday:
#         return True
#     else:
#         return False

# # Examples:
# print(stay_at_home(False, False))  # True
# print(stay_at_home(True, False))   # False
# print(stay_at_home(False, True))   # True

# Given two integers, a and b, return True if either a or b is 10, or if their sum is 10.

def makes10(a, b):
    if (a == 10 or b == 10) or (a + b == 10):
        return True
    else:
        return False

print(makes10(9, 10))  # True
print(makes10(9, 9))   # False
print(makes10(1, 9))   # True


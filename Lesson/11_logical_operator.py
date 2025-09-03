# Logical operators = evaluate multiple conditions (or, and, not)
# or = at least one condition must be True 
# and = both conditions must be True
# not = inverts the condition (not False, not True)


# temp = 20
# is_raining = False

# if temp > 35 or temp < 0 or is_raining: # or is_raining mean is_raining = True
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")




temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is cold outside")
    print("It is Sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside")
    print("It is Sunny")
elif temp >= 28 and not is_sunny:
    print("It is hot outside")
    print("It is CLOUDY")
elif temp <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is CLOUDY")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside")
    print("It is CLOUDY")




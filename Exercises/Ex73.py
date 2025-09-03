def average_point(Math, Literature, English = 7):
    return (Math + Literature + English) / 3

Math = float(input())
Literature = float(input())
English_input = input()

if English_input:
    English = float(English_input)
else:
    English = 7

print(average_point(Math, Literature, English))

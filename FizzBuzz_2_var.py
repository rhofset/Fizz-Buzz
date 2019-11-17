"""
Fizz Buzz with two different input values and check if the end value is larger than the start value
"""

start = input("Input your start value")
end = input("input your end value")

if int(end) <= int(start):
    print("You need to have a higher end value than your start value. Your start value is {}.".format(start))
    end = input("input your end value")

for x in range(int(start),(int(end)) + 1):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)
# 1 - 100, if multiple of 3 and 5 print FizzBuzz, if multiple of 5 print Buzz and if multiple of 3 print Fizz
for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)


n = int(input('Введите число'))


def fizz_buzz(n):
    for result in range(1, n + 1):
        if result % 3 == 0:
            print('Fizz')
        elif result % 5 == 0:
            print('Buzz')
        elif result % 3 == 0 and result % 5 == 0:
            print('FizzBuzz')
        else:
            print(result)


fizz_buzz(n)

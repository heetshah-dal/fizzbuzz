def fizzBuzz(n=100):
    for i in range(1, n+1):
        if i%3 == 0:
            print('Fizz',end='')
        if i%5 == 0:
            print('Buzz',end='')
        print('')
fizzBuzz()
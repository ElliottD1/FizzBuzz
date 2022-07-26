def fizzbuzz(number,max):
    while number<=max:
        if number %3==0:
            print('Fizz')
            number += 1
        elif number %7==0:
            print('buzz')
            number += 1
        else:
            print(number)
            number += 1



number=int(input('What is your starting number: '))
max=int(input('what do you want to go to?'))

fizzbuzz(number,max)


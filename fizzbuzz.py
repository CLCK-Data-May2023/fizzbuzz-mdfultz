# add your code here

x=1

while x <= 100:
    if x % 3 == 0:
        if x % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    else:
        print (x)
    x +=1

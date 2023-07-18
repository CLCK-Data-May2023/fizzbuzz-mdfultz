# add your code here

x=1

while x <= 100:
    if x % 5 == 0:
        if x % 3 == 0:
            print('FizzBuzz')
        else:
            print('Buzz')
    elif x % 3 ==0:
        print('Fizz')
    
    else:
        print (x)
    x +=1

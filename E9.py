#EX 045
t = 0
while t <= 50:
            a= int(input ('add number: '))
            t = t + a 
            j= str (t)
            print ('the total is' + j)
else:
    print('the total is more than the 50')




#EX 046
n=0
while n<=5:
    n=int(input('Enter a number:'))
print('The last number you entered was a ' + n)





#EX 047
a = int(input('add a number:'))
b = int(input('add another number:'))
v = a + b
c = input('do you want to add another number?')
while c == 'yes' or c == 'Yes' or c == 'YES':
    d = int(input('add another number:'))
    t = v + d
    c = input('do you want to add another number?')
else:
    print(t)




#EX 048
a = input('enter your guest name:')
print(a + ' ' + 'has now been invited')
number_g = 1
b = input('do you want to invite sb else?')
while b == 'yes' or b == 'Yes' or b == 'YES':
      c = input('enter your guest name:')
      number_g = number_g + 1
      print(c + 'has now been invited')
      b = input('do you want to invite sb else?')
else:
    print(number_g)




#EX 049
compnum = 50
guess = 0
score = 0
while compnum != guess :
    guess = int(input('add a number:'))
    score = score + 1
    if guess < compnum :
        print('too low')
    elif guess > compnum :
        print('too high')
print('welldone,your score is',score)




#EX 050
a = int(input('enter a number between 10 to 20'))
while a < 10:
    print('too low')
    a = int(input('enter a number between 10 to 20'))
while a > 20:
    print('too high')
    a = int(input('enter a number between 10 to 20')) 
else:
    print('thank you')





#EX 051
num = 10
while num > 0:
    print('there are',num,'green bottles hanging on the wall,if 1 green bottle should accidently fall')
    a = int(input('how many bottles will be hanging on the wall?'))
    num -= 1
    while num != a:
        print('no,try again')
        a = int(input('how many bottles will be hanging on the wall?'))
    if num == a:
        print('there will be',num,'bottles hangin on the wall')
print('there are no more bottles on the wall')

    
    
    


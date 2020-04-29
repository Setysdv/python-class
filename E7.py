num1 = int(input('yek adad vared konid:'))
num2 = int(input('yek adade digar vared konid:'))
if num1>num2:
    print([num1,num2])
else:
    print([num2,num1])



num = int(input('yek adad zire 20 vared konid:'))
if num >= 20:
    print('Too high')
else:
    print('Thank you')
    


num = int(input('yek adad beyne 10 ta 20 vared konid:'))
if 10<num<20:
    print("thank you")
else:
    print("incorrect answer")



num = input('range delkhahe khod ra benevisid:')
if num == 'red' or num == 'Red' or num == 'RED':
    print('I like red too')
else:
    print('I dont like',num,',','I prefer red')



num = input('is it raining?')
num = num.lower()
if num == 'yes':
    num2 = input('is it windy?')
    num2 = num2.lower()
    if num2 == 'yes':
        print('it is too windy for an umbrellas')
    else:
        print('take an umbrella')
else:
    print('enjoy your day')



num = int(input('how old are you?'))
if num >= 18:
    print('you can vote')
elif num == 17:
    print('you can learn to drive')
elif num == 16:
    print('you can buy a lottery ticket')
elif num < 16:
    print('you can go trick or treating')



num = int(input('enter a number:'))
if num < 10:
    print('too low')
elif 10 <= num <= 20:
    print('correct')
elif num > 20:
    print('too high')



num = int(input('yek adad beyne 1,2,3 vared konid:'))
if num == 1:
    print('thank you')
elif num == 2:
    print('well done')
elif num == 3:
    print('correct')
elif num != 1 and num != 2 and num != 3:
    print('error message')

    
    

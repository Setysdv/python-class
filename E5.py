def julian_date(y,m,d):
   days = [31,28,31,30,31,30,31,31,31,30,31,30]
   days_passed = 0
   if y%400 == 0 or (y%4 == 0 and y%100 != 0):
      days[1] = 29
   for months in days[:m-1]:
      days_passed += months
   days_passed += d
   return (days_passed)




def pos(num):
   for i in range(num):
      print(i)




def dev(num1,num2):
   if num1%num2 == 0 or num2%num1 == 0:
     print('bakhshpazir')
   else:
      print('gheyre bakhshpazir')





def prime(num):
   jazr = int(num ** 0.5)
   for i in range(jazr):
      if num % i == 0:
         return 'aval nist'
   return 'aval ast'
      
 
    


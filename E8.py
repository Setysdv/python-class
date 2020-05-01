#E.8 069 070
t1 = ('iran','india','america','germany','brazil')
print(t1)
num = input('yeki az keshvarhaye t1 ra benevisid:')
print(t1.index(num))
num1 = int(input('yek adad vared koni az 0 ta 4:'))
print(t1[num1])


#E.8 071
l1 = ['basketball','Trx']
num1 = input('enter your favourite sport:')
l1.append(num1)
l1.sort()
print(l1)


#E.8 072
l2 = ['evolution','biology','histology','physiology','biophysic','immunology']
print(l2)
a = input('which subject dont you like?')
l2.remove(a)
print(l2)


#E.8 073
x,y,z,w = [x for x in input('enter your 4 favourite foods').split()]
dic = {1:x,2:y,3:z,4:w}
print(dic)
a = int(input('which number do you want to get rid of?'))
dic.pop(a)
print(dic)


#E.8 074
l3 = ['abi','ghermez','sabz','zard','siah','sefid','surati','banafsh','yashmi','yasi']
print(l3)
s = int(input('yek adad baraye shoro az 0 ta 4 entekhab konid:'))
e =int(input('yek adad baraye payan az 5 ta 9 entekhab konid:'))
print(l3[s+1:e])


#E.8 075
l4 = [123,245,550,960]
print(l4[0])
print(l4[1])
print(l4[2])
print(l4[3])
t = int(input('yek adade 3 raghami vared konid:'))
if t in l4:
    print(l4.index(t))
else:
    print('dar list nist')



#E.8 076
l,m,n = [l for l in input('3 nafar az kasani k mikhahid davat konid benevisid:').split()]
l5 = [l,m,n]
print(l5)
c = input('kase dgar ham mikhahid davat konid?')
while c == 'bale':
    d = input('esmash ra benevisid:')
    l5.append(d)
    print(l5)
    c =input('kase dgar ham mikhahid davat konid?') 
if c == 'na':
    g = int(input('chan nafar davat kardid?'))

#E.8 077
l,m,n = [l for l in input('3 nafar az kasani k mikhahid davat konid benevisid:').split()]
l5 = [l,m,n]
print(l5)
c = input('kase dgar ham mikhahid davat konid?')
while c == 'bale':
    d = input('esmash ra benevisid:')
    l5.append(d)
    print(l5)
    c =input('kase dgar ham mikhahid davat konid?') 
if c == 'na':
    print(l5)
    h = input('esme yeki az afrade list ra benevisid?')
    print(l5.index(h))
    k = input('aya mikhahid hanuz davatash konid?')
    if k == 'na':
        l5.remove(h)
    print(l5)



    
#.8 078    
l7 = ['navad','dorehami','manotoplus','kodakshow']
print(l7[0])
print(l7[1])
print(l7[2])
print(l7[3])
u = input('yek barnameye dg begoyid?')
g = int(input('index ham begoid?'))
l7.insert(g,u)
print(l7)


#.8 079
nums = []
while len(nums) == 0 or len(nums) == 1 or len(nums) == 2 or len(nums) == 3:
   f = int(input('enter a number:'))
   nums.append(f)
   print(nums)
else:
   h = input('aya mikhahid dar list bemanad?')
if h == 'na':
    u = nums[3]
    nums.remove(u)
print(nums)


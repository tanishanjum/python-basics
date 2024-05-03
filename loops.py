w=int(input("weight of watermelon"))
if(w%2!=0 or w==2):
    print("no")
else:
    x=w/2
    if(x%2==0):
        print("x1=",x, "and" "x2=",x)
    else:
        print("x1=",x-1, "and" "x2=",x+1)

n=int(input('enter the value of nor'))
value=n*(n+1)/2
print(value)

n=int(input('enter the nor'))
sum=0
for i in range (1,n+1):
    sum += i
print('sum of first',n,'natural numbers:',sum)

n=int(input('enter the number'))
fact=1
for i in range (1,n+1):
    fact*=i
print('factorial of',n,'is',fact)

n=int(input('enter the number:'))
a,b=0,1
for _ in range(n):
    print(a,end=" ")
    temp_a=a
    a=b
    b=temp_a+b

num=int(input('enter the number'))
rev=0
while num >0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print('reversed number',rev)

num=int(input('enter the number'))
count=0
while num!=0:
    num//=10
    count+=1
print('number of digits',count)

num=int(input('enter the no'))
print('multiplication table of',num)
for i in range (1,11):
    print(num,"x",i,"=",num*i)

password='sameer'
for i in range(3):
    attempt=input('enter the password')
    if (attempt==password):
        print("login successful.!")
        break
    else:
        print("incorrect password.Please try again.")
else:
    print("too many incorrect attempts account locked")

password='sajid'
attempts=3
while attempts >0:
    user_input=input('enter he password:')
    if user_input==password:
        print('Welcome')
        break
    else:
        attempts-=1
        if attempts >0:
            print('wrong password! You have {attempts} attempts left')
        else:
            print('account is blocked')
            break

#remove duplicates from list
a=[10,20,30,50,60,70,80,90,100,60,80,70,20,30]
dup_items=set()
uniq_items=[]
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)
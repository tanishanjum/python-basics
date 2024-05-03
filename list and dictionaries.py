fruits=['kiwi','orange','apple']
print(fruits)
fruits.append('pineapple')
print(fruits)

fruit={'apple':'red','pineapple':'yellow','watermelon':'red'}
print(fruit)
fruit.update({'kiwi':'blue'})
print(fruit)

fruits=['apple','cherry','kiwi','mango','orange','pineapple','guava']
for x in fruits:
    if (x=="guava"):
        print("the fruit is present")
    else:
        print("the fruit is not present")

user_list=[int(i) for i in (input("enter the elements")).split()]
print("user list:",user_list)

l=[2,3,4,5,6,7,8,9,98,76,65,43,21]
max=0
for i in l:
    if (i>max):
        max=i
print(max)

l=[1,2,3,4,5,6,7,8,9,98,76,65,43,21]
min=10
for i in l:
    if (i<min):
        min=i
print(min)

a=(10,'hello',True)
print(a)
a.append[0:20]
print(a)
"no we cannot change or append the tuple,hence it is a immutable datatype"

x=input('enter the name or roll number:')
a={'name':'abdul','roll_num':'44','marks':'100','result':'pass'}
b={'name':'sami','roll_num':'42','marks':'100','result':'pass'}
c={'name':'shafi','roll_num':'47','marks':'99','result':'pass'}
d={'name':'shiraj','roll_num':'43','marks':'99.9','result':'pass'}
def student_details(x):
        if x=='abdul' or x=='44':
            print(a)
        elif x=='sami' or x=='42':
            print(b)
        elif x=='shafi' or x=='47':
            print(c)
        elif x=='shiraj' or x=='43':
            print(d)
        else:
            print('name not found')
student_details(x)
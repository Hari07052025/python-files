#if condition:if condition is ture then only it go to next statement 
'''age = 35
if age >= 20 :
    print("you are eligible to vote")
print("you are not eligible to vote")'''

'''k =25
if k <= 6:
   k1 = 10
   k2 = 20
   result=k1*k2
   print(result)
print('this is not valid statement')'''

#else helps to execute alternative block of code if statement is false, in else should not write any condition

'''stock_price = 1000
if stock_price < 980 :
    print(f"purchase the stock for {stock_price}")
else :
    print(f"dont purchase stock above {stock_price}")'''

#elif: it helps to execute multiple condition one after another

'''stock = int(input("stock price:"))
if stock >100 :
    print("put stock in rack A")
elif stock <100 and stock > 90:
    print("put stock in rack b")'''

#nested statement:if condition has one more if or else condithition then it is called as nested condition.inside statement can
#write either if,elif,else

'''username = input('username:')
password = int(input('enter the password:'))
if username == "hari": 
    if password == 17890:
        print("authencical sucessfule")
    else: 
        print("wrong password")
else:
    print("wrong usename")'''

#task:
#2nd method
'''English_letter = input("provide the input:")
if English_letter in ('aeiou'):
    print("itis volwel letter")
else:
    print("it is not vowel")'''
#first method
'''english_words = input("print the letter")
if english_words == 'u':
    print('it is a vowel letter')
elif english_words == 'i':
    print('it is a vowel')
else:
    print('it is not vowel')'''

'''age = int(input("enter your age:"))
if age > 100:
    print("he is a elder person")
elif age >90 and age <100 :
    print("he is a senior citizen")
else:
    print("they are not eligible for petnsion")'''
#for division use the %
'''year = int(input("provide the year:"))
if (year%4 ==0  or year%400==0):
    print("it is leap year")
else:
    print("it is not leap year")'''

'''num2 = int(input("provide number:"))
num3 = int(input("provide the number:"))
result = input("provide the artihime symbol:")
if result == "+":
    print(num2+num3)
elif result == "-":
    print(num2-num3)'''

weight = int(input("provide the weight:"))
height = int(input("provide the height:"))
BMI = weight%height**2
print(BMI)
  


 
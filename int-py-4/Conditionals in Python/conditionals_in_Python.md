![Logo](https://user-images.githubusercontent.com/85128689/123909136-3a37f680-d996-11eb-93cb-fd82ef3263b9.jpeg)

## **Conditional statements:**

**What are Conditional statements ?**

In any programming language we need a ability to check given conditions whether it is satisfied or not and allows execution of statements accordingly. Such ability is provided by Conditional statements also known as selection control statements.
- Conditional statements is controlled by boolean expressions in it.
- If the boolean expression is satisified i.e., true then it executes all the statements indented in conditional block.
- If the boolean expression is not satisified i.e., false then it ignores the statements inside the conditional block and jumps to the next line in the code.


**What is the use of conditional statements ?**
- Execute statements selectively based on the condition provided.
- This helps to improve efficiency of code by providing the ability to control of execution of code.

**Python language supports different types of conditional statements which are as follows:**
- if statement
- if - else statement
- Nested if statement
- Chained conditional statements

## 1.**If Statement:**

- if statement is frequently used in conditional statement.

**Syntax of if statement:**<br> 
       &ensp; if (expression):<br>
           &emsp;  statement(s)<br>

- Expression consists of boolean expressions.
- if statement evaluates the boolean expression
    - if the expression returns TRUE, then it evaluates block of indented statement(s) present inside the if statement.
    - if the expression returns FALSE, then it ignores and executes next statements in the code 
- **Points to be remembered**:
    - Colon (':') is must after if statement, otherwise an error will occur.
    - Indentation must be followed after if statement (usually 4 spaces or 1 tab space), otherwise an error will occur.
    - It is not necessary to enclose the expression inside any parentheses().

    
- Let us take a look at the flow chart for better understanding,    


![if](https://user-images.githubusercontent.com/85128689/123909253-5b98e280-d996-11eb-94c1-38782ad3b7f5.jpg)


**Lets us try to work on few examples:**


```python
x = 10 #x is initialised with 10
y = 4 #y is initialised with 4
if x>y: #Boolean Expression  
    print("x is greater than y")
```

    x is greater than y
    


```python
x = 10 #x is initialised with 10
y = 4 #y is initialised with 4
if x>y: #Boolean Expression
print("x is greater than y")#Without indentadtion
```


      File "<ipython-input-6-bff1c9bc8e4f>", line 4
        print("x is greater than y")
        ^
    IndentationError: expected an indented block
    


As indentation is not followed after the if statement an has occured.


```python
if 'PineApple' in ['Mango','Orange','Apple','Kiwi']:
    print("TRUE")
print("FALSE")
```

    False
    

Here, we can observe that the condition pineapple is not in the given list the if block is not executed and executed the next line prints the FALSE.


```python
if x>y
print(x)
```


      File "<ipython-input-11-65734aeaf3c5>", line 1
        if x>y
              ^
    SyntaxError: invalid syntax
    


Here colon(':') is not used so it generated an syntax error.

## 2.**else Statement:**
- else statement is used  for alternative execution.

**Syntax of else statement:**<br> 
       &ensp; if (expression):<br>
           &emsp;  statement(s)<br>
       &ensp; else:<br>
           &emsp;  statement(s)<br>

- Expression consists of boolean expressions.
- if statement evaluates the boolean expression
    - if the expression returns TRUE, then it evaluates block of indented statement(s) present inside the if statement and ignore else block.
    - if the the expression returns FALSE, then it ignores if block and executes else block.

- **Points to be remembered**:
    - Colon (':') is must after if statement and else statement, otherwise an error will occur.
    - Indentation must be followed after if statement (usually 4 spaces or 1 tab space), otherwise an error will occur.
    - It is not necessary to enclose the expression inside any parentheses().

- Let us take a look at the flow chart for better understanding,

![else](https://user-images.githubusercontent.com/85128689/123909321-7408fd00-d996-11eb-9b98-b6f738e832b0.jpg)


**Lets us try to work on few examples:**


```python
x = 9
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')

```

    x is odd
    

As the condition is false it executes the else statement and prints x is odd.


```python
x = 14
y = 4
if x<y:
    print("x is less than y")
else:
    print("x is greater than y")
```

    x is greater than y
    

- Let's take an example from our routine life
Question : Students greater than or equal to 9 CGPA are eligible to interview for an XYZ company and remaining are not eligible.


```python
CGPA = float(input("CGPA: "))
if CGPA >= 9:
    print("Congratulations..!! You are eligible for the interview")
else:
    print("Sorry, you aren't eligible")
```

    CGPA: 8.9
    Sorry, you aren't eligible
    

Here, given input is 8.9 which is less than 9 so it ignored "if block" and executed "else block" as the student CGPA is not matching the companies eligibility criteria so it printed **Sorry, you aren't eligible** 

- Let's take another example.

Question: Mr Dev went to market for buying an pine apple.
if pine apple is available print stock available otherwise out of stock.


```python
if 'PineApple' in ['Mangoes','Oranges','Apples','Kiwis']:
    print("Stock Available")
else:
    print("Out of stock")
```

    Out of stock
    

  As there are only mangoes, oranges,apples,kiwis in market it printed out of stock

## 3. Nested if Statement:
- Nested if statements are used to check whether more than one condition is satisfied.
- Here if statements are placed one inside the other

**Syntax of Nested-if statement:**<br>
&ensp; if (expression):<br>
           &emsp;  statement(s)<br>
           &emsp; if(expression):<br>
                    &emsp;&emsp;    statement(s)<br>

- Expression consists of boolean expressions.
- if statement evaluates the boolean expression
    - if the expression returns TRUE, then it evaluates block of indented statement(s) present inside the if statement and enters to the nested if statements and executes the block indented statements.
    - if the expression returns FALSE, then it ignores if, nexted if blocks and executes next statements in the code

- **Points to be remembered**:
    - Colon (':') is must after if statement and else statement, otherwise an error will occur.
    - Indentation must be followed after if statement (usually 4 spaces or 1 tab space), otherwise an error will occur.
    - It is not necessary to enclose the expression inside any parentheses().

- Let us take a look at the flow chart for better understanding,

![NESTED IF (1)](https://user-images.githubusercontent.com/85128689/123909379-913dcb80-d996-11eb-8bba-06aa5b773fe5.JPG)


**Lets us try to work on few examples:**


```python
a = 4 #intialised a with 4
if (a>0): #Condition
    print("It is Positive number")
    if (a<5):
        print("Number is less than 5")

```

    It is Positive number
    Number is less than 5
    

- Let's take an example from our routine life

Question : Students greater than or equal to 9 CGPA are eligble for aptitude test, scoring 90 will get opportuinity for interview in XYZ company.


```python
CGPA = 9
Aptitude = 95
if CGPA >= 9:
    print("All the best for aptitude, scoring 90 will help you to get opportunity for interview")
    if Aptitude >=90:
        print("\nCongratulations..!! You are eligible for the interview")
```

    All the best for aptitude, scoring 90 will help you to get opportunity for interview
    
    Congratulations..!! You are eligible for the interview
    

## 4. Chained conditional statements:
- Chained conditional statements comes into action when we require more than two possibilities.
- Chanined conditional statements consists of if, elif(short for else if), else.


**Syntax of Chained conditional statement:**<br> 
       &ensp; if (expression):<br>
           &emsp;  statement(s)<br>
       &ensp; elif(expression):<br>
           &emsp;  statement(s)<br>
       &ensp; else:<br>
           &emsp;  statement(s)<br>

- Expression consists of boolean expressions.
- if statement evaluates the boolean expression
    -  If that expression returns to TRUE  then it goes into if block.
    - If it returns to FALSE, then it goes to elif and executes the condition of the elif block.
    - If the condition in the elif bock returns TRUE , then the elif block is executed.
    - If the condition in elif block returns FALSE , then the code in the else block is executed.
    
- **Points to be remembered**:
    - Colon (':') is must after if statement and else statement, otherwise an error will occur.
    - Indentation must be followed after if statement (usually 4 spaces or 1 tab space), otherwise an error will occur.
    - It is not necessary to enclose the expression inside any parentheses().

- Let us take a look at the flow chart for better understanding,

![ifelifelse](https://user-images.githubusercontent.com/85128689/123909433-adda0380-d996-11eb-9f79-9d571155c693.jpg)

**Let us try to work on few examples:**

Question: To check whether given input is divisible by 2 or 3 or nothing.


```python
a = int(input("number: "))
if a%2==0:
    print("given number is divisible by 2")
elif a%3==0:
    print("given number is divisible by 3")
else:
    print("given number is neither divisible by 2 nor 3")
```

    number:2
    given number is divisible by 2
    

- Let us take an example from our routine life,

Question: XYZ University provides concession in fee based on their marks obtained in entrance test. They are as follows:

|Percentage|Concession| 
|-|-|
| 100|100%|
|95 to 99|75%|
|90 to 94|50%|
|80 to 89|25%|
|70 to 79|10%|
|60 to 69|5% |

No concession for students who scored below 60 marks.


```python
a = int(input("Marks:"))
if a>100:
    print("Please enter valid Marks")
elif a==100:
    print("Congratulations...!! you got 100% concession")
elif a in range(95,100):
    print("Congratulations...!! you got 75% concession")
elif a in range(90,95):
    print("Congratulations...!! you got 50% concession")
elif a in range(80,90):
    print("Congratulations...!! you got 25% concession")
elif a in range(70,80):
    print("Congratulations...!! you got 10% concession")
elif a in range(60,70):
    print("Congratulations...!! you got 5% concession")
else:
    print("Sorry...!! you aren\'t eligible for concession")
```

    Marks:60
    Congratulations...!! you got 5% concession
    

**Summary:**
- Conditional statements in python is evaluated using boolean expressions.
- Executes statements selectively based on the condition provided.
- Various types of conditional statements are: if,else,nested-if, if-elif-else
- If a condition is true, the "if" statement executes.
- else statement is executed when "if" statement condition is evaluated as false.
- A nested-if statement is an if statement placed inside another if statement.
- Chained conditional statement is if-elif-else.
- Indentation is white spaces (usually 4 spaces or 1 tab) that indicates the statements belong to same block
- Avoiding colon(":") after if,elif,else will result in syntax error.
- Ignoring indentation in if,elif,else will result in indentation error.



**Now let's try implementing all the an example as summary of conditional statements**

Code a program using conditional statements 
- Take year and month as input
- Find whether entered year is leap year or not
- Find no of days in entered month 



```python
Year = int(input ("Year: " ) )
month = int(input("Month: " ) )
if ((Year % 4 ) == 0 and (Year % 100 ) != 0 or (Year % 400 ) == 0 ):
       print("Leap Year")
       if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
               print("There are 31 days in this month " )
       elif ( month == 4 or month == 6 or month == 9 or month == 11 ):
           print("There are 30 days in this month " )
       elif ( month == 2 ):
           print("There are 29 days in this month " )
       else:
           print("Invalid month ")
elif ( ( Year % 4 ) != 0 or ( Year % 100 ) != 0 or (Year % 400 ) != 0 ):
    print("Non Leap Year " )
    if ( month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 ):
        print("There are 31 days in this month" )
    elif ( month == 4 or month == 6 or month == 9 or month == 11 ):
            print("There are 30 days in this month " )
    elif ( month == 2 ):
            print("There are 28 days in this month ")
    else:
            print("Entered month is not valid" )
else:
       print( " Entered year is not valid" )
```

    Year: 2021
    Month: 6
    Non Leap Year 
    There are 30 days in this month 
    

![Tqq](https://user-images.githubusercontent.com/85128689/123909514-c9dda500-d996-11eb-8808-f2156178daac.jpeg)


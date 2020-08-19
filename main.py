# Enter your code here. Read input from STDIN. Print output to STDOUT

x, k = map(int, input().split())#Takes the input

expression = input()#Takes the input

p = 0#Initializing p

p += x ** int(expression[3])#Adds the first term of the expression

for i in range(1,len(expression)):
    if expression[i-4] == '+' and expression[i-2].isnumeric() and expression[i] == 'x' and expression[i+1] == '*':#Adds the term if it has a coefficient other than 1
        p += int(expression[i - 2]) * x ** int(expression[i+3])
    elif expression[i-4] == '-' and expression[i-2].isnumeric() and expression[i] == 'x' and expression[i+1] == '*':#Subtracts the term if it has a coefficient other than 1
        p -= int(expression[i - 2]) * x ** int(expression[i+3])
    elif expression[i-2] == '+' and expression[i] == 'x' and expression[i+1] == '*':#Adds the term
        p += x ** int(expression[i+3])
    elif expression[i-2] == '-' and expression[i] == 'x' and expression[i+1] == '*':#Subtracts the term
        p -= x ** int(expression[i+3])
    elif expression[i-2] == '+' and expression[i] == 'x' and expression[i+1] != '*':#Adds the term whose power is 1
        p += x
    elif expression[i-2] == '-' and expression[i] == 'x' and expression[i+1] != '*':#Subtracts the term whose power is 1
        p -= x 

if expression[len(expression) - 3] == '+' and expression[len(expression) - 1].isnumeric():#Adds the constant
    p += int(expression[len(expression) - 1])
elif expression[len(expression) - 3] == '-' and expression[len(expression) - 1].isnumeric():#Subtracts the constant
    p -= int(expression[len(expression) - 1])

#Prints the answer
if p == k:
    print("True")
else:
    print("False")

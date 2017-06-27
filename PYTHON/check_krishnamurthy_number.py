import sys
# A Krishnamurthy number is a number whose sum of the factorial of digits is equal to the number itself. For example 145, sum of factorial of each digits:
# 1! + 4! + 5! = 1 + 24 + 120 = 145
# Example
# 1! = 1.
# 2! = 2.
# 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 4! + 0! + 5! + 8! + 5! = 24 + 1 + 120 + 40320 + 120 = 40585.
# There are exactly four such numbers.
def factorial(number):
    factorial = 1
    while number != 0:
        factorial = factorial * number;
        number = number - 1
    return factorial

def isKrishnamurthynumber(number):
    sum = 0
    temp = number
    while temp != 0 :
        sum += factorial(temp%10)
        temp = temp/10
    return (sum == number)

print "Get Space Seperated String"
print "Example:"
print "Input - 145"
print "Output - YES"
print "Input - 1450"
print "Output - NO"
input_string = raw_input("Please enter your string: ")
print "You entered: ", input_string
resultString = isKrishnamurthynumber(int(input_string))
if resultString:
    resultString = "YES"
else:
    resultString = "NO"
print "Output: ",resultString
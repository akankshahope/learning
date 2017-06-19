import sys
def getSecondLargestNumber(numbersList):
    first_number = 0
    second_number = 0
    lengthOfArray = len(numbersList)
    resultResp = ""
    if lengthOfArray <  2:
        resultResp = "Please provide minimum two values"
    else:
        for i in range(lengthOfArray):
            numbersList[i] = int(numbersList[i])
            if numbersList[i] > first_number:
                second_number = first_number
                first_number = numbersList[i]
            elif (numbersList[i] > second_number) and (numbersList[i] <> first_number):
                second_number = numbersList[i]
        resultResp = second_number
    return resultResp

print "Get Second Largest Number"
print "Example:"
print "Input - 12 10 15 5 6 7 14"
print "Output - 14"
input_string = raw_input("Please enter your numbers(single space separated): ")
print "You entered: ", input_string
resultResp = getSecondLargestNumber(input_string.split())
print "Output: Second Largest Number is ",resultResp

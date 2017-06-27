import sys

def getMaximumNumber(currentNumber,result):
    lengthOfCurrentNumber = len(currentNumber)
    lengthOfResult = len(result)
    if(lengthOfCurrentNumber == lengthOfResult):
        i = 0
        while currentNumber[i] == result[i]:
            i = i+1
        if currentNumber[i] < result[i]:
            return result
        else:
            return currentNumber
    if lengthOfCurrentNumber < lengthOfResult:
        return result
    else:
        return currentNumber
    
def getMaximumNumberFromString(stringToProcess):
    tempString = ""
    lengthOfString = len(stringToProcess)
    currentNumber = ""
    result = ""
    for i in range(lengthOfString):
        while i < lengthOfString and stringToProcess[i] == '0':
            i = i+1
        while i < lengthOfString and stringToProcess[i] >= '0' and stringToProcess[i] <= '9':
            currentNumber = currentNumber + stringToProcess[i]
            i = i+1
        if i == lengthOfString:
            break
        if len(currentNumber) > 0:
            i = i-1
        result = getMaximumNumber(currentNumber,result)
        currentNumber = ""
    if len(currentNumber) == 0 and len(result) == 0:
        result = result + '0'
    return getMaximumNumber(currentNumber,result)
    
print "Get AlphaNumeric String"
print "Example:"
print "Input - 100klh564abc365bg"
print "Output - 564"
input_string = raw_input("Please enter your string: ")
print "You entered: ", input_string
resultString = getMaximumNumberFromString(input_string)
print "Output: ",resultString
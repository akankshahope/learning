import sys
def makeStringSpacedOnUpperCase(stringToProcess):
    tempString = ""
    for i in range(len(stringToProcess)):
        if stringToProcess[i] > 'A' and stringToProcess[i] < 'Z':
            if i != 0:
                tempString+=str(' ')
        tempString+=str(stringToProcess[i])
    return tempString

print "Get Space Seperated String"
print "Example:"
print "Input - ThisIsTheTestString"
print "Output - This Is The Test String"
input_string = raw_input("Please enter your string: ")
print "You entered: ", input_string
resultString = makeStringSpacedOnUpperCase(input_string)
print "Output: ",resultString

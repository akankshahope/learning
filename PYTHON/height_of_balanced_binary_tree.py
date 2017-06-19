def getHeightOfBalancedTree(height):
    height = height+1
    tempList = [None]*(height)
    tempList[0] = tempList[1] = 1
    for i in xrange(2,height):
        tempList[i] = (tempList[i-1] * (2 * tempList[i-2] + tempList[i-1]))
    return tempList[height-1]
print "Get height of the balanced binary tree"
print "Example:"
print "Input - 3"
print "Output - 15"
print "Input - 4"
print "Output - 315"
input_string = raw_input("Please enter height of the balanced tree: ")
print "You entered: ", input_string
resultResp = getHeightOfBalancedTree(int(input_string))
print "Output: Height of the balanced tree is ",resultResp
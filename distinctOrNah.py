def testData(data):
    if len(data)==len(set(data)):
        return True
    else:
        return False

print(testData([1,2,3,4]))
print(testData([1, 2, 3, 3,3,5,6]))



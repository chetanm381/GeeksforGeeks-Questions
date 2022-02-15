def match(ps):
    ps=list(ps)
    temp=[]
    for x in ps:
        if x=="{":
            temp.append("{")
        if x=="}":
            try:
                temp.pop()    
            except:
                return False     
    if(len(temp)==0):
        return True
    else:
        return False    


if __name__ == '__main__':
    testCases = ["{{}}", "{{{}}", "{{{{}}}","{{{}{}}}","}{"]
    results = [True, False, False,True,False]
    for i in range(len(testCases)):
        if match(testCases[i]) == results[i]:
            print("Test Succeed ",i)
        else:
            print("Test Failed ", i)
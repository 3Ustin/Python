def overAchievers(str):
    #PARENTH
    countParenth = 0
    countSquig = 0
    countBracket = 0
    #LOOP
    for i in range(0,len(str)):
        #PARENTH
        if str[i] == "(":
            countParenth += 1
        if str[i] == ")":
            countParenth -= 1
        if  countParenth < 0:
            return False
        #SQUIGILLY
        if str[i] == "{":
            countSquig += 1
        if str[i] == "}":
            countSquig -= 1
        if countSquig < 0:
            return False
        #BRACKETS
        if str[i] == "[":
            countBracket += 1
        if str[i] == "]":
            countBracket -= 1
        if countBracket < 0:
            return False
    if countParenth != 0 or countSquig != 0 or countBracket !=0:
        return False
    else:
        return True
print(overAchievers("[](){}"))
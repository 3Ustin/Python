# SOLUTION NUMBER 1
# 
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15
# students[0]["last_name"] = "Bryant"
# sports_directory['soccer'][0] = "Andres"
# z[0]["y"] = 30


# SOLUTION NUMBER 2
# 
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
#def iterateDict(students):
#  for i in range(0, len(students)):
#     for key, value in students[i].items():
#         print(key)
#         print(value)
#iterateDict(students)


# SOLUTION NUMBER 3
#
# someList = [
#     {'a':"A",'b':"B",'c':"C",'d':"D",'e':"E",'f':"F",'g':"G"},
#     {'a':"C",'b':"D",'c':"E",'d':"F",'e':"G",'f':"H",'g':"I"},
#     {'a':"34",'b':"92834",'c':"290",'d':"4409",'e':"287",'f':"298",'g':"0928"},
#     {'a':"1",'b':"2",'c':"3",'d':"4",'e':"5",'f':"6",'g':"7"}
# ]

# def getDict(keyName, someList):
#     for i in range(0, len(someList)):
#         for key, value in someList[i].items():
#             if(key == keyName):
#                 print(value)
# getDict('a',someList)


#SOLUTION NUMBER 4
#
# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# def Info(dojo):
#     arrayValues = []
#     arrayKey = []
#     for key, value in dojo.items():
#         arrayKey.append(key)
#         arrayValues.append(value)
#     print(arrayValues)
#     for x in range(len(arrayKey)):
#         print(arrayKey[x] + " number of items " + str(len(arrayValues[x])))
#         for y in range(len(arrayValues[x])):
#             print(arrayValues[x][y])
#     return arrayValues
# print(Info(dojo))


#SOLUTION NUMBER -~4~- AGAIN
#
# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# def Info(dojo): 
#     for key, value in dojo.items():
#         print(len(value),key) # len(value) == 7     key == locations
#         for i in range(len(value)):
#             print(value[i])
# Info(dojo)
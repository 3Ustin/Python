# print("Please print your first name: ")
# first_name = input()
# first_name = first_name.lower()
# if(first_name == "austin"):
#     print("Hey, " + first_name + "! That's my name!")
# else:
#     print("Hello", first_name)
print("Now remember this is a first name party. /n So make sure you party members don't share a name.")
print("We will now take your first ten for the party:")
listOfNames = []
for x in range(0,10):
    print("Please enter name number",x + 1,":")
    currentName = input()
    listOfNames.append(currentName)
print("It's nice to meet all of you first namers!")
print("Now please give us the second list:")
listOfNames2 = []
for x in range(0,10):
    print("Please enter name number",x + 1,":")
    currentName = input()
    for x in listOfNames:
        while(currentName == x):
            print(x)
            print("Oh I'm sorry we'll have to give you a nickname!/nSomeone already has your name!")
            currentName = input()
    listOfNames2.append(currentName)
print("Enjoy the party!!")


#COMMENTS CORRISPOND TO THE FOLLOWING LINE!

#Variable int declaration, intilized as 42.
num1 = 42 
#Variable decimal declaration, initilized as 2.3
num2 = 2.3 
#variable boolean declaration, initilized as true.
boolean = True 
# Variable String declaration, initilized as Hello World. Also known as a String Object.
string = 'Hello World' 

# Variable Array declaration, initilized as ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'], Also known as an Array object.
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 
# Variable Object (this might also be called a dictionary - type value object.) declaration, initilized as {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}. Not an instant of a class, and can't be made into an instance with this syntax.
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#I think this is a list.
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))
#Printing the second index of pizza_toppings array.
print(pizza_toppings[1])
#Adding Mushrooms to the pizza_toppings array.
pizza_toppings.append('Mushrooms')
#print value of type 'name' of person object.
print(person['name'])
#change value of type 'name' to 'George'
person['name'] = 'George'
#change person's type 'eye_color' to value blue.
person['eye_color'] = 'blue'
#print third item in list. 
print(fruit[2])

#if statement asking a true or false question: is num1 greater than 45?
if num1 > 45:
    #if above statement was true print to console: "it's greater"
    print("It's greater")
#code after the : in the else only runs if the above if statement was false.
else:
    #print to console its lower.
    print("It's lower")

#Similiar to above if statement though I'm concerned about errors here.
# len() is not defined.
if len(string) < 5:
    #if above statement is true print it's a short word!
    print("It's a short word!")
#This isn't an error, Sorry, this is an else-if statement.
#which means that this code with ask a boolean expression if the previous statement was false.
elif len(string) > 15:
    #if the above statement was given a chance to run this would print: "it's a long word!"
    print("It's a long word!")
#This is an else statement.
else:
    #print statement.
    print("Just right!")

#this is a for loop whose iterative value = x starting at 0 and incrementing 1 each iteration. 
#The range I think would be the boolean expression, is x less than 5.
for x in range(5):
    #would print x through each itteration of loop.
    print(x)
#Another for loop this time the range is different. Starting at 2 and going to 5.
for x in range(2,5):
    #prints x for each itteration.
    print(x)
#I really like this syntax.
#The for loop here goes from 2 => 10 with each itteration ='ing 3.
for x in range(2,10,3):
    #prints x each itteration.
    print(x)
#My best guess is that this isn't in the above for loop. But an instatiation for the former while loop.
x = 0
#while x is less than 5 do the following code.
while(x < 5):
    #print x.
    print(x)
    #x would be incrememnted by 1
    x += 1

#delete an element from the end of an array.
pizza_toppings.pop()
#delete an element from the second index from the right.
pizza_toppings.pop(1)

#prints to console the person object.
print(person)
#If the dictionary object in the reference has a method called pop 
#   that takes in a paramater and matches it with one of its own elements...
#   Then this'll delete the eye_color type to the type value object.
person.pop('eye_color')
#prints to the consoel the person object.
print(person)

#loops through the array, and stores the current index as topping.
for topping in pizza_toppings:
    #compares the currently stored index with a value.
    if topping == 'Pepperoni':
        #stored index is equivilent to value so continue... which means
        #just to go on with the code normally.
        continue
    #print "after 1st if statement"
    print('After 1st if statement')
    #compare current stored index with value.
    if topping == 'Olives':
        #if they are equivilent then leave for loop? 
        #   or just leave the if statement?
        #   not sure on this one here.
        break

# define a function called "print_hello_ten_times"
def print_hello_ten_times():
    #runs a for loop 10 times
    for num in range(10):
        #prints hello ten times.
        print('Hello')

#call defined function above.
print_hello_ten_times()

#define a function called "print_hello_x_times" taking in a pramater of x.
def print_hello_x_times(x):
    #run a for loop x number of times, and starting at num not x.
    for num in range(x):
        #print to console hello.
        print('Hello')

#call defined function above passing through the number four.
print_hello_x_times(4)

#define a function that takes a parameter x, when it is empty it makes x = 10;
def print_hello_x_or_ten_times(x = 10):
    #loops, starting at num, for x or 10 amount of times.
    for num in range(x):
        #print hello world.
        print('Hello')
#calls print_hello_x_or_ten_times
#calls print_hello_x_or_ten_times with the parameter of 4.
print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)



"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
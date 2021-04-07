#1 The total return will be 5.
def number_of_food_groups():
    return 5
print(number_of_food_groups())

#2 The total return will be an error.
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

#3 total return will be 5
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

#4 total return will be 5
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

#5 total return will be 5, print undefined.
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

#6  3, then 5, then enter space.
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

#7 25 -- best code i've seen so far.
# I keep looking at it trying to see if they missspelled their call.
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

#8 100, 10
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

#9 7, 14, 21
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

#10 8
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

#11 500, 500, 300, 500
# Tricky tricky! 
# Scope is a good conversation about this one!
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

#12 500, 500, error, i think if not then, 300, 500, but it think it should be error. 
#syntactically anyway in js I'm pretty confidant.
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

#13 500, 500, 300,300
#Hey you fixed my so call error! Well done!

b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

#14 1,3,2
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


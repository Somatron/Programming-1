"""
Printing special characters

print('I can't') doesnt work because we completed an apostrophe and added an extra apostrophe.


Printing special characters

    - Python (and many other languages) has an escape character.
    -it's just backslash, \ 

    - this character in combination with other characters can be used to print some special characters

    \n = new line

"""
#code 
print('They said "hi"')

# instead of this.  print('"They said "I can't"')
print("They said \"I can't\"")     #adding 2 back slashes onto a quote with double quotes and single quotes makes it into one \ \ 
print('They said "I can\'t"')      #adding a back slash onto a quote with single quotes makes it into one \
# double quotes have 2 back slashes
#single quotes have 1 back slash
print("This is a backslash \\")   #adding 2 back slashes onto a back slash makes it into one
print("See below: \nhi!!   Xp >:DDD")
print("See below: \thi!!   Xp :DDD")  #\t = tab space

print("//n") #in case you ever wanted to print /n for some reason



#variables
"""
Variables

    - In python, a variable is just a name that refers to a piece of data.
    - The data. All data, has a type.

    So far the TYPES we've seen are:
    
    NUMERIC
        1) int: integers, (whole numbers) 2.40 tacos
        2) float: floating point values, numbers with information passed into decimal 

    STRINGS
        3) str: strings of characters, "hello", "5", "catfood"    

        Side quest: type(Value)
        type(value) returns the type


        PEMDAS
        P ()
        E **
        M *
        D /
        A +
        S -
        
        2 special operators
        % 
        //

        The % operator: Mod AKA Modulo. Aka Remainder you get when you divide a number.

        a % b = result in value between 0 and b - 1 
        assumes both values are positive

        The // operator: Floor Division
        - Given a//b you will get an integer that is the result of "flooring" the division down to the next lowest int
"""

type(3)       #int
type(3.14549)     #float
type("catfood")    #str (string of characters)  "5" is a string too
print(7 % 4)
print(7 // 6)
print(-5 // 2) # -3 because -2.5 is floored down to -3

"""

String Operations

    + concatenation
    str + str combines 2 strings into one string
    'abc' + 'def' = 'abcdef'

    * string repeater heh...

    str * int repeats the string int times (or vice versa order doesnt matter)
    repeats the string int number of time   

"""

print('ho' * 3)  #hohoho
print('meow ' * 37)  #arf

#VARIABLES 
"""
Creating variable

Obtaining user input
    Templates:
variable_name = input()'Prompt for the user')                most basic form of this

"""

stealing_a_user_name = input('What is your name?: ') 
user_age = input("What is your age?: ")

print(stealing_a_user_name)
print(user_age)           #ALL INPUT IS STORED AS A STRING??????????????????????????????????????????
#added comma instead of plus to add space
print('In 10 years I will be', user_age + 10, 'years old')
#TYPEERROR: data has types, str, int, float

#HOW WILL WE INPUT NUMBERS WITHIN THE STRINGS
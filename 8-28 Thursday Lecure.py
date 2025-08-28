"""
Casting between tpyes

- Python has built-in functions to convert from one type to another
- The built-in functions are just type names

    int(value)      float(value)        str(value)

'5' + 3           instead of this
int('5') + 3      we do this 

Obtaining numeric input

    Templates:
        variable = int(input('What is your age'))     storing it
input just converts anything into a string. to get a proper number we put int or float 

variable = float(input('prompt'))
"""

int('5')+3

float('3.14')+4
#float('rootbeer') #not a number

user_age = float(input("What is your age? : "))
print('In 10 years I will be', user_age + 10, 'years old')
#Can not add string by number

"""
user_age2 = input("your age? ")
print('I am', user_age2, 'years old')
"""

#BRAINTEASERS
"""
Write a python program that obtains a base and height of a triangle from the user.
1/2 B * H       

Obtain numerator and a denominator then you print the equation and result of long division

Enter numerator: 7
Enter denominator: 3
7 /2 = 2 R 1


Constant Variables
    - It is convention (not a hard rule) that constants are named in ALL_CAPS
"""

Name = "Nutshack"
PI = 3.14 #hint that its a constant name. all constant names are all caps
TACO_PRICE = float(3.25) #This vairable is not gonna change. Hence its called price name. 


print(Name)
print("The taco price is:", TACO_PRICE)
How_much = float(input("Select how much Tacos you want: "))
Total_Price = How_much * TACO_PRICE  #REMEBER CAN NOT MULTIPLY FLOAT WITH A STRING THATS JUST NOT POSSIBLE     "Taco_Price"

print("Total price will be:", Total_Price)

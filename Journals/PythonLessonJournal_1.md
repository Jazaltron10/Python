# The Jazaltron Learning Journal
## This is the First LessonJournal in the Python series 

### Different ways of concatenating strings in python.

    print("20 days are "+str(20*24*60)+" minutes")=>old way<br>
    print(f"20 days are {20*24*60} minutes")=>New way
    The f just stands for *format*

 
### Variables 
    calculation_to_secs = 24x60x60
    name_of_unit = "seconds"

Use variables for values that end up repeating themselves in your program

Also use a descriptive variable name for your assigned value 
    
    print(f"35 days are {35*calculation_to_secs} {name_of_unit}")
    print(f"132 days are {132*calculation_to_secs}{name_of_unit}")
    print(f"96 days are {96*calculation_to_secs} {name_of_unit}")

###Functions 
+ Functions are simply blocks of code that does something and are used to avoid 
   repeating the same logic. 
+ A function in python is defined using the **def** keyword
+ It is a block of code that only runs when it is called 
+ Whatever that is part of the function is called the function body


### Parameters
+ These are some kind of input values 
  that contain information and can be 
  passed into a function.
+ Parameters are also called arguments
  When the function is been called. 



##### Example:
    calculation_to_secs = 24 <br>
    name_of_unit = "hours" <br>

    def days_to_units(num_of_days, custom_message):<br>
        print(f"{num_of_days} days are {num_of_days * calculation_to_secs} {name_of_unit}")
        print("all good!")



##### calling the functions 
    days_to_units(21, "Awesome! \n")
    days_to_units(35, "Looks Good \n" )
    days_to_units(60, "Good job \n")
    days_to_units(90, "Python is the way \n")
 
### Scope  
#####  Variable scopes simply means where is the variable the function uses, defined
+ A Variable has a **Global Scope** for a function if it is described/created outside 
    the function. They are accessible to every function within the program

+ A Variable has a **Local Scope** if it is created within/(inside) a function 



##### Types of Variable 
+  Global Variable 
+  Internal Variable passed in as a parameter
+  Internal Variable defined within the function 

##### Example:
    def Scope_check(num_of_days):
        my_var = "Variable inside function"
        print(name_of_unit)
        print(num_of_days)
        print(my_var)

    Scope_check(20)

### User Input 
+ To ask the user for an input you use
   input()
+ Python stops executing when it comes 
   to the input()
+ It is a built-in function in python
+ You can provide a string parameter within 
  the input function to clarify to the 
  user on what is to be done precisely
+ You can then use the input provided by
  assigning it to a variable.  
  
##### Expression:
This is an instruction that combines values 
and operators and always evaluates 
down to a single value.  

##### Example:
    User_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
    print(f"{User_input} years ago....")


### Functions With Return Values
+ A function can return data as result
+ You do this using the **return** keyword
+ when we return a value from a function
  we can assign it to a variable

##### Example:
    calculation_to_secs = 24
    name_of_unit = "hours"


    def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_secs} {name_of_unit}"

    my_var = days_to_units(20)
    print(my_var)

##### Casting
This is the process of turning one data
type to another.<br> 
**int()**:   
+ Is a built in Python function
+ converts the specified value into an integer number
+ The integer number is returned by the function 

##### Example:
    calculation_to_secs = 24
    name_of_unit = "hours"


    def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_secs} {name_of_unit}"


    User_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
    User_input_number = int(User_input)
    Calculated_Value = days_to_units(User_input_number)
    print(Calculated_Value)

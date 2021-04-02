# The Jazaltron Learning Journal
## This is the Second LessonJournal in the Python series 

### Conditionals (if / else) & Boolean Data Type
    In programming when we allow users to give 
    our program some input value we would also 
    want to restrict them and basically validate 
    that what they provided as input is a valid 
    value for our program specifically

##### Input Validation
**We validate User Input because**
**we want to avoid or handle values:**
+ Which doesn't make sense
+ That could crash our program
+ Could even be a security risk
 
**When Ever You Allow User Input You** 
**Always Have To Validate It**

    Conditional
        if condition is correct:
        then do this 

    otherwise:
        do this

+ A conditional can either be true or false

### Boolean Data Type 
+   A type of data type that could either be
    true or false
    
+   The built-in function of type() in python
    takes in a variable as a parameter and then
    prints out it's **Data Type**
    
+   It Looks like this: print(type(condition_check))
    
+   You can nest Functions in python this 
    because the Return value of inner function
    is the input value for the outer function 
    
+   They are the core part of writing anyform 
    of logic in programming

##### Example:  
    calculation_to_secs = 24 <br>
    name_of_unit = "hours"


    def days_to_units(num_of_days):
    condition_check = num_of_days > 0 <br>
    print(type(condition_check))<br><br>
        
        if num_of_days > 0:
            return f"{num_of_days} days are {num_of_days * calculation_to_secs} {name_of_unit}"
        elif num_of_days == 0:
            return "You entered a 0, please enter a valid positive number"
        else:
            return "You entered a negative value,so no conversion for you"

    User_input = input("Hey user, enter a number of days and i will convert it to hours!\n")<br>
    User_input_number = int(User_input)<br>
    Calculated_Value = days_to_units(User_input_number)<br>
    print(Calculated_Value)<br>

##### type()
+ This just checks the data type of the value or variable that is being passed into it
+ To see the result, it has to be nested in a print function like this print(type(30))
+ checking for type string => print(type("This Should be a string type"))
+ checking for type integer => print(type(30))
+ checking for type float => print(type(89.37))


### More User Input Validation 
+ checking if **string** was entered instead of int
+ In python you can have an if statement without an
  else statement.

### CLeaning Up The Code 
> As a common and best practice all logic are usually encapsulated in a function
##### Example:
    calculation_to_secs = 24<br>
    name_of_unit = "hours"<br>


    def days_to_units(num_of_days):

    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_secs} {name_of_unit}"
    elif num_of_days == 0:
        return "You entered a 0, please enter a valid positive number"


    def validate_and_execute():
    
    if User_input.isdigit():
        User_input_number = int(User_input)
        Calculated_Value = days_to_units(User_input_number)
        print(Calculated_Value)
    else:
        print("Your input is not a valid number, Don't ruin my program!")

    validate_and_execute()<br>
    User_input = input("Hey user, enter a number of days and i will convert it to hours!\n")<br>


### Nested i f...Else
   with this all validation logic can be put in one place
   
##### Example:
    calculation_to_secs = 24
    name_of_unit = "hours"


    def days_to_units(num_of_days):
           return f"{num_of_days} days are {num_of_days * calculation_to_secs} {name_of_unit}"


    def validate_and_execute():
        if User_input.isdigit():
            User_input_number = int(User_input)
            if User_input_number > 0
                Calculated_Value = days_to_units(User_input_number)
                print(Calculated_Value)
            elif User_input_number == 0:
                print("You entered a 0, please enter a valid positive number")
        else:
            print("Your input is not a valid number, Don't ruin my program!")

    validate_and_execute()
    User_input = input("Hey user, enter a number of days and i will convert it to hours!\n")

### Error Handling with try/except
The try block: lets you "test" a block of code for errors.
with this you can cover multiple errors and avoid doing a 
nested if/else validation it is very useful for places 
where you can't really validate something using 
the if condition especially if there is a chance that you might miss something 

##### Example:
    calculation_to_secs = 24
    name_of_unit = "hours"


    def days_to_units(num_of_days):

        if num_of_days > 0:
            return f"{num_of_days} days are {num_of_days * calculation_to_secs} {name_of_unit}"



    def validate_and_execute():
        try:

            User_input_number = int(User_input)
            if User_input_number > 0:
                Calculated_Value = days_to_units(User_input_number)
                print(Calculated_Value)
            elif User_input_number == 0:
                print("You entered a 0, please enter a valid positive number")
            else:
                print("You entered a negative number, no conversion for you!")
        except ValueError:
            print("Your input is not a valid number, Don't ruin my program!")



    User_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
    validate_and_execute()



###### My While Loop work in progress

    r_input = ""
    while r_input != "stop":
        User_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
        validate_and_execute()
        r_input = input("If you want to exit just type 'stop' \n")



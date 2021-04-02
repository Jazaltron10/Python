# The Jazaltron Learning Journal
## This is the Fourth LessonJournal in the Python series 


#### Built In Functions
These are functions that python makes available to us to use

###### Example:
+   print() => Prints to the standard output device
+   input() => Asks user for input
+   set() => Returns a new set from a given list
+   int() => Converts a value into an integer number <br>

These are just a few built-in functions in python there are still a lot
more built-in functions that are available to us.<br>
Most of these built-in functions accepts an input parameter and then 
does something with it to give us some kind of output.<br>
This is logical because the purpose of a function is to take in some
input do something with it and then give us a result or output.<br>


###### The Second Type Of Built-in Functions 
Unlike the first type of built in functions these second types do not take in any
parameter and are called on directly on a specific data type value.<br>
The major difference between this type of built-in function and the first is that
+   Each data type has its own built-in functions(i.e referring to the second type)
+   They are very useful and makes sense only for that specific data type 
+   The parameters for these functions are actually the value for which we are calling the function for 
+   In some cases special parameters can also be passed into the function itself

###### Example:
    "Jonathan".split(, )
    "text".split()
    [1, 3, 4].count()
 

 
#### The Dictionary Data Type 
+   They are used to store values in key:value pairs
+   It is a collection, which does not allow duplicate values
+   items can be accessed by its key name 
+   you can use square brackets or get( method )<br>
    your_dict["days"] or your_dict.get("days")<br>
   
###### Syntax For:  Time Converter    
    def days_to_units(num_of_days, conversion_unit):
        if conversion_unit == "hours":
            return f"{num_of_days} days are {num_of_days * 24} hours"
        elif conversion_unit == "minutes":
            return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
        else:
            return "unsupported unit!"


    def validate_and_execute():
        try:
            User_input_number = int(days_and_unit_dictionary["days"])

            # we want to do conversion only for positive integers
            if User_input_number > 0:
                Calculated_Value = days_to_units(User_input_number,days_and_unit_dictionary["unit"])
                print(Calculated_Value)
            elif User_input_number == 0:
                print("You entered a 0, please enter a valid positive number")
            else:
                print("You entered a negative number, no conversion for you!")
        except ValueError:
            print("Your input is not a valid number, Don't ruin my program!")

    
    User_input = ""
    while User_input != "exit":
        User_input = input("Hey user, enter a number of days and conversion unit!\n")
        days_and_unit = User_input.split(":")
        print(days_and_unit )
        days_and_unit_dictionary = {"days":days_and_unit[0], "unit":days_and_unit[1]}
        print(days_and_unit_dictionary)
        print(type(days_and_unit_dictionary))
        validate_and_execute()


###### Summary of all the Data-types we've done so far
        message = "enter some value"
        days = 20
        price = 9.99
        valid_number = True
        exit_input = False
        list_of_days = [20, 40, 20, 100]
        list_of_months = ["January", "February", "June"]
        set_of_days = {20, 45, 100}
        days_and_unit = {"days":10, "unit":"hours"}

###### Why do we need all these data types?
+   Depending on what you try to achieve in your program you are gonna need 
    a different data type to achieve exactly that.

#### Modules
This helps the programmer connect to other python files(.py)<br>
so in other words a module is a python file that contains functions and variables 
that you can use in another python file.  
+   Logically organize your python code
+   Module should contain related code 
+   The things that are defined in the module that you can basically 
    use in another file are called **definitions**
+   To rename the module you'll have to use this syntax:<br>
    **import ExternalPythonFile as epf**
###### Syntax:
    import ExternalPythonFile
    
     
    """ 
    Block 
    of 
    code
    """
    ExternalPythonFile.function_imported()
    
###### Syntax: for importing only one item to be used(could be a function or variable) 
    from ExternalPythonFile import function_to_be_used, variable_to_be_used
    
    """ 
   
    Block 
    of 
    code(variable_to_be_used)
    
    """
    function_to_be_used()
    
###### alternatively you can import all by using *
    
    
    from ExternalPythonFile import * 
    """    
    
    Block 
    of 
    code(variable_to_be_used)
    
    """
    function_to_be_used()

#### Built-In Python Modules    
+   we can use modules that python itself already created
+   Example: math module , datetime module etc...
+   They contain multiple functions and variables for the specific use case 
    in which the module is being used 
    
 ###### Examples Of Built-In Modules
 
        import os
        print(os.name)
        
        # used for logging errors
        import logging
        logger = logging.getLogger("MAIN")
        logger.error("Error happened in the app")
         
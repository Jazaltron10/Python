# The Jazaltron Learning Journal
## This is the Third LessonJournal in the Python series 



#### While Loop
The whole concept of loops in programming is basically that you get to do the
same thing multiple times, in this case it is executing logic multiple times.
And how many times that logic gets executed is basically defined in the condition 
of that loop, and the condition could be it should run ten times or it should run
until some specific event happens in the application

Conditions
+ They basically evaluate to true or false 
+ They are used most commonly in **if statements** and **loops**

While loop - This executes a statement as long as a condition is true
    
    while True:
        User_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
        validate_and_execute()
 
##### Let user exit the program
 ##### Example:
    calculation_to_secs = 24
    name_of_unit = "hours"


    def days_to_units(num_of_days):
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

    User_input = ""
    while User_input != "exit":
        User_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
        validate_and_execute()

 ##### Program Flow
+ Assign an empty string to User_input
+ First Loop{Condition gets evaluated}: As long as the user input is something different than "exit"
+ User is prompted for its input
+ Function is called and input is validated and executed
+ Second Loop{Condition gets reevaluated}:check if "exit" was typed in
+ User is prompted for its input
+ Function is called and input is validated and executed 
+ Loop continues
+ program stops only when the User types exit and it is evaluated by the loop conditional



 #### LISTS & FOR LOOP
Here We Explore entering a set of values once and iterating over them while 
performing operations on them. 

##### The List Data-type
+ This is just another data type that is used to store multiple items in a
  single variable.
+ A list can contain different data types
##### The For Loop
+ It is used for iterating over a sequence (like a list)
+ So we can execute something for each item in a list 
 
 e.g 
 + from the example above, if given a list of [10, 15, 40, 100]
 + In order to call the validate_and_execute() function for each number in the list
 + we would have to use the for loop since the basic definition of a loop is 
 + simply executing the same function with the same logic multiple times
 + and the number of times depends on the condition stated in the loop definition
 + and it being a loop requires a condition for it to keep running<br>
 (
    i.e it needs a conditional statement for it to keep on executing the 
    validate_and_execute() function for each element(number) in the list.
 )
 + in this case the condition happens to be the number of elements in the list
   (i.e length of the list)
   
 Syntax 
    for element in list:  
        def validate()
        
 +  The condition above is implicit and it simply states that for however how many 
    elements there are in this list that many times the function or block of code 
    validate will be  executed 
 +  However the list is created as a string this because input is always a string 
    and to convert it we'll have to use list.split()
 +  split() is a function that would take the string being passed on by the user
    as a parameter and would give us a list data type(it basically converts string to list data type)
 +  so the split function will basically return a list of those input values  
 +  to see what the list looks like and to get the data type of the list you use 
 +  split function by default splits that provided lists on spaces and then provides 
    alist out of them. However it can be overriden to split on comma, as shown below: 
            
                
                print(type(User_input.split(", ")))
                print(User_input.split(", "))
    
 ##### Example:
 
        calculation_to_secs = 24
        name_of_unit = "hours"


        def days_to_units(num_of_days):
            return f"{num_of_days} days are {num_of_days * calculation_to_secs} {name_of_unit}"


        def validate_and_execute():
            try:
                User_input_number = int(num_of_days_element)
                if User_input_number > 0:
                    Calculated_Value = days_to_units(User_input_number)
                    print(Calculated_Value)
                elif User_input_number == 0:
                    print("You entered a 0, please enter a valid positive number")
                else:
                    print("You entered a negative number, no conversion for you!")
            except ValueError:
                print("Your input is not a valid number, Don't ruin my program!")

        User_input = ""
        while User_input != "exit":
            User_input = input("Hey user, enter a number of days as a comma separated list and i will convert it to hours!\n")
            print(type(User_input.split(", ")))
            print(User_input.split(", "))
            for num_of_days_element in User_input.split(", "):
                validate_and_execute()
                

##### Basic List Operation
+ You can create a list
+ Access items of the list 
+ Add an item to the list
+ Remove an item from the list
+ Change items in the list

Syntax: 
       
        # creating a list
        my_list = ["january", "february", "march", "January"] 

        # printing/accessing a specific item on the list
        print(my_list[2]) 

        # adding items
        my_list.append("april") 

        # printing the entire list
        print(my_list) 

        # Using a for loop to iterate over a list
        for k in my_list:
            print(f"{k} is a nice month!")

        # removing from a list
        my_list.remove("january")
        print(my_list)

            
            
##### Comments
+ These are used to explain blocks of code for easy understanding
+ Comments are easy way to communicate your thoughts and logic 
  so that other collaborators can easily step through your code 
+ Can be used to prevent execution of a block of code when testing code
  (Python Interpreter ignores it) 

  
Syntax:
+ Multi-line comments   """ Block of Code """
+ Single-line comments   # Block Of Code 

  
Best Practices:
+ Don't overuse Comments!
+ You should try to make your Code self-explanatory by using
  descriptive variable and function names
  
  
  
  #### Sets 
  it is a data type similar to list but does not allow for duplicate values <br>
  
  Syntax:<br>
  set(my_list)
  
  ##### Nested Function Execution
  It starts executing from the innermost function <br>
  Syntax:  print(type(set(list_of_days)))
            
            1. set(list_of_days)
                =>Input:the user input array
                =>Output:Returns the converted set
            
            2.type(return_value_of_previous_func)
                =>Input:the converted set
                =>Output:Returns the data type of the set
            
            3.print(return_value_of _previous_func)
                =>Input:the data type 
                =>Output:Prints the value to console        
  
  
  
  ###### SET Example:
    calculation_to_secs = 24
    name_of_unit = "hours"


    def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_secs} {name_of_unit}"
        
            



    def validate_and_execute():
        try:
            User_input_number = int(num_of_days_element)

            # we want to do conversion only for positive integers
            if User_input_number > 0:
                Calculated_Value = days_to_units(User_input_number)
                print(Calculated_Value)
            elif User_input_number == 0:
                print("You entered a 0, please enter a valid positive number")
            else:
                print("You entered a negative number, no conversion for you!")
        except ValueError:
            print("Your input is not a valid number, Don't ruin my program!")

    User_input = ""
    while User_input != "exit":
        User_input = input("Hey user, enter a number of days as a comma separated list and i will convert it to hours!\n")
        list_of_days = User_input.split(" ")

        print(list_of_days)
        print(set(list_of_days))

        print(type(list_of_days))
        print(type(set(list_of_days)))

        for num_of_days_element in set(list_of_days):
           validate_and_execute()




+ items in a set do not have a defined order!
+ items cannot be referred to by index!
+ items cannot be changed, only added/removed
+ we can only access the elements of a set with a loop <br>

Syntax:

        # creating a set
        my_set = {"january", "february", "march"} 
        
        #Accessing elements in a set 
        for item in my_set:
            print(f"\n{item} is a nice month when it comes to the world of python!")

        #adding new elements
        my_set.add("july")
        print(my_set )

        #removing elements
        my_set.remove("january")
        print(my_set)



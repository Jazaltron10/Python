def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit!"



def validate_and_execute(days_and_unit_dictionary):
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


user_input_message = "Hey user, enter a number of days and conversion unit! like this days:unit\n"
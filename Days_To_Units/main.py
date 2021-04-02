from Days_To_Units.helper import validate_and_execute, user_input_message
# This is a Time Converter App
User_input = ""
while User_input != "exit":
    User_input = input(user_input_message)
    days_and_unit = User_input.split(":")
    print(days_and_unit )
    days_and_unit_dictionary = {"days":days_and_unit[0], "unit":days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute(days_and_unit_dictionary)




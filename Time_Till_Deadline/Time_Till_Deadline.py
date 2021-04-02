from datetime import datetime

user_input = input("enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]


deadline_date = datetime.strptime(deadline,"%d/%m/%Y")
# calculate how many days from now till deadline
today_date = datetime.today()

due_date = deadline_date - today_date

# due_date_in_days = due_date.days
due_date_in_hours = int(due_date.total_seconds()/ 60 /60)
print()
print(f"Dear user! Time remaining for your goal: {goal} is {due_date_in_hours} hours")





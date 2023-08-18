from datetime import datetime
import datetime as dt
import django

user_input = input(
    "Please enter your Project with deadline delimited by colon. Please provide date format in dd.mm.yyyy\n")
input_list = user_input.split(":")
project = input_list[0]
deadline = input_list[1]

print(f"User input is {input_list}")

deadLine_date = datetime.strptime(deadline, "%d.%m.%Y")
print(f"Dead line date in date format is {deadLine_date}")

today_date = datetime.today()
time_left = deadLine_date - today_date


print(f"Time left for project {project} is {time_left.days}")
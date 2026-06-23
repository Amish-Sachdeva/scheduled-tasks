import random
import pandas
import smtplib
import os
from datetime import datetime

today = (datetime.now().month, datetime.now().day)
data_file = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data_file.iterrows()}   #


if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        email = os.environ["MY_EMAIL"]
        password = os.environ["EMAIL_APP_PASS"]
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!\n\n {content}")

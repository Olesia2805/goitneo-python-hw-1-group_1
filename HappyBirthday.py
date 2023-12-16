# import libraries
from datetime import datetime, timedelta
from collections import defaultdict

# sorted list users and write days in correct order
def sorted_by_month_day (users):
    return sorted(users, key = lambda x: datetime.strptime(x["birthday"].strftime('%m-%d'), '%m-%d'))

# creation function for get birthdays
def get_birthdays_per_week (users):

    # what days is it today
    today = datetime.today().date()

    # save date of birth in days of week
    birthday_per_week = defaultdict(list)

    # check each user
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        
        # check if this person has already birthday in this year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # difference in  (compare with today)
        delta_days = (birthday_this_year - today).days

        # check day of week (which day of week it will be)
        if delta_days < 7:
            if delta_days == 0:
                day_of_week = "Today"
            elif delta_days == 1:
                day_of_week = "Tomorrow"
            else:
                # check if the birthday falls on the weekend and if it's a Saturday or Sunday, greet on Monday
                if (today + timedelta(days=delta_days)).weekday() >= 5:
                    day_of_week = "Monday"
                else:
                    day_of_week = (today + timedelta(days=delta_days)).strftime('%A')
            birthday_per_week[day_of_week].append(name)
        
    return birthday_per_week

# users for example
# name, surname, birthday (Year, month, day)
users = [
    {"name": "Bill Gates", "birthday": datetime(2023, 12, 15)},
    {"name": "Ben Ten", "birthday": datetime(2002, 12, 13)},
    {"name": "Nastia Ermak", "birthday": datetime(2003, 12, 10)},
    {"name": "Jan Koum", "birthday": datetime(1980, 12, 12)},
    {"name": "Richard Mork", "birthday": datetime(2023, 12, 16)},
    {"name": "Rosa Tier", "birthday": datetime(2018, 4, 5)},
    {"name": "Robert Gat", "birthday": datetime(2023, 12, 15)},
    {"name": "Angelina Hanz", "birthday": datetime(2001, 12, 27)},
    {"name": "Olesia Vys", "birthday": datetime(2020, 5, 28)}
]

# print result
result = get_birthdays_per_week(sorted_by_month_day(users))

# decoration
if result:
    print ("\n🥳 Don't forget write HAPPY BIRTHDAY!!!\n")
else:
    print ("\nYou congratulated everyone")

# find people who have birthday in this week
for day, names in result.items():
    print(f"{day}: {', '.join(names)}")
    
# decoration
print("\n🎊 🎉 🎁 🎈 🎀 🪄 🪅\n")

from datetime import datetime
import datetime as dt

# Get the current date and time
now = dt.datetime.now()
print("Current date and time:", now)

# Add 1 hour, 23 minutes, and 10 seconds to the current time
future_time = now + dt.timedelta(days=1, minutes=23, seconds=10)
print("Future time:", future_time)

# Define two dates
date1 = datetime.strptime('2022/2/20', "%Y/%m/%d")
date2 = datetime.strptime('2021/10/20', "%Y/%m/%d")

# Calculate the difference in days
difference = (date2 - date1).days
print("Difference in days:", difference)


date_str = "2025-07-15 15:45:00"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(dt)

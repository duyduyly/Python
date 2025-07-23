# Datetime
- [**Date And Time**](#date-and-time)
- [**Calculate Datetime**](#calculate-datetime)
- [**Conversion**](#date-conversion)
  - [*Format Codes*](#format-codes)
  - [*String to Date*](#string-to-date)
  - [*Date To Time*](#date-to-time)
- [**Comparing Dates**](#comparing-dates)
- [**More Libraries**](#more-libraries)

------------
<br/>

## Date and Time
```python
from datetime import datetime

now = datetime.now()
print(now)  # 2025-07-15 16:30:25.123456

print(now.year)     # 2025
print(now.month)    # 7
print(now.day)      # 15
print(now.hour)     # 16
print(now.minute)   # 30
print(now.second)   # 25


#Create Datetime
dt = datetime(2024, 12, 25, 10, 30, 0)
print(dt)  # 2024-12-25 10:30:00

#Date Only and Time Only
today = datetime.today().date()    # Only date
current_time = datetime.now().time()  # Only time

#Get Weekday
print(now.weekday())  # Monday=0, Sunday=6
print(now.strftime("%A"))  # Full name: e.g., Tuesday
```

------------
<br/>

## Calculate Datetime
```python
from datetime import timedelta
from datetime import datetime

now = datetime.now()
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
print(tomorrow)

next_hour = now + timedelta(hours=1)
print(next_hour)
```

----------------
<br/>

## Date Conversion
### Format Codes
- Example Date: `2025-07-15 17:41:08.548513` in timezone `Asia/Ho_Chi_Minh (UTC+0700)`

```python
from datetime import datetime
import pytz  # install with: pip install pytz

# Set example datetime in Asia/Ho_Chi_Minh timezone
tz = pytz.timezone("Asia/Ho_Chi_Minh")
dt = tz.localize(datetime(2025, 7, 15, 17, 41, 8, 548513))
```

| Directive | Description                                      | Example Result           |
|-----------|--------------------------------------------------|--------------------------|
| `%a`      | Weekday, short version                           | Tue                      |
| `%A`      | Weekday, full version                            | Tuesday                  |
| `%w`      | Weekday as a number 0-6, 0 is Sunday             | 2                        |
| `%d`      | Day of month 01-31                               | 15                       |
| `%b`      | Month name, short version                        | Jul                      |
| `%B`      | Month name, full version                         | July                     |
| `%m`      | Month as a number 01-12                          | 07                       |
| `%y`      | Year, short version, without century             | 25                       |
| `%Y`      | Year, full version                               | 2025                     |
| `%H`      | Hour 00-23                                       | 17                       |
| `%I`      | Hour 01-12                                       | 05                       |
| `%p`      | AM/PM                                            | PM                       |
| `%M`      | Minute 00-59                                     | 41                       |
| `%S`      | Second 00-59                                     | 08                       |
| `%f`      | Microsecond 000000-999999                        | 548513                   |
| `%z`      | UTC offset                                       | +0700                    |
| `%Z`      | Timezone                                         | ICT                      |
| `%j`      | Day number of year 001-366                       | 196                      |
| `%U`      | Week number of year (Sunday as first day), 00-53 | 28                       |
| `%W`      | Week number of year (Monday as first day), 00-53 | 29                       |
| `%c`      | Local version of date and time                   | Tue Jul 15 17:41:08 2025 |
| `%C`      | Century                                          | 20                       |
| `%x`      | Local version of date                            | 07/15/25                 |
| `%X`      | Local version of time                            | 17:41:08                 |
| `%%`      | A `%` character                                  | %                        |
| `%G`      | ISO 8601 year                                    | 2025                     |
| `%u`      | ISO 8601 weekday (1-7, Monday = 1)               | 2                        |
| `%V`      | ISO 8601 week number (01-53)                     | 29                       |


#
### String to Date
```python
from datetime import datetime

date_str = "2025-07-15 15:45:00"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(dt)
```

#
### Date To Time
```python
from datetime import datetime

now = datetime.now()
now_str = now.strftime("%d/%m/%Y %H:%M")
print(now_str)  # e.g., 15/07/2025 16:30
```

------------
<br/>

## Comparing Dates
```python
from datetime import datetime

if datetime.now() > datetime(2025, 1, 1):
    print("New Year has passed!")
```

------------
<br/>

## More Libraries
| Library    | Use Case                            |
|------------|-------------------------------------|
| `pytz`     | Time zone support                   |
| `dateutil` | Natural parsing, relative dates     |
| `arrow`    | Human-friendly datetime replacement |
| `pendulum` | Modern and timezone-aware datetime  |


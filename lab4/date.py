"""
from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print(new_date.strftime('%Y-%m-%d'))
"""

"""
from datetime import datetime, timedelta

today = datetime.now()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

# Print the results
print(yesterday.strftime('%Y-%m-%d'))
print(today.strftime('%Y-%m-%d'))
print(tomorrow.strftime('%Y-%m-%d'))
"""

"""
from datetime import datetime

current_datetime = datetime.now()

current_datetime_2 = current_datetime.replace(microsecond=0)

print(current_datetime_2)
"""

"""
from datetime import datetime, timedelta

date1 = datetime.now()
date2 = datetime(2026, 5, 7, 12, 0, 0)

dif = (date2 - date1).total_seconds()

print(dif)
"""


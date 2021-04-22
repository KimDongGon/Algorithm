import datetime
now = datetime.datetime.utcnow()
print(now.year)
print(str(now.month).zfill(2))
print(now.day)
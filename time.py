from datetime import datetime

now = datetime.now()
current_hour = now.hour
current_minute = now.minute
current_second = now.second

print str(current_hour) + ":" + str(current_minute) + ":" + str(current_second)
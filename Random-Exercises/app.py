#This program calculates the hours, minutes, seconds and days since 1 january of 1970
import time

seconds = int(time.time())
minutes = int(int(seconds / 60))
hours = int(minutes / 60)
days = int(hours / 24)


print(f"Since 1970, {days} days, {hours} hours, {minutes} minutes and {seconds} seconds have passed")

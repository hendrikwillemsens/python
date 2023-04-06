#!/usr/bin/python3
################################################################################
# TIME MODULE (example-code-4-time.py)
################################################################################
import time
# Seconds since epoch
ticks = time.time()
print("\nNumber of ticks since epoch (January 1, 1970):")
print(ticks)
# Use time to get and use struct_time
timetuple = time.localtime(time.time())
print("\nLocal current time:\n{}".format(timetuple))
print("Year: {}".format(timetuple.tm_year))
print("Hour: {}".format(timetuple.tm_hour))
# Hour & min
hourmin = str(timetuple.tm_hour) + "h" + str(timetuple.tm_min)
print("Hour & min: {}".format(hourmin))
# Formatted time
time_string = time.strftime("%d/%m/%Y, %H:%M:%S", timetuple)
print("\nFormatted time: {}".format(time_string))
# Sleep
print("\nSleeping...\n")
time.sleep(3.5)
print("\nThis is printed after 3.5 seconds!\n")
################################################################################
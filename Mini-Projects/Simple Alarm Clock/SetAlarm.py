#Simple-Alarm-Clock

import time

alarm = input("Set alarm time (HH:MM): ")

print("Alarm is running...")

while True:
    current_time = time.strftime("%H:%M")

    if current_time == alarm:
        print("Wake Up! Alarm Time!")
        break

    time.sleep(1)

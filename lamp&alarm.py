#Automatic night lamp and morning alarm
import time
def is_night():
    current_hour = time.localtime().tm_hour
    return 18 <= current_hour or current_hour < 6
def turn_on_lamp():
    print("Night lamp is ON")

def turn_off_lamp():
    print("Night lamp is OFF")

def morning_alarm():
    print("It's time to wake up!")
try:
    print("Set time for alarm: ")
    h=int(input("Hours: "))
    m=int(input("Minutes: "))
    while True:
        if is_night():
            turn_on_lamp()
        else:
            turn_off_lamp()

        # Check for morning alarm
        current_time = time.localtime()
        print(current_time.tm_hour,":",current_time.tm_min,end="  ")
        if current_time.tm_hour == h and current_time.tm_min == m:
            morning_alarm()

        time.sleep(2)  # Check every 2 seconds

except KeyboardInterrupt:
    print("Program terminated by user.")

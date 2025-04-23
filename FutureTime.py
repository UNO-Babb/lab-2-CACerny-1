#FutureTime.py
#Name: Caden Cerny
#Date: Feb. 2
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
    now = datetime.datetime.now()
    currentHour = now.hour
    currentMinute = now.minute

    add_hours = int(input("Enter the number of hours to add: "))

    add_minutes = int(input("Enter the number of minutes to add: "))

    total_minutes = currentMinute + add_minutes
    extra_hours = total_minutes // 60
    final_minutes = total_minutes % 60

    final_hour_24 = (currentHour + add_hours + extra_hours) % 24

    final_hour = (final_hour_24 - 1) % 12 + 1

    print(f"The time will be: {final_hour}:{final_minutes:02d}")

if __name__ == '__main__':
  main()

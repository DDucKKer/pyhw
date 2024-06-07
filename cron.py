import schedule
import time
from datetime import datetime

def job():
    print("I'm working...")
    current_dateTime = datetime.now()

    print(current_dateTime)


def another_job():
    print("I'm working... really")
    current_dateTime = datetime.now()

    print(current_dateTime)


schedule.every(5).seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
# schedule.every().minute.at(":17").do(job)
schedule.every().minute.at(":30").do(another_job)
schedule.every().minute.at(":10").do(another_job)

while True:
    schedule.run_pending()
    time.sleep(1)

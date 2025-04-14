import smtplib
import datetime as dt
import random
#from http.cookiejar import month

my_email = "azakgzuu@gmail.com"
password = "fxsksfeulwbyicjd"

def send_email(text):
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="nurjamalkanatbekova8@gmail.com",
        msg=f"Subject:Hello\n\n{text}.")
    connection.close()

# def random_line(afile):
#     line = next(afile)
#     for num, aline in enumerate(afile, 2):
#         if random.randrange(num):
#             continue
#         line = aline
#     return line

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

nurzhamals_day = '04/14'

month1 = int(nurzhamals_day[:2])
day1 = int(nurzhamals_day[3:])
lines = open('quotes.txt').read().splitlines()

print(month, month, day, day1)

if month1 == month and day1 == day:
    send_email(random.choice(lines))



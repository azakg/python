import smtplib

my_email = "azakgzuu@gmail.com"
password = "fxsksfeulwbyicjd"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="nurjamalkanatbekova8@gmail.com",
    msg="Subject:Hello\n\nThis is the body of my email.")
connection.close()
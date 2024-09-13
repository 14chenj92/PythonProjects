import smtplib

email = input("Email: ")
receiver_email= input("Receiver: ")

subject = input("Subject: ")
message = input("Message: ")

text = f"Subject: {subject}\n\n{message}"

server= smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "xwbk blzb qhur mmgj")

server.sendmail(email, receiver_email, text)

print("Email has been sent to " + receiver_email)
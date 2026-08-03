import smtplib

EMAIL = "vedikajadhav0213@gmail.com"
APP_PASSWORD = "vedika2637"

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, APP_PASSWORD)
    print("Login Successful!")
    server.quit()

except Exception as e:
    print(e)
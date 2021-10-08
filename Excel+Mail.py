import pandas as pd
import smtplib, ssl

# Open port with  [  python -m smtpd -c DebuggingServer -n localhost:1025  ] first
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "krit.peace@mail.kmutt.ac.th"  # Enter your address
receiver_email = ""  # Enter receiver address
password = input("Type your password and press enter: ")
message_header = """\
Subject: FRA141 - Assignment 7 : List II

This is the last assignment. Please read the instructions and enjoy ^^ \n\n"""



FRA141_Link_Path    = '/Users/Peace/Desktop/Link_Assignments.xlsx'
FRA141_Student_Path = '/Users/Peace/Desktop/Student_Assignments.xlsx'
FRA141_Mail_Path    = '/Users/Peace/Desktop/Student_Mail.xlsx'

df  = pd.read_excel(FRA141_Link_Path,sheet_name='List II', header=None)
df2 = pd.read_excel(FRA141_Student_Path,sheet_name='List II', header=None)
df3 = pd.read_excel(FRA141_Mail_Path,sheet_name='Mail', header=None)

for i in range(0,80):
    message_tail = ""
    for j in range(0,3):
        print(df2.iloc[i,j])
        q = df2.iloc[i,j]
        print(df.iloc[q-1,0])
        message_tail = message_tail + str(df.iloc[q-1,0]) + "\n\n"

    print("----------------")
    print(df3.iloc[i,0])
    print("----------------")

    receiver_email = str(df3.iloc[i,0])
    message = message_header + message_tail
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        
#from bs4 import BeautifulSoup as soup
#import urllib.request
import pandas as pd
#import pandas_datareader as pdr
from pandas import ExcelWriter
import datetime
from time import strptime

import smtplib
#from email.mime.text import MIMEText

def send_mail():

    gmail_user = 'abce@gmail.com'
    gmail_password = 'xxxxxx'

    sent_from = gmail_user
    to = ['tariq.delwar@gmail.com']
    subject = str(item) + str(' ') + str(latest_earnings)  #'OMG Python Test'
    body = 'Earnings\n\n'    #-You

    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()


list = ['FSLY','MU','MDB']
# list = ['XXXX']
xls_path = '/Users/tony/documents/Python_Projects/test_prices_2.xlsx'

writer = pd.ExcelWriter(xls_path, engine='xlsxwriter')

# for item in list:
#     print (item)

for item in list:
    print (item)
    try :

        earnings = pd.read_html('https://finance.yahoo.com/calendar/earnings?day=2019-06-13&symbol=' + str(item))[0]
        latest_earnings = earnings['Earnings Date'].tolist()[3] #[:4]
        #report_earnings = latest_earnings[4]
        #latest_earnings = earnings[:4]
        print (latest_earnings)
        passer(latest_earnings)

    except :
        print ("Stock not found")



def passer(latest_earnings):
    earnings_Date = latest_earnings[:-3]

    today = datetime.datetime.today()
    date = datetime.datetime.strptime(earnings_Date, "%b %d, %Y, %I %p") # Corrected
    day_count = (date - today).days
    if day_count <= 3:
        print (day_count)
        send_mail()

    else:
        print ("Out of range")

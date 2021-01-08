# email: couch-965@couch-300017.iam.gserviceaccount.com

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup
import requests
import time

scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("portfolio").sheet1
data = sheet.get_all_values()

# justetf.com adresses
iShares = "IE00B1FZS350"
Vanguard = "IE00B3VVMM84"
Lyxor = "LU0419741177"
Xtracker = "IE00BK1PV551"

names = ["Vanguard", "Xtracker", "Lyxor", "iShares"]
adresses = [Vanguard, Xtracker, Lyxor, iShares]

while True:
    for i in range(0, len(adresses)):
        html = requests.get("https://www.justetf.com/de/etf-profile.html?isin={}".format(adresses[i])).text
        soup = BeautifulSoup(html, "html.parser")

        price = soup.find(class_="infobox").find(class_="val").find_all("span")[1].text
        price = price.replace(",", ".")  # NEEDED for english notation
        price = float(price)
        print("The current price for {} is {}".format(names[i], price))

        sheet.update("F{}".format(i+2), price)
    time.sleep(10)

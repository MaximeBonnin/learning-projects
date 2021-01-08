from pprint import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from bs4 import BeautifulSoup

# authorize for google sheets API
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize((creds))
sheet = client.open("database").sheet1
data = sheet.get_all_values()

# reading data

# print(data)

# print(cell)
# print(row)
# pprint(data)
# inserting data sheet.delete / .update / .insert


# Web scrape https://www.ardmediathek.de/daserste/sendungen-a-bis-z
A_bis_Z = "https://www.ardmediathek.de/daserste/sendungen-a-bis-z/#Z"

html = requests.get(A_bis_Z).text
soup = BeautifulSoup(html, "html.parser")

# pprint(soup)
# "/html/body/div/div[2]/main/section/div[1]/div/div[1]/div/div/div/a/div/div[2]/h3"
entry = soup.find("body").find("div").find_all("div")[1].find("main")# .find("section")
entry = soup.find("section")



print(entry)

# sheet.update(entry)

# startup general ideas first attempt

# 1. Webscrape mediathek
# 2. Set up google sheet
# 3. Write and read from sheet with searches
# 4. Output search into something? maybe tkinter for starters


# webscraping mediathek data
# need whitelist to register for ARD API
SERIE = "x"
"/html/body/div/div[2]/main/section/div[1]/div/div[{SERIE}]".format(SERIE) # this div contains the show info
title = "/html/body/div/div[2]/main/section/div[1]/div/div[1]/div/div/div/a/div/div[2]/h3" # the text here is title of the show
link = "/html/body/div/div[2]/main/section/div[1]/div/div[1]/div/div/div/a"
img = "/html/body/div/div[2]/main/section/div[1]/div/div[1]/div/div/div/a/div/div[1]"

# dann auf der seite mehr, aber erstmal warten ob vlt einfacher mit api acess



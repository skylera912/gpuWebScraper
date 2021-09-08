import requests
import html2text as h
from bs4 import BeautifulSoup
import winsound

frequency = 1000
duration = 500 

url = "https://www.worldtimeserver.com/"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

check = soup.find('div').getText()

print(check)

# for i in range(len(rec)):
#     if rec[i] != "Out of Stock":
#         print("ALERT - POSSIBILY IN STOCK")
#         winsound.Beep(frequency, duration)







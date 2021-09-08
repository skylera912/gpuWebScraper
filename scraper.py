import requests
import html2text as h
from bs4 import BeautifulSoup
import winsound

frequency = 1000
duration = 500 

url = "https://www.nowinstock.net/computers/videocards/nvidia/rtx3060ti/"
url2 = "https://www.time.gov/"
page = requests.get(url)
page2 = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(page2.content, 'html.parser')


req = soup.find_all('td', class_ = "stockStatus")

req1 = soup.find_all('tr', id = "tr54493")
req2 = soup.find_all('tr', id = "tr54504")
req3 = soup.find_all('tr', id = "tr54494")
req4 = soup.find_all('tr', id = "tr54495")
req5 = soup.find_all('tr', id = "tr54501")
req6 = soup.find_all('tr', id = "tr54506")
req7 = soup.find_all('tr', id = "tr54508")
req8 = soup.find_all('tr', id = "tr54507")
req9 = soup.find_all('tr', id = "tr54505")
req10 = soup.find_all('tr', id = "tr54503")
req11 = soup.find_all('tr', id = "tr54502")
req12 = soup.find_all('tr', id = "tr54481")
req13 = soup.find_all('tr', id = "tr54867")
req14 = soup.find_all('tr', id = "tr54865")
req15 = soup.find_all('tr', id = "tr54518")
req16 = soup.find_all('tr', id = "tr54866")
req17 = soup.find_all('tr', id = "tr54518")
req18 = soup.find_all('tr', id = "tr54866")
req19 = soup.find_all('tr', id = "tr54518")


text_req0 = str(req[0])
text_req1 = str(req[1])
text_req2 = str(req[2])
text_req3 = str(req[3])
text_req4 = str(req[4])
text_req5 = str(req[5])
text_req6 = str(req[6])
text_req7 = str(req[7])
text_req8 = str(req[8])
text_req9 = str(req[9])
text_req10 = str(req[10])
text_req11 = str(req[11])
text_req12 = str(req[12])
text_req13 = str(req[13])
text_req14 = str(req[14])
text_req15 = str(req[15])
text_req16 = str(req[16])
text_req17 = str(req[17])
text_req18 = str(req[18])

text2_req0 = str(req1)
text2_req1 = str(req2)
text2_req2 = str(req3)
text2_req3 = str(req4)
text2_req4 = str(req5)
text2_req5 = str(req6)
text2_req6 = str(req7)
text2_req7 = str(req8)
text2_req8 = str(req9)
text2_req9 = str(req10)
text2_req10 = str(req11)
text2_req11 = str(req12)
text2_req12 = str(req13)
text2_req13 = str(req14)
text2_req14 = str(req15)
text2_req15 = str(req16)
text2_req16 = str(req17)
text2_req17 = str(req18)
text2_req18 = str(req19)

rec = [text_req0[39:51], text_req1[39:51], text_req2[39:51], text_req3[39:51], text_req4[39:51], text_req5[39:51], text_req6[39:51], text_req7[39:51], text_req8[39:51], text_req9[39:51], text_req10[39:51], text_req11[39:51], text_req12[39:51], text_req14[39:51]]

# print(text2_req0[243:277], " - ",  text_req0[39:51])
# print(text2_req1[229:261], " - ",  text_req1[39:51])
# print(text2_req2[243:288], " - ",  text_req2[39:51])
# print(text2_req3[229:268], " - ",  text_req3[39:51])
# print(text2_req4[243:288], " - ",  text_req4[39:51])
# print(text2_req5[229:268], " - ",  text_req5[39:51])
# print(text2_req6[243:279], " - ",  text_req6[39:51])
# print(text2_req7[229:269], " - ",  text_req7[39:51])
# print(text2_req8[243:286], " - ",  text_req8[39:51])
# print(text2_req9[229:268], " - ",  text_req9[39:51])
# print(text2_req10[243:281], " - ",  text_req10[39:51])
# print(text2_req11[359:392], " - ",  text_req11[39:51])
# print(text2_req12[243:280], " - ",  text_req12[39:51])
# print(text2_req14[522:549], " - ",  text_req14[39:51])

print(text2_req0[243:277], " - ", rec[0])
print(text2_req1[229:261], " - ",  rec[1])
print(text2_req2[243:288], " - ",  rec[2])
print(text2_req3[229:268], " - ",  rec[3])
print(text2_req4[243:288], " - ",  rec[4])
print(text2_req5[229:268], " - ",  rec[5])
print(text2_req6[243:279], " - ",  rec[6])
print(text2_req7[229:269], " - ", rec[7])
print(text2_req8[243:286], " - ",  rec[8])
print(text2_req9[229:268], " - ",  rec[9])
print(text2_req10[243:281], " - ",  rec[10])
print(text2_req11[359:392], " - ",  rec[11])
print(text2_req12[243:280], " - ",  rec[12])
print(text2_req14[522:549], " - ", rec[13])
i = 0

for i in range(len(rec)):
    if rec[i] != "Out of Stock":
        print("ALERT - POSSIBILY IN STOCK")
        winsound.Beep(frequency, duration)







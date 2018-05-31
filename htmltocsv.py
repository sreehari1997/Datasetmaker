import bs4 as bs
import urllib.request
import csv
import time

source = urllib.request.urlopen('http://139.59.68.161/realtime.html').read()
soup = bs.BeautifulSoup(source, 'lxml')


table = soup.table
t_r = table.find_all('tr')
for tr in t_r:
    td = tr.find_all('td')
    l=[]
    for j in td:
        l.append(j.text)
    #time.sleep(1)
    with open('data.csv', 'a') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(l)
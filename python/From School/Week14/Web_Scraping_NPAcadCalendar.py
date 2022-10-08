import requests
from bs4 import BeautifulSoup

session = requests.Session()
my_headers = {"User-Agent":'Mozilla/5.0'}
url = 'https://www.np.edu.sg/admissions/Pages/calendar.aspx'
response = session.get(url, headers=my_headers)
soup = BeautifulSoup(response.text, 'html.parser')
calendar_labels = soup.find_all('span', class_='cal-course')
calendar_periods = soup.find_all('span', class_='cal-time')
labels = []
periods = []

for s in calendar_labels:
    labels.append(s.text)
for s in calendar_periods:
    periods.append(s.text)

for i in range(len(labels)):
    if '2020' in periods[i]:
        print(periods[i])
        break
    print(f'{labels[i]:25s} {periods[i]}')
    

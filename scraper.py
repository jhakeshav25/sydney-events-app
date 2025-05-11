import json
from bs4 import BeautifulSoup
import requests

URL = "https://www.eventbrite.com.au/d/australia--sydney/events/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_with_bs4():
    events = []
    res = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(res.text, 'html.parser')
    for card in soup.select('.eds-event-card-content__content'):
        title_elem = card.select_one('div.eds-event-card-content__primary-content')
        link_elem = card.find('a', href=True)
        if title_elem and link_elem:
            events.append({
                'title': title_elem.text.strip(),
                'url': link_elem['href']
            })
    return events

def save_events(events):
    with open('events.json', 'w') as f:
        json.dump(events, f, indent=2)

if __name__ == '__main__':
    events = scrape_with_bs4()
    if not events:
        print("No events found using BeautifulSoup. Try using Selenium.")
    else:
        save_events(events)
        print("Scraped and saved using BeautifulSoup.")

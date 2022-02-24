from genericpath import exists
from sys import argv
import requests as req
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook

if len(argv) != 2:
    print()
    print("Usage: python main.py code")
    print()
    print('Get notified when Your timetable is updated!')
    print('You can find code in Your timetable\'s URL')
    print("https://planzajec.eaiib.agh.edu.pl/view/timetable/<code>")
    print()
    exit(1)

res = req.get(f'https://planzajec.eaiib.agh.edu.pl/view/timetable/{argv[1]}', verify=False)

webhook_urls = [
    # place Your Discord webhooks URL here
]
webhook = DiscordWebhook(url=webhook_urls, rate_limit_retry=True, content='Zaktualizowano plan!')

if not exists('updated_at'):
    f = open('updated_at', 'x')
    f.close()

if res.ok:
    soup = BeautifulSoup(res.text, 'html.parser')
    f = open('updated_at')
    old_date = f.read()
    f.close()
    new_date = soup.find('small').text.split(": ", 1)[1]
    if new_date != old_date:
        webhook.execute()
        f = open('updated_at', 'w')
        f.write(new_date)
        f.close()

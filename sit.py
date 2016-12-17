#!/usr/bin/env python
from lxml import html
import requests
import datetime
from gi.repository import Notify

ukedag = datetime.datetime.today().weekday()



def main():
    page = requests.get('https://www.sit.no/middag/elgeseter')
    tree = html.fromstring(page.content)
    sit = tree.xpath('//li[@class="dishes__dishes__dish dishes__dishes__dish--old-day"]/text()')
    
    sit = [s.strip() for s in sit]
    
    Notify.init ("sit-notice")
    
    if ukedag == 0:
        lunsjMessage = ("Dagens lunsj: {} og {}.".format(sit[0], sit[2]))
    elif ukedag == 1:
        lunsjMessage = ("Dagens lunsj: {} og {}.".format(sit[4], sit[6]))
    elif ukedag == 2:
        lunsjMessage = ("Dagens lunsj: {} og {}.".format(si[8], sit[10]))
    elif ukedag == 3:
        lunsjMessage = ("Dagens lunsj: {} og {}.".format(sit[12], sit[14]))
    elif ukedag == 4:
        lunsjMessage = ("Dagens lunsj: {} og {}.".format(sit[16], sit[18]))
    else:
        lunchMessage = "Ingen lunsj idag."

    Hello=Notify.Notification.new ("test")
    Hello.show ()

if __name__ == "__main__":
    main()

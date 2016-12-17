#!/usr/bin/env python
from lxml import html
import requests
import datetime
from gi.repository import Notify
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

ukedag = datetime.datetime.today().weekday()


def main():
    page = requests.get('https://www.sit.no/middag/elgeseter')
    tree = html.fromstring(page.content)
    sit = tree.xpath('//li[@class="dishes__dishes__dish dishes__dishes__dish--old-day"]/text()')
    
    sit = [s.strip() for s in sit]
    
    Notify.init ("sit-notice")
    lunsjMessage = ""
    
    if ukedag == 0:
        lunsjMessage = "{} og {}.".format(sit[0], sit[2])
    elif ukedag == 1:
        lunsjMessage = "{} og {}.".format(sit[4], sit[6])
    elif ukedag == 2:
        lunsjMessage = "{} og {}.".format(sit[8], sit[10])
    elif ukedag == 3:
        lunsjMessage = "{} og {}.".format(sit[12], sit[14])
    elif ukedag == 4:
        lunsjMessage = "{} og {}.".format(sit[16], sit[18])
    else:
        lunsjMessage = "Ingen lunsj idag."
    
    Hello=Notify.Notification.new ("Dagens Lunsj",
                                    lunsjMessage,
                                    )
    Hello.show ()

if __name__ == "__main__":
    main()

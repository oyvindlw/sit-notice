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
    sit = tree.xpath('//li[@class="dishes__dishes__dish dishes__dishes__dish--new-day"]/text()')
    
    sit = [s.strip() for s in sit]
    sit = list(filter(None, sit))

    Notify.init ("sit-notice")
    lunsjMessage = ""
    
    if ukedag == 0:
        lunsjMessage = "{} og {}.".format(sit[0], sit[1])
    elif ukedag == 1:
        lunsjMessage = "{} og {}.".format(sit[2], sit[3])
    elif ukedag == 2:
        lunsjMessage = "{} og {}.".format(sit[4], sit[5])
    elif ukedag == 3:
        lunsjMessage = "{} og {}.".format(sit[6], sit[7])
    elif ukedag == 4:
        lunsjMessage = "{} og {}.".format(sit[8], sit[9])
    else:
        lunsjMessage = "Ingen lunsj idag."
    
    Hello=Notify.Notification.new ("Dagens Lunsj",
                                    lunsjMessage,
                                    )
    Hello.show ()

if __name__ == "__main__":
    main()

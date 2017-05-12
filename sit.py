#!/usr/bin/env python
from lxml import html
import requests

from gi.repository import Notify

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    page = requests.get('https://www.sit.no/middag/elgeseter')
    tree = html.fromstring(page.content)
    sit = tree.xpath('//li[@class="dishes__dishes__dish dishes__dishes__dish--new-day"]/text()')
    
    sit = [s.strip() for s in sit]
    sit = list(filter(None, sit))

    Notify.init ("sit-notice")
    

    if sit: |
        lunsjMessage = "\n".join(str(x) for x in sit)
    else:
        lunsjMessage = "Ingen lunsj idag."

    Hello=Notify.Notification.new ("Dagens Lunsj",
                                    lunsjMessage,
                                    )
    Hello.show ()

if __name__ == "__main__":
    main()

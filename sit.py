#!/usr/bin/env python
from lxml import html
from gi.repository import Notify
import requests

def main():
    page = requests.get('https://www.sit.no/middag/elgeseter')
    tree = html.fromstring(page.content)
    sit = tree.xpath('//li[@class="dishes__dishes__dish dishes__dishes__dish--old-day"]/text()')
    
    sit = [s.strip() for s in sit]

    Notify.init ("Hello world")
    Hello=Notify.Notification.new ("Hello world",
                               "This is an example notification.",
                               "dialog-information")
    Hello.show ()

if __name__ == "__main__":
    main()

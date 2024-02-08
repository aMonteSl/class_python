#!/usr/bin/python3

import urllib.request

class Robot():
    def __init__(self, url):
        self.url = url

    def retrieve(self):
        endpoint = urllib.request.urlopen(self.url)
        data = endpoint.read().decode("utf-8")
        print(data)



if __name__ == "__name__":
    robot = Robot("https://cursosweb.github.io/programas/IT-ST.pdf")
    robot.retrieve()
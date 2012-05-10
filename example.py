#!/usr/bin/env python

from time import sleep

from loading import Loading


def main():

    loader = Loading(100, 'installing all the things.', '+')
    for count in range(1, 99):
        loader.complete(count)
        sleep(0.2)


    loader = Loading(100)
    loader.complete(10)
    sleep(1)
    loader.complete(20)
    sleep(1)
    loader.complete(30)
    sleep(1)
    loader.complete(40)
    sleep(1)
    loader.complete(50)
    sleep(1)
    loader.complete(60)
    sleep(1)
    loader.complete(70)
    sleep(1)
    loader.complete(80)
    sleep(1)
    loader.complete(90)
    sleep(1)





if __name__ == '__main__':
    exit(main())
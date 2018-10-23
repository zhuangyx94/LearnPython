# coding:utf8
# myapp.py
import logging
import mylib


def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Start')
    mylib.do_something()
    logging.info('Finished')


if __name__ == '__main__':
    main()












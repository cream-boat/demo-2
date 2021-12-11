
import logging


def tf():
    logging.basicConfig(filename='../logs/cols.log', level=logging.DEBUG, format='[%(asctime)s]-%(levelname)s-%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    mylist = [1, 2, 3]
    logging.critical('Starting to process `mylist`...')

def am():
    tf()

am()
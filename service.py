import csv
import sys

to_be_read = sys.argv[1]



def openFile(name):
    with open('source/{0}'.format(to_be_read), 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        items = {}

        for row in reader:
            items.push:wq
           item = {}


def breakdown(name):
    items = {}
    for row in name:
        item = {}
        print row.keys()

breakdown(openFile(to_be_read))
#openFile(to_be_read)        


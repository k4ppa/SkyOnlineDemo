import datetime
from datetime import timedelta

import stormtest.ClientAPI as StormTest


def goToSleep():
    with open("testStartingDate.txt","r") as dateFile:
        startingDate = dateFile.readlines()
        print startingDate
        
        splittedDate = splitDate(startingDate)
        startDate = datetime.datetime(int(splittedDate[0]), int(splittedDate[1]), int(splittedDate[2]), hour=int(splittedDate[3]), minute=int(splittedDate[4]))
        
        print 'startDate {0}'.format(startDate)
        print 'today {0}'.format(datetime.datetime.today())
        if (datetime.datetime.today() - startDate > timedelta(seconds=600)):
            StormTest.PressButton("LOCK:10")
            StormTest.WaitSec(15)
            StormTest.PressButton('SWIPE:1000:400:500:400')
            
            with open("testStartingDate.txt","w") as dateFile2:
                newStartDate = datetime.datetime.today()
                print "newStartDate"
                print newStartDate
                dateFile2.write(str(newStartDate))
                dateFile2.close()
            StormTest.WaitSec(3)
        dateFile.close() 


def splitDate(startingDate):
    splittedDate = startingDate[0].split(' ')
    date = splittedDate[0]
    hour = splittedDate[1]
    dateSplit = date.split('-')
    hourSplit = hour.split(':')
    print 'dateSplit {0}'.format(dateSplit)
    print 'hourSplit {0}'.format(hourSplit)
    del hourSplit[-1]
    
    return dateSplit + hourSplit 
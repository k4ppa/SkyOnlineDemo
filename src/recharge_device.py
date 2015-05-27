
import datetime
from datetime import timedelta


def rechargeDevice(device):
    startingDate = _readTestStartingDate()
    if (_oneDayIsPassed(startingDate)):
        _goToSleep(device, startingDate) 
        _writeNewTestStartingDate()
        

def _readTestStartingDate():
    startingDate = __readDate()
    splittedDate = __splitDate(startingDate)
    return datetime.datetime(int(splittedDate[0]), int(splittedDate[1]), int(splittedDate[2]), hour=int(splittedDate[3]), minute=int(splittedDate[4]))


def __readDate():
    with open("testStartingDate.txt","r") as dateFile:
        startingDate = dateFile.readlines()
    dateFile.close()
    return startingDate


def _oneDayIsPassed(startingDate):
    return datetime.datetime.today() - startingDate > timedelta(seconds=86400)


def __splitDate(startingDate):
    splittedDate = startingDate[0].split(' ')
    date = splittedDate[0]
    hour = splittedDate[1]
    dateSplit = date.split('-')
    hourSplit = hour.split(':')
    del hourSplit[-1]
    
    return dateSplit + hourSplit 


def _goToSleep(device, startDate):
    device.recharge(40) # 14400
    device.tap(text='Continua')
    #StormTest.WaitSec(3)
    pass
    

def _writeNewTestStartingDate():
    with open("testStartingDate.txt","w") as dateFile2:
        newStartDate = datetime.datetime.today()
        dateFile2.write(str(newStartDate))
        dateFile2.close()
    pass
    
    
    
    

import logging

import stormtest.ClientAPI as StormTest
import stormtest.WarningCenter as WarningCenter

log = logging.getLogger('connection')


def _getTestRunConfiguration():
    StormTest.BeginLogRegion('Open Connection')
    params = WarningCenter.GetTestRun()
    
    if params == None:     
        return __getDeveloperModeParams() 
    return params    


def __getDeveloperModeParams():
    from mobile_framework.tests.test_environment import TestEnvironment
    log.info("Developer mode - using a hard coded set of parameters")
    
    return TestEnvironment.params


def _setUpEnvironment():
    log.info("SetUp Environment")
    if not StormTest.IsUnderDaemon():
        return __setUpTestEnvironment()
    else:
        return __setUpRealEnvironment()
        

def __setUpTestEnvironment():
    from mobile_framework.tests.test_environment import TestEnvironment
    server = TestEnvironment.getServerName()
    slot = TestEnvironment.getSlotNumber()
    log.info("Test running under daemon, using test environment")
    
    return server, slot
    
    
def __setUpRealEnvironment():
    slotAllocated = StormTest.GetPhysicalAllocations()
    server = slotAllocated[0].split(':')[0]
    slot = slotAllocated[1][0]
    log.info("Test not running under daemon, using real environment")
    
    return server, slot


def _establishConnection(server, slot, description):
    isServerConnected = __openConnection(server, description)
    isSlotReserved = __reserveSlot(slot, signalDb='', serialParams=[], videoFlag=True)
    
    return __isConnectionOk(isServerConnected, isSlotReserved)
    

def __openConnection(server, description):
    try:
        log.info("Opening connection to server: '%s'" % server)
        StormTest.ConnectToServer(server, description)
    except SystemExit:
        log.error("Failed to connect to server")
        StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='Failed to connect to server (%s)' % server)
        return False
    
    log.info("Connection established with the server")
    return True


def __reserveSlot(slot, signalDb='', serialParams=[], videoFlag=True):
    log.info("Starting to reserve slot %d" % slot)
    isReserved = StormTest.ReserveSlot(slot, signalDb, serialParams, videoFlag)
    __logReserveSlotResult(slot, isReserved)
    
    return isReserved 
    
    
def __logReserveSlotResult(slot, isReserved):
    if isReserved is 0:    
        StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='Failed to reserve slot %d' % slot)
        log.error('Failed to reserve slot %d' % slot)
    else:
        log.info("Slot %d reserved" % slot)
    pass
    
    
def __isConnectionOk(isServerConnected, isSlotReserved):
    isConnectionOk = False
    if isServerConnected and isSlotReserved:
        isConnectionOk = __OCRCheckRemainingChars()
        
    log.info("Connection established and slot reserved") if isConnectionOk else log.info("Connection failed")
    if isConnectionOk:
        log.info("Connection established and slot reserved")
        StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Pass, comment='Connection with the server established')
    else:
        log.error("Connection failed")
         
    return isConnectionOk    
    

def __OCRCheckRemainingChars():
    remainingChars = StormTest.OCRGetRemainingChars()
    __logRemainingCharsResult(remainingChars)
    
    return True if remainingChars else False


def __logRemainingCharsResult(remainingChars):
    log.info("Remaining OCR chars in license: %d" % remainingChars)
    if remainingChars is 0:    
        StormTest.EndLogRegion('Open Connection', StormTest.LogRegionStyle.Fail, comment='OCR licenses has ran out. Not possible to run tests')
        log.error("OCR licenses has ran out. Not possible to run tests")
    pass


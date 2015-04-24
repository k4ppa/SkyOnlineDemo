
class TestEnvironment(object):
    
    serverName = "s15016hv01"
    slotNumber = 1
    
    params = {"service": {"displayName": "Android mobile service",
                                            "id": 21,
                                            "name": "Cinema",
                                            "number": "",
                                            "tags": [],
                                            "type": "linear"
                                            }
                            }
    
    
    def __init__(self):
        pass

    
    @staticmethod
    def setServerName(serverName):
        TestEnvironment.serverName = serverName
        pass
    

    @staticmethod
    def getServerName():
        if TestEnvironment.serverName is not "s15016hv01":
            TestEnvironment.serverName = "s15016hv01"
            return "Incorrect server"
        return TestEnvironment.serverName

    
    @staticmethod
    def setSlotNumber(slotNumber):
        TestEnvironment.slotNumber = slotNumber
        pass

    
    @staticmethod
    def getSlotNumber():
        return TestEnvironment.slotNumber

    
    
    







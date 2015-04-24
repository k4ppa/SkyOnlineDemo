
import stormtest.ClientAPI as StormTest


def goToCatalog(device, catalog):
    appCommands = device.getAppCommands()
    
    appCommands.openMenu()
    
    device.tap(text=catalog)
    pass

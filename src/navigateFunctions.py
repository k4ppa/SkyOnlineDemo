

def goToCatalog(device, catalogName):
    appCommands = device.getAppCommands()
    
    appCommands.openMenu()
    result, comment, image = appCommands.openCatalog(catalogName)
    return result, comment, image

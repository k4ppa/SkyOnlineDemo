
import logging

import stormtest.ClientAPI as StormTest
import importlib


log = logging.getLogger('userAction')

def _loadDeviceCommands(moduleName):
    deviceModule = __importDeviceModule(moduleName)
    return deviceModule.DeviceCommands()


def __importDeviceModule(deviceCommandsModule):
    try:
        return importlib.import_module(deviceCommandsModule + ".device_commands")
    except ImportError:
        log.error("Fail to import device mapped commands: {0}".format(deviceCommandsModule))
        raise 
    

def _loadAppCommands(self, appName, deviceModuleName):
    appModuleName = __concatModulesName(appName, deviceModuleName)
    appCommandsModule = __importAppModule(appModuleName)
    
    return appCommandsModule.AppCommands(self)


def __concatModulesName(appName, deviceCommandsModule):
    moduleName = appName.replace(".", "_")
    return deviceCommandsModule + ".{0}_commands".format(moduleName)
    

def __importAppModule(deviceCommandsModule):
    try:
        return importlib.import_module(deviceCommandsModule)
    except ImportError:
        log.error("Fail to import app mapped commands: {0}".format(deviceCommandsModule))
        raise


def _tapWithMappedText(commands, mappedText):
    log.info("Tap on mapped text {0} {1}".format(mappedText, commands[mappedText]))
    
    command = commands[mappedText]
    return StormTest.PressButton('TAP:{0}:{1}:{2}'.format(command['x'], command['y'], command['time']))





    
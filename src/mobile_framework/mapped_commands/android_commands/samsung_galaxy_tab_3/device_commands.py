
from mobile_framework.mapped_commands.android_commands.android_commands import AndroidCommands


class DeviceCommands(AndroidCommands):

    def __init__(self):
        AndroidCommands.__init__(self)
        
        self._commands = {'OpenAssistantMenu':{'x':1230, 'y':435, 'time':0},
                         'CloseAssistantMenu':{'x':1270, 'y':450, 'time':0},
                         'DeviceMenu':{'x':1000, 'y':390, 'time':0},
                         'DeviceHome':{'x':990, 'y':520, 'time':0},
                         'Back':{'x':1125, 'y':515, 'time':0},
                         'Up':{'x':1225, 'y':360, 'time':0},
                         'Down':{'x':1225, 'y':535, 'time':0},
                         'DeviceSettings':{'x':1125, 'y':515, 'time':0},
                         
                         'a': {'x':110, 'y':610, 'time':0},
                         'b': {'x':625, 'y':680, 'time':0},
                         'c': {'x':400, 'y':680, 'time':0},
                         'd': {'x':340, 'y':610, 'time':0},
                         'e': {'x':285, 'y':530, 'time':0},
                         'f': {'x':450, 'y':610, 'time':0},
                         'g': {'x':565, 'y':610, 'time':0},
                         'h': {'x':675, 'y':610, 'time':0},
                         'i': {'x':850, 'y':530, 'time':0},
                         'l': {'x':1015, 'y':610, 'time':0},
                         'm': {'x':850, 'y':680, 'time':0},
                         'n': {'x':735, 'y':680, 'time':0},
                         'o': {'x':960, 'y':530, 'time':0},
                         'p': {'x':1075, 'y':530, 'time':0},
                         'q': {'x':60, 'y':530, 'time':0},
                         'r': {'x':400, 'y':530, 'time':0},
                         's': {'x':220, 'y':610, 'time':0},
                         't': {'x':510, 'y':530, 'time':0},
                         'u': {'x':740, 'y':530, 'time':0},
                         'v': {'x':510, 'y':680, 'time':0},
                         'z': {'x':170, 'y':680, 'time':0},
                         'w': {'x':170, 'y':530, 'time':0},
                         'y': {'x':625, 'y':530, 'time':0},
                         'j': {'x':790, 'y':610, 'time':0},
                         'k': {'x':900, 'y':610, 'time':0},
                         'x': {'x':290, 'y':680, 'time':0},
                        
                         '0': {'x':1210, 'y':460, 'time':0},
                         '1': {'x':65, 'y':460, 'time':0},
                         '2': {'x':195, 'y':460, 'time':0},
                         '3': {'x':320, 'y':460, 'time':0},
                         '4': {'x':450, 'y':460, 'time':0},
                         '5': {'x':570, 'y':460, 'time':0},
                         '6': {'x':700, 'y':460, 'time':0},
                         '7': {'x':830, 'y':460, 'time':0},
                         '8': {'x':960, 'y':460, 'time':0},
                         '9': {'x':1080, 'y':460, 'time':0},
                         
                         '@': {'x':110, 'y':600, 'time':0},
                        
                         'Find': {'x':1170, 'y':600, 'time':0},
                         'Shift': {'x':60, 'y':680, 'time':0},
                         'Sym': {'x':60, 'y':755, 'time':0},
                         ' ': {'x':630, 'y':750, 'time':0},
                         '.': {'x':1070, 'y':680, 'time':0}
                         }
        pass
    
    
    def getCommands(self):
        return self._commands  
    
    
from config import QTWSConfig

class QTWSPlugin:
    def __init__(self, name):
        self.name = name
        
    def webEngineSetup(self, web):
        pass
        
    def onWindowCreated(self):
        pass
    
    def onActionClicked(self):
        pass
    
    def onPageLoaded(self):
        pass
    
    def addMenuItems(self, menu):
        pass
    
    def isURLBlacklisted(self, url):
        return False
    
    def isURLWhitelisted(self, url):
        return False
        
class QTWSPluginManager:
    __instance = None
    
    def instance():
        if not QTWSPluginManager.__instance:
            QTWSPluginManager.__instance = QTWSPluginManager()
            
        return QTWSPluginManager.__instance
        
    def loadPlugins(self, config):
        self.plugins = list()
        for pluginInfo in config.plugins:
            pluginModule = __import__('plugin.' + pluginInfo.name, globals(), locals(), [pluginInfo.name])
            pluginInstance = pluginModule.instance(pluginInfo.params)
            self.plugins.append(pluginInstance)
            
    def forEach(self, action):
        for plugin in self.plugins:
            action(plugin)

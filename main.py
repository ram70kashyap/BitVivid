import os
import importlib

class Arch():
    """This is basiscs file for the class, framework test"""

    def __init__(self,dir, filename):
        self.filename = filename
        self.dir = dir
        self.filePath = None

    def setPath(self):
        self.filePath = os.path.join(os.getcwd(), self.dir)
        return self.filePath
    
    def getDirList(self):
        self.pathDir = self.setPath()
        self.moduleList = [i for i in os.listdir(self.pathDir) if i[-3:] == ".py" if i != "__init__.py"]
        return self.moduleList

    def importModule(self):
        self.moduleList = self.getDirList()
        os.chdir(self.dir)
        for name in self.moduleList:
            self.ModName = name[:-3]
            # globals()[name[-3:]] = __import__(os.path.join(os.getcwd(),name), locals())
            # importlib.import_module(f"{os.getcwd()}\\{name}")
            break

        
if __name__ == "__main__":
    arch = Arch("Modules","Module.py")
    arch.importModule()
    # arch.importModule()
# os.chdir(os.path.join(os.getcwd(), "Modules"))
# print(os.getcwd())

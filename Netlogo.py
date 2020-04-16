import nl4py
import csv
import json
import collections
#'Models\BicicletasUD.nlogo'
#worksp = nl4py.newNetLogoHeadlessWorkspace() # create NetLogo HeadlessWorkspaces from Python using the netLogoWorkspaceFactory

def startServer(self):
    nl4py.startServer('E:\Juan\Programs') # top level directory of your NetLogo installation

def stopServer(self):
    nl4py.stopServer()

def netlogoCommand(self, command):
    worksp.command(command)

def openModel(self, path_model):
    worksp.openModel(path_model)

def closeModel(self):
    worksp.dispose()

def loadDataWord(path_csv):
    data = {}
    with open(path_csv) as csvFile:
        csvReader = csv.reader(csvFile)
        i=0
        for rows in csvReader:
            if i<12:
                if (rows):
                    print(rows[1])
            i=i+1
#nl4py.NetLogoApp() # open the NetLogo application in GUI 

#worksp.scheduleReportersAndRun(reporters_array, startAtTick=0, intervalTicks=1, stopAtTick=-1, goCommand="go")
#worksp.closeModel()
#
#worksp.report(netlogo_command_string)
#worksp.getScheduledReporterResults() # non-blocking and returns nothing if the simulation is not finished
#worksp.awaitScheduledReporterResults() # blocking and returns only after the simulation has finished
#worksp.setParamsRandom()
#worksp.getParamNames()
#worksp.getParamRanges()
loadDataWord('Models\Data\word.csv')
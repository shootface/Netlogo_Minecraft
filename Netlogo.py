import nl4py
import csv
import json
import collections
import pandas as pd
import numpy as np
import os
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

def loadDataWord(load_csv_path, save_csv_path):
    data = {}
    with open(load_csv_path) as csvFile:
        csvReader = csv.reader(csvFile)
        in_section = False
        file_name = ""
        for row in csvReader:
            try:
                if(in_section):
                    if(len(row)!=0):
                        if( 'pxcor' in row[0] or 'who' in row[0] ):
                            zeros = np.zeros([1,len(row)])
                            df_columns = row
                            df = pd.DataFrame(zeros, columns=row)
                        else:
                            temp_df = pd.DataFrame([row], columns=df_columns)
                            df = pd.concat([df, temp_df], ignore_index=True)
                    else:
                        save_csv = os.path.join(save_csv_path, '{}.csv'.format(file_name))
                        df = df.drop(0)
                        df.to_csv(save_csv, index=False)
                        in_section = False
                        print('creado csv {} en la ruta {}'.format(file_name, save_csv))
                if('TURTLES' in row[0] or 'PATCHES' in row[0]):
                    file_name = row[0]
                    in_section = True
            except:
                print('elemento vacio')
            
          




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
BASE_PATH = os.getcwd()

LOAD_CSV_PATH = os.path.join(BASE_PATH, 'Models', 'Data', 'word.csv')
SAVE_CSV_PATH = os.path.join(BASE_PATH, 'Models', 'Data')

loadDataWord(LOAD_CSV_PATH, SAVE_CSV_PATH)
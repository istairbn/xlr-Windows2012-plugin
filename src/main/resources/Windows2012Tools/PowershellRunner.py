#################################################################################################
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
###################################################################################################

import sys, os, zipfile
from com.xebialabs.deployit.plugin.api.reflect import Type

def createPowershellTask(phaseId,title,precondition, propertyMap):

    parenttaskType = Type.valueOf("xlrelease.CustomScriptTask")
    parentTask = parenttaskType.descriptor.newInstance("nonamerequired")
    parentTask.setTitle(title)

    childTaskType = Type.valueOf("remoteScript.Powershell")
    childTask = childTaskType.descriptor.newInstance("nonamerequired")
    for item in propertyMap:
        childTask.setProperty(item,propertyMap[item])
    parentTask.setPythonScript(childTask)
    parentTask.setPrecondition(precondition)
    taskApi.addTask(phaseId,parentTask)


def createParallelTask(phaseId,title,precondition,propertyMap):
    paralleltaskType = Type.valueOf("xlrelease.ParallelGroup")
    parallelTask = paralleltaskType.descriptor.newInstance("nonamerequired")
    parallelTask.setTitle(title)
    parallelTask.setPrecondition(precondition)
    taskApi.addTask(phaseId,parallelTask)
    return parallelTask.id

mynewtask = createParallelTask(phase.id,task.title,None,{})
serversSplit = servers.split(",")
stringToAdd = ""

if len(valuesDict) > 0:
    for argument in valuesDict:
        stringToAdd = stringToAdd + " -" + argument + " " + '"' +  eval(argument) + '"'

pathtojar = os.getcwd()+"/plugins/xlr-Windows2012-plugin-1.0.2.jar"
archive = zipfile.ZipFile(pathtojar, 'r')
script = archive.read(PSscriptLocation)
script = script + stringToAdd

for elem in serversSplit:
    createPowershellTask(mynewtask,elem,None,{'address':elem,'script':script,'remotePath':remotePath,'port':port,'username':username,'password':password,'connectionType':connectionType,'winrmEnableHttps':winrmEnableHttps})

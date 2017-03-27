#################################################################################################
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
###################################################################################################

import subprocess,time
shell = 'C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe'
pShellArray = "@('"+ "','".join(servers) + "')"
serverString = ",".join(servers)

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

restartCommand = "Restart-Computer %s -Force -Wait -For PowerShell -Timeout -1 -Delay 3 -WsmanAuthentication Kerberos ;Write-Output 'Initial Return'" % serverString

secondCheck = """;
ForEach($Server in $Servers){
    $Ready = $False
    While(!$Ready){
        $Services = @()
        $Services += gwmi -Class Win32_Service -ComputerName eurv192d03 | Where name -eq winRM | Where State -eq running
        $Services += gwmi -Class Win32_Service -ComputerName eurv192d03 | Where name -match LanMan | Where State -eq running

        If($Services.count -eq 3){
            Write-Output "Ready"
            $Ready = $True
        }
        Else{
            Sleep 10
        }
    }
}"""

checkCommand = "$Servers =" + pShellArray + secondCheck

phase = getCurrentPhase()
task = getCurrentTask()

createPowershellTask(phase.id, task.title + " - Reboots", None, {'address':address,'script':restartCommand,'remotePath':remotePath,'port':port,'username':username,'password':password,'connectionType':connectionType,'winrmEnableHttps':winrmEnableHttps,'winrsAllowDelegate':winrsAllowDelegate})

createPowershellTask(phase.id, task.title + " - Confirmation", None, {'address':address,'script':checkCommand,'remotePath':remotePath,'port':port,'username':username,'password':password,'connectionType':connectionType,'winrmEnableHttps':winrmEnableHttps,'winrsAllowDelegate':winrsAllowDelegate})
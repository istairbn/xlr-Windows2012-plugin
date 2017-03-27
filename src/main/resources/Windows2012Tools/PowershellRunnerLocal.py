#################################################################################################
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
###################################################################################################

import sys, os, zipfile,subprocess

pathtojar = os.getcwd()+"/plugins/xlr-Windows2012-plugin-1.0.2.jar"
archive = zipfile.ZipFile(pathtojar, 'r')
script = archive.read(PSscriptLocation)
if valuesDict:
    for argument in valuesDict:
        stringToAdd = stringToAdd + " -" + argument + " " + '"' +  eval(argument) + '"'
        command = script + stringToAdd
else:
    command = script
    
shell = 'C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe'

output = subprocess.check_output([shell,script])
print(output)
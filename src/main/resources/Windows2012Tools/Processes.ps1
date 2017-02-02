Function XLR-Processes{

[CmdletBinding(SupportsShouldProcess=$True)]
Param(
[parameter(Mandatory=$true)]
[String]
$ProcessName,

[parameter(Mandatory=$False)]
[boolean]
$throwOnError = $True

)

ForEach($Process in $ProcessName.Split(",")){
        
        If($a = Get-Process -Name $Process -ErrorAction SilentlyContinue){
        $a | Stop-Process -Force
        }

        Elseif($throwOnError){
        Write-Error "$Process doesn't exist"
        }
    }

}

XLR-Processes
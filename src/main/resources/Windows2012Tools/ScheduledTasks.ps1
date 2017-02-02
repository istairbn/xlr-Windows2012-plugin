Function XLR-SchTask{

[CmdletBinding(SupportsShouldProcess=$True)]
Param(
[parameter(Mandatory=$true)]
[String]
$TaskName, 

<#[parameter(Mandatory=$true)]
[ValidateSet("Stopped","Running")]
[String]
$Status,#>

[parameter(Mandatory=$true)]
[ValidateSet("Enabled", "Disabled")]
[String]
$State,

[parameter(Mandatory=$False)]
[boolean]
$throwOnError = $True
)

ForEach($Task in $TaskName.Split(",")){
    
    If($a = Get-ScheduledTask -TaskName $Task -ErrorAction SilentlyContinue){      
        If($State -eq "Enabled"){
            $a | Enable-ScheduledTask
            }
        
        Else{
            $a | Disable-ScheduledTask
            }
        }

    Else{
        Write-Error "$Task doesn't exist"
        }
    }

}

XLR-SchTask
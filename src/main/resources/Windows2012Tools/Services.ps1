Function XLR-Service{

[CmdletBinding(SupportsShouldProcess=$True)]
Param(
[parameter(Mandatory=$true)]
[String]
$DisplayName, 

[parameter(Mandatory=$true)]
[ValidateSet("Paused", "Stopped","Running")]
[String]
$Status,

[parameter(Mandatory=$true)]
[ValidateSet("Automatic", "Manual", "Disabled")]
[String]
$StartupType,

[parameter(Mandatory=$False)]
[boolean]
$throwOnError = $True
)

ForEach($Service in $DisplayName.Split(",")){
        
        If($a = Get-Service -DisplayName $Service -ErrorAction SilentlyContinue){
        $a | Set-Service -StartupType $StartupType -Status $Status
        }

    Elseif($throwOnError){
        Write-Error "$DisplayName doesn't exist"
        }
    }
}

XLR-Service
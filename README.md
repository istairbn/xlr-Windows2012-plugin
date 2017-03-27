# xlr-windows2012-plugin
An XL Release plugin to perform Windows Server 2012 tasks across multiple machines

See the **[XL Release Documentation](https://docs.xebialabs.com/xl-release/index.html)** for background information on XL Release and release concepts.

## Installation #
Place the latest released version under the `plugins` dir. If needed append the following to the `script.policy` under `conf`:```permission java.io.FilePermission "plugins/*", "read";permission java.io.FilePermission "conf/logback.xml", "read";```This plugin requires XLR 6.1+

## Types ##

All of these take a list of servers. Once the task runs, it will generate a parallel group of PowerShell tasks to run the appropriate actions. For this reason, these tasks must be located at the end of a Phase. 

+ Processes
  *  Stops processes
  * `Process Name`: Name of process to stop, comma separate for multiple processes. Wildcard supported. For example: notepa*,explorer

+ Scheduled Tasks
  *  Enables/Disables scheduled tasks
  * `Task Name`: Name of Scheduled Task to change, comma separate for multiple processes. Wildcard supported. For example: notepa*,explorer
  * `State`: Enabled,Disabled

+ Services
  * Changes the state and start-up type of services. 
  * `Task Name`: Name of Service to change, comma separate for multiple processes. Wildcard supported. For example: IIS,win*
  * `Startup Type`: Disabled, Manual, Automatic
  * `Status`: Paused,Running,Stopped
  
+ Reboot Servers
  * Restarts the server. Requires an intermediate host to run from. 
  * `Servers`: List of servers  
  * `Username`: Username to login with
  * `Password`: Password for Username
  * `Remote Path`: Where the script should run
  * `Port`: Port to connect with
  * `Connection Type`: How to connect - see overthere documentation for more detail
  
+ Generic Arguments (sourced from PowerShell Task)
  * `Servers`: Comma Separated list of servers  
  * `Username`: Username to login with
  * `Password`: Password for Username
  * `Remote Path`: Where the script should run
  * `Port`: Port to connect with
  * `Connection Type`: How to connect - see overthere documentation for more detail

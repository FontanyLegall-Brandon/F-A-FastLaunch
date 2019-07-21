##############################################################
## FAST LAUNCH          
##############################################################
##
## Author : =F|A= Scarface    
## Licence : MIT              
##                            
##############################################################
## CONFIGURATION         
##############################################################

servers = {"jay1":"jay1.clan-fa.com:27960",
           "jay2":"jay2.clan-fa.com:27960",
           "b1":"jay3.clan-fa.com",
           "b2":"b2.clan-fa.com:27960",
           "silent1":"silent1.clan-fa.com:27960",
           "hc":"hc.clan-fa.com:27960",
           "nq1":"nq1.clan-fa.com:27960",
           "nq2":"nq2.clan-fa.com:27960",
           "nq3":"nq3.clan-fa.com:27960",
           "fun1":"fun1.clan-fa.com:27960",
           "fun2":"fun2.clan-fa.com:27960",
           "etl1":"etl1.clan-fa.com:27950"}

          
# Please insert into the toLaunch table the servers that you want to launch
toLaunch = ["jay1"]

# To launch all, use this above :
#toLaunch = [key for key in servers.keys()]

##############################################################
## Script            
##############################################################

import subprocess
program='C:\Program Files (x86)\Wolfenstein - Enemy Territory\ET.exe'

for server in toLaunch :
    if server in servers.keys():
        arguments={"+connect "+servers[server]}
        subprocess.call([program, arguments])

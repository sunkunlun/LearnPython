#!/usr/bin/env python
import os
import re
from _ast import Or
from platform import node

debug_mode=1

def GetOutPut(sCommand):
    if debug_mode == 1:
        fd=open(os.path.join(os.getcwd(),sCommand),'r')
        result=fd.read()
        fd.close()
        return result
    else:
        return os.popen(sCommand).read()

def GetHostList():
    hostdir={}
    cmd=""
    if debug_mode == 1:
        cmd="nova_list.txt"
    else:
        cmd="os.popen(\"nova list --all-t |grep -v '\--'| cut -d'|' -f2,3\").read().split(\"|\")"
    
    templist=GetOutPut(cmd)
    
    allhost=[]
    for onenode in templist.split(' '):
        if len(onenode)<1 or onenode.count('ID')>0 or onenode.count('Name')>0 or onenode.count('|')>0:
            continue
        else:
            allhost.append(onenode)
    #print(allhost)
    
    for i in range(0,len(allhost),2):
        hostdir[allhost[i+1].strip('\n')]=allhost[i]
    
    return hostdir
 
    

def GetVirHostInfo():
    pass

if __name__ == '__main__':
    GetHostList()
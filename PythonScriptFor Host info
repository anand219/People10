#!/usr/bin/python
import sys
import os
sys.path.append("/opt/opsware/pylibs2")
from pytwist import *
from pytwist.com.opsware.server import *
from pytwist.com.opsware.search import *
from pytwist.com.opsware.storage import *
from pytwist.com.opsware.locality import *
#-------------------------------------------------------------
#Function to get the Server's memory statistics
#------------------------------------------------------------
def get_server_Mem(serverService,serverRef,writeTofile):
        try:

                serverMems = serverService.getServerHardwareVO(serverRef)
                memory = serverMems.memories
                for mem in memory:
                        x = mem.quantity
                        capacity = long(float(x))
                        type(capacity)
                        if mem.type == 'RAM':
                         writeTofile.write(',%s' %(capacity/1024/1024))
                        #print type(mem.quantity)
		writeTofile.write(',')
        except:
                #writeTofile.write('unexpected error\r\n')
                return

#----------------------------------------------------------------
#Function to get the Server's disk statistics
#----------------------------------------------------------------
def get_disk_size(serverService,serverRef,diskService,writeTofile):
        try:
                disks = serverService.getPhysicalDisks(serverRef)
                for disk in disks:
                	diskVO = diskService.getPhysicalDiskVO(disk)
                        #if diskVO.media == "SCSI DISK" or "DISK" :
                      	writeTofile.write("%s:-%s " %(disk.name,diskVO.storageCapacity/1024/1024/1024))
                writeTofile.write(',')

        except:
                #writeTofile.write('unexpected error\r\n')
                return

#---------------------------------------------------------------------------------------------
#Function to get the Server's information i.e Hostname, IP, Customer, Facility, Model etc
#---------------------------------------------------------------------------------------------
def get_server_info(serverService,facilityService,customerService,serverRef,platformService,writeTofile):
        try:
                serverVO = serverService.getServerVO(serverRef)
                platform = platformService.getPlatformVO(serverVO.platform)
                serverOS = platform.displayName
                facilityVO = facilityService.getFacilityVO(serverVO.facility)
                customerVO = customerService.getCustomerVO(serverVO.customer)
                writeTofile.write("%s,%s,%s,%s,%s,%s,%s" %(customerVO.displayName, serverVO.use, serverVO.description,serverVO.name, serverVO.hostName,serverVO.primaryIP, serverOS))
        except:
                #writeTofile.write('unexpected error\r\n')
                return

#---------------------------------------------------------------------------------------------
#Function to get the Server's information i.e Hostname, IP, Customer, Facility, Model etc
#---------------------------------------------------------------------------------------------
def get_server_info2(serverService,facilityService,customerService,serverRef,platformService,writeTofile):
        try:
                serverVO = serverService.getServerVO(serverRef)
                platform = platformService.getPlatformVO(serverVO.platform)
                serverOS = platform.displayName
                facilityVO = facilityService.getFacilityVO(serverVO.facility)
                customerVO = customerService.getCustomerVO(serverVO.customer)
                writeTofile.write("%s,%s" %(facilityVO.name, serverVO.model))
                writeTofile.write(',')
        except:
                #writeTofile.write('unexpected error\r\n')
                return

#----------------------------------------------------------------------

#----------------------------------------------------------------------
#Function to get the Server's CPU information
#-----------------------------------------------------------------------
def get_cpu_info(serverService,serverRef,writeTofile):
        try:
                serverCPUs = serverService.getServerHardwareVO(serverRef)
                cpus = serverCPUs.cpus
                writeTofile.write(",%s" %(len(cpus)))
                #writeTofile.write('----------------------------------------------------------------------\r\n') 
                #for cpu in cpus:
                        #writeTofile.write("cpuModel:%s; Phy Core/CPU:%s"%(cpu.model, cpu.physicalCoresCount))
                        #writeTofile.write('Physical Core/s per CPU = %s\r\n'%(cpu.physicalCoresCount)) 
                        #writeTofile.write('----------------------------------------------------------------------\r\n') 
                #writeTofile.write(',')
        except:
                #writeTofile.write('unexpected error\r\n')
                return

#----------------------------------------------------------------------
#Function to get the Server's Network slots and their respective ip's
#-----------------------------------------------------------------------
def get_interface_slot(serverService,serverRef,writeTofile):
        try:
                interface = serverService.getServerHardwareVO(serverRef)
                ethernet = interface.interfaces
                for ether in ethernet:
		 #writeTofile.write("Ethernet Type = %s -----> Ethernet slot = %s -----> Ethernet ip address = %s ----> Ethernet speed = %s"%(ether.type,ether.slot,ether.ipAddress,ether.speed))
                 if ether.type == 'ETHERNET':
		  writeTofile.write("%s:-%s  "%(ether.slot,ether.ipAddress))
                writeTofile.write(',')
        except:
                #writeTofile.write('unexpected error\r\n')
                return

#-------------------------------------------------------------------------------------------------------
#Main function where all pytwist related objects are defined and each specific function are being called
#-------------------------------------------------------------------------------------------------------
def main():
        # Create the TwistServer object
        ts = twistserver.TwistServer()
        
        #Create the output file which will be generated after script execution
        file_name = 'get_server_info.csv'

        #opening file 'get_server_info.txt' in write mode
        writeTofile = open(file_name,'w')

        serverService = ts.server.ServerService
        platformService = ts.device.PlatformService
        diskService = ts.storage.PhysicalDiskService
        facilityService = ts.locality.FacilityService
        customerService = ts.locality.CustomerService

        # Construct a search filter and provided expression to target the servers within matched Customer
        filter = Filter()
        #filter.expression = '(device_customer_displayname CONTAINS "OSS Tools")'
        filter.expression = '(device_group_id EQUAL_TO "462780102")'
        serverRefs = serverService.findServerRefs(filter) 
	#writeTofile.write("Hostname,ManamentIP,Facility,Customer,Agent Staus,OS,Model,SNO,Object ID,Memory(GB),Disk statistics(GB),CPU,NIC Details\r\n")
        writeTofile.write("Customer,Server use (Environment),Description (Business application name),Name,Hostname,IP,OS,CPU,Memory (GB),Disk Statistics,Facility,Model\r\n")
        for serverRef in serverRefs:

                # Calling each specific function
                get_server_info(serverService,facilityService,customerService,serverRef,platformService,writeTofile)
                get_cpu_info(serverService,serverRef,writeTofile)
                get_server_Mem(serverService,serverRef,writeTofile)
                get_disk_size(serverService,serverRef,diskService,writeTofile)
                get_server_info2(serverService,facilityService,customerService,serverRef,platformService,writeTofile)
                #get_interface_slot(serverService,serverRef,writeTofile)
                writeTofile.write('\r\n')

if __name__ == "__main__":
        main()

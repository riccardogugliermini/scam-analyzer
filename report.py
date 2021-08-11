from sys import argv
import os
import virtualbox
import filecmp
import sys
import config 

VM_NAME = "test"

class Machine:
	vbox = virtualbox.VirtualBox()
	session = virtualbox.Session()

	def __init__(self):
		#Lookup for the virtual machine, if not found terminates
		#try:
		#	self.vm = self.vbox.find_machine("test")
		#except virtualbox.library.VBoxErrorObjectNotFound :
		#	print("Machine not found")
		#	sys.exit(1) 
		script, self.hdd_uuid, self.snap_uuid  = argv

	def mountVDIs(self):
		#for m in self.vm.medium_attachments:
		#	if m.type_p == virtualbox.library.DeviceType.hard_disk:
		#		self.hdd_uuid = m.medium.id_p
				
		os.system("sudo echo user_allow_other >> /etc/fuse.conf ")
		#os.system("mkdir hd-mount/")
		#os.system("vboximg-mount -i "+self.hdd_uuid+" -o allow_root hd-mount")
		#os.system("mkdir snap-mount/")
		#os.system("vboximg-mount -i "+self.snap_uuid+" -o allow_root snap-mount")
		#os.system("mkdir /mnt/hdd")
		#os.system("mkdir /mnt/snap")
		os.system("sudo mount " + HDD_PATH + "/vhdd " + HDD_MOUNT)
		os.system("sudo mount " + SNAP_PATH + "/vhdd " + SNAP_MOUNT)
	
	def compare(self, dircmp, dirName):
		print("------ "+dirName+" ------")
		print("Different files in "+dirName)
		for f in dircmp.diff_files:
			print("\t-"+str(f))
	
		print("New files in "+dirName)
		for f in dircmp.right_only:
			print("\t-"+str(f))
	
		print("Deleted files in "+dirName)
		for f in dircmp.left_only:
			print("\t-"+str(f))

		print("\n")
		for s in dircmp.subdirs:
			compare(dircmp.subdirs[s], dirName+"/"+s)
		
	def writeLog(self, dircmp, dirName):
		with open('log.txt', 'w') as f:
			f.write("------ "+dirName+" ------")
			f.write("Different files in "+dirName)
			for f in dircmp.diff_files:
				f.write("\t-"+str(f))
	
			f.write("New files in "+dirName)
			for f in dircmp.right_only:
				f.write("\t-"+str(f))
	
			f.write("Deleted files in "+dirName)
			for f in dircmp.left_only:
				f.write("\t-"+str(f))

			f.write("\n")
			for s in dircmp.subdirs:
				compare(dircmp.subdirs[s], dirName+"/"+s)

	def printReport(self):
		self.compare(filecmp.dircmp(HDD_MOUNT, SNAP_MOUNT), "snap")

	def saveLog(self):
		self.compare(filecmp.dircmp(HDD_MOUNT, SNAP_MOUNT), "snap")

m = Machine()
m.mountVDIs()
m.saveLog()
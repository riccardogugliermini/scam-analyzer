import virtualbox
import time
import cv2
import numpy as np
import glob
import shutil
import os
import config

FPS = 15
VM_NAME = "test"
screenshot_path = "machine_screenshot/"


def wait(sth):
    sth.wait_for_completion(-1)

class Machine:
    vbox = virtualbox.VirtualBox()
    session = virtualbox.Session()
    #hdd_uuid = ""
    #snap_uuid = ""

    def __init__(self):
    	#Lookup for the virtual machine, if not found terminates
        try:
            self.vm = self.vbox.find_machine(VM_NAME)
        except virtualbox.library.VBoxErrorObjectNotFound :
            print("Machine not found")
            sys.exit(1)
        #Set up directory to dave screnshoots    
        if os.path.exists(screenshot_path):
            shutil.rmtree(screenshot_path)

        os.makedirs(screenshot_path)
        
       


	#Restore main snapshot
    def restore(self):
        snap = self.vm.find_snapshot("")
        self.vm.create_session(session=self.session)

        restoring = self.session.machine.restore_snapshot(snap)
	
		#Wait unit snapshot is restored
        while restoring.operation_percent < 100:
                time.sleep(0.5)

        self.session.unlock_machine()
			
		#Starup virtual machine
        wait(self.vm.launch_vm_process(self.session,'gui',[]))
        
        #Start capturing traffic
        self.caputreNetwork()
        
        #self.gs = self.session.console.guest.create_session("User", "user")
			
	#Record virtual machine screen 
    def record(self):
        prev = 0
        ss = 0;
        while self.vm.state == virtualbox.library.MachineState.running or self.vm.state == virtualbox.library.MachineState.starting:
            time_elapsed = time.time() - prev
            if time_elapsed > 1.0/FPS:
                h, w, _, _, _, _ = self.session.console.display.get_screen_resolution(0)
                #try to screenshot or write black image
                try:
                    png = self.session.console.display.take_screen_shot_to_array(0, h, w, virtualbox.library.BitmapFormat.png)
                except:
                    png = np.zeros(shape=[512, 512, 3], dtype=np.uint8)

                with open(screenshot_path+'screenshot'+str(ss)+'.png', 'wb') as f:
                    f.write(png)
                    ss+=1

                prev = time.time()

        #Get screenshots
        img_array = []
        files = sorted(glob.glob(screenshot_path+'screenshot*.png'), key=os.path.getmtime)
        for filename in files:
            img = cv2.imread(filename)
            img_array.append(img)

        #Setup encoder
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        out = cv2.VideoWriter('recording.avi',fourcc, FPS, (h,w))

        #Write video
        for i in range(len(img_array)):
           out.write(img_array[i])

        #Release video
        out.release()

        #Remove screenshots
        shutil.rmtree(screenshot_path)

	#Take virtualmachine snapshot
    def takeSnapshot(self):
        #while self.session.state != virtualbox.library. SessionState.locked:
        while self.vm.state != virtualbox.library.MachineState.powered_off:
            time.sleep(0.5)
        snap_name = str(time.time())
        self.session.machine.take_snapshot(snap_name,"", True)
        self.snap_uuid = self.getHD_UUID(snap_name)
        self.hdd_uuid = self.getHD_UUID("")
    
    #Capture virtual machine network traffic
    def caputreNetwork(self):
    	adapter = self.session.machine.get_network_adapter(0)
    	adapter.trace_file = os.path.abspath('vm-network-traffic.pcap')
    	adapter.trace_enabled = True
    	
    def getSSLKeysFile(self):
    	p = self.gs.file_copy_from_guest("C:\\Users\\User\\AppData\\Local\\Keys\\keys.log",  "~/test/keys/keys.log",[])
    	p.wait_for_completion()
    	print(p.error_info.text)
    
    def getHD_UUID(self, snap_name):
    	snap = self.vm.find_snapshot(snap_name)
    	for m in snap.machine.medium_attachments:
    		if m.type_p == virtualbox.library.DeviceType.hard_disk:
    			return m.medium.id_p
    			
    def mountVDIs(self):
    	os.system("mkdir " + config.HDD_PATH)
    	os.system("vboximg-mount -i "+self.hdd_uuid+" -o allow_root " + config.HDD_PATH)
    	os.system("mkdir " + config.SNAP_PATH)
    	os.system("vboximg-mount -i "+self.snap_uuid+" -o allow_root " + config.SNAP_PATH)
    	os.system("mkdir -p mnt/hdd")
    	os.system("mkdir -p mnt/snap")
		
		
m = Machine()
m.restore()
m.record()
m.takeSnapshot()
m.mountVDIs()
print("HD ID:")
print(m.hdd_uuid)
print("")
print("SNAP ID:")
print(m.snap_uuid)

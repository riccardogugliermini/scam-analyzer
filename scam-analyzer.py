import virtualbox
import time
import cv2
import numpy as np
import glob
import shutil
import os

FPS = 15
VM_NAME = "test2"
screenshot_path = "machine_screenshot/"


def wait(sth):
    sth.wait_for_completion(-1)

class Machine:
    vbox = virtualbox.VirtualBox()
    session = virtualbox.Session()

    def __init__(self):
        try:
            self.vm = self.vbox.find_machine('test2 Clone2 Clone')
        except virtualbox.library.VBoxErrorObjectNotFound :
            print("Machine not found")
            sys.exit(1)
        if os.path.exists(screenshot_path):
            shutil.rmtree(screenshot_path)

        os.makedirs(screenshot_path)


    def restore(self):
        snap = self.vm.find_snapshot("")
        self.vm.create_session(session=self.session)

        restoring = self.session.machine.restore_snapshot(snap)

        while restoring.operation_percent < 100:
                time.sleep(0.5)

        self.session.unlock_machine()

        wait(self.vm.launch_vm_process(self.session,'headless',[]))

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

    def takeSnapshot(self):
        #while self.session.state != virtualbox.library. SessionState.locked:
        while self.session.machine.state != virtualbox.library.MachineState.powered_off:
            time.sleep(0.5)
        self.session.machine.take_snapshot(str(time.time()),"", True)




m = Machine()
m.restore()
m.record()
m.takeSnapshot()

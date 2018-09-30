import subprocess, time, os

class ADB:
    def __init__(self, device_name):
        self.ADB_path = 'tool/adb.exe'
        self.device_name = device_name

    def touch(self, x, y=None, times=1, **kwargs):
        # judge input is Loc class or x + y
        for i in range(times):
            if y == None:
                # judge input is a list or not
                if isinstance(x, list):
                    for b in x:
                        self._adb_call(['shell', 'input', 'tap', str(b)], **kwargs)
                else:
                    self._adb_call(['shell', 'input', 'tap', str(x)], **kwargs)
            else:
                x, y = str(x), str(y)
                self._adb_call(['shell', 'input', 'tap', x, y], **kwargs)
            time.sleep(0.1)

    def swipe(self, loc1, loc2, duration='', **kwargs):
        duration = str(duration * 1000) # to str and sec to ms
        self._adb_call(['shell', 'input', 'swipe', str(loc1), str(loc2), duration], **kwargs)

    def key_event(self, key_code, **kwargs):
        key_code = str(key_code)
        self._adb_call(['shell', 'input', 'keyevent', key_code], **kwargs)

    def screen_shot(self, **kwargs):
        '''
        adb shell screencap -p /sdcard/sc.png & adb pull /sdcard/sc.png ../img/sc.png
        '''
        # self._adb_call(['shell', 'screencap', '-p', '/sdcard/sc.png'], **kwargs)
        # self._adb_call(['pull', '/sdcard/sc.png', 'out.png'], **kwargs)

        null = subprocess.DEVNULL
        subprocess.call('tool\\screen_shot.bat', stdout=null, stderr=null)
        # os.system('tool\\screen_shot.bat')

    def _adb_call(self, opts, delay=0.5):
        cmd = [self.ADB_path, '-s', self.device_name]
        cmd += opts
        cmd = ' '.join(cmd)

        # print(cmd)
        # subprocess.Popen(cmd)
        subprocess.call(cmd)
        # time.sleep(delay)

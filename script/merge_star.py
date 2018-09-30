# ===== system module =====
import time
import cv2 as cv
import numpy as np
# ===== self module =====
from module import adb, key
from module.key import Loc

class MS:
    def __init__(self, device_name='CC52BYM17545'):
        self.adb = adb.ADB(device_name)

        types = ['helmet']
        nums = [2, 3, 4, 5, 6]
        templates = {}
        for t in types:
            for n in nums:
                templates['{}-{}'.format(t, n)] = cv.imread('img/{}/{}.png'.format(t, n), 0)

        names = ['star']
        for n in names:
            templates['{}-{}'.format('else', n)] = cv.imread('img/{}/{}.png'.format(t, n), 0)

        self.templates = templates

    def start(self):
        self.adb.touch(key.SORT)
        self.adb.screen_shot()

    def lazy_mode(self):
        start_t = int(time.time())
        while True:
            try:
                now_t = int(time.time())

                skl1_t = now_t
                skl4_t = now_t

                if (now_t - skl1_t) >= 700:
                    self.adb.touch(key.SKILL1)
                    time.sleep(10)
                    self.adb.touch(key.SKILL3)

                    skl1_t = now_t
                if (now_t - skl4_t) >= 2000:
                    self.adb.touch(key.SKILL4)

                    for i in range(20):
                        self.adb.touch(key.MAKE_EQUIP)

                        time.sleep(3)

                    skl4_t = now_t


                time.sleep(30)
            except Exception as e:
                print(now_t - start_t + 'seconds')
                print(e)

    def test(self):
        # touch
        self.adb.touch(key.SORT)
        self.adb.touch(key.MAKE_EQUIP)
        # key_event
        self.adb.key_event(3) # HOME

        self.adb.touch(key.SORT, delay=1)
        self.adb.touch(key.MAKE_EQUIP, delay=3)
        self.adb.touch(key.SORT, delay=5)

    def combine(self, type, num):
        # Take ScreenShot
        self.adb.touch(key.SORT, delay=2)
        self.adb.screen_shot()

        # find-out duplicate object
        img_rgb = cv.imread('img/sc.png')
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        # template = cv.imread('img/{}/{}.png'.format(type, num), 0)
        template = self.templates['{}-{}'.format(type, num)]
        w, h = template.shape[::-1]

        res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)

        threshold = 0.95
        loc = np.where( res >= threshold)
        loc = list(zip(*loc[::-1]))
        print('{} {} have {} objects!'.format(type, num, len(loc)))
        # loc => [(220, 710), (340, 710), (460, 710), (580, 710), (160, 790)]

        # for i in range(len(loc)):
        #     cv.rectangle(img_rgb, loc[i], (loc[i][0] + w, loc[i][1] + h), (0,0,255), 2)
        # cv.imwrite('img/res.png',img_rgb)
        for i in range(0, len(loc) - 1, 2):
            start = Loc(loc[i][0] + w / 2, loc[i][1] + h / 2)
            end = Loc(loc[i + 1][0] + w / 2, loc[i + 1][1] + h / 2)
            self.adb.swipe(start, end, delay=0.1)

    def SKILL4(self):
        self.adb.touch(key.SKILL4)

        for i in range(20):
            self.adb.touch(key.MAKE_EQUIP)
            time.sleep(3)

import sys, time

from module import key
from script.merge_star import MS

if __name__ == '__main__':
    device_name = 'CC52BYM17545'
    bot = MS(device_name)

    if sys.argv[1] == 'test':
        bot.test()
    elif sys.argv[1] == 'touch':
        for k in sys.argv[2:]:
            key_name = 'key.{}'.format(k)
            key_name = eval(key_name)
            bot.adb.touch(key_name)
    elif sys.argv[1] == 'SKILL4':
        bot.SKILL4()
    elif sys.argv[1] == 'sc':
        bot.adb.screen_shot()
    elif sys.argv[1] == 'combine':
        while True:
            s_t = time.time()

            print('Click MAKE_EQUIP 6 times')
            bot.adb.touch(key.MAKE_EQUIP, times=6)
            for n in [2, 3, 4, 5, 6]:
                bot.combine('helmet', n)

            bot.combine('else', 'star')

            print('====== {} seconds one round ======'.format(time.time() - s_t))

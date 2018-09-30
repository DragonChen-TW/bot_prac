# Android Bot practice

## requirements
- python3.6
- adb.exe(exist in tool/)
- now developed on windows 10

## script list(game list)
- [merge_star](https://play.google.com/store/apps/details?id=com.nanoo.mergestar)

## how-to
### test
Test mode is a sequence of movements.
They contains basic event about touch screen, drag, keyevent(like home btn).
```
Movements:
  1. click SORT btn
  2. click MAKE_EQUIP btn
  3. trigger keyevent home btn
```

You can start test mode
```
python main.py test
```

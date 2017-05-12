
import time


import uinput

def keyclick():
	device = uinput.Device([
	        uinput.KEY_E,
	        uinput.KEY_H,
	        uinput.KEY_L,
	        uinput.KEY_O,
	        ])

	device.emit_click(uinput.KEY_H)
	device.emit_click(uinput.KEY_E)
	device.emit_click(uinput.KEY_L)
	device.emit_click(uinput.KEY_L)
	device.emit_click(uinput.KEY_O)

def mousemove():
	device = uinput.Device([
    uinput.BTN_LEFT,
    uinput.BTN_RIGHT,
    uinput.REL_X,
    uinput.REL_Y,
    ])

	for i in range(20):
	    device.emit(uinput.REL_X, 5)
	    device.emit(uinput.REL_Y, 5)

def keyboardcombos():
	device = uinput.Device([
        uinput.KEY_LEFTALT,
        uinput.KEY_TAB,
        ])

	device.emit_combo([
        uinput.KEY_LEFTALT,
        uinput.KEY_TAB,
        ])
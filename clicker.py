#Auto Clicker
#Hotkeys : SHFT + a 
#Press once to start, once to stop


from pynput import mouse, keyboard
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener

print("Listening for hotkey..")

hotkeys = [ {keyboard.Key.shift, keyboard.KeyCode(char='a')}, {keyboard.KeyCode(char='A'), keyboard.Key.shift} ]
current = set()
mouse = Controller()

def click_pos(x,y):
	mouse.position = (x, y)
	mouse.press(Button.left) 
	mouse.release(Button.left)

  
def execute():   
	print("Make sure desired window is in focus with taskbar aligned to left!\n") 
	for i in range(180):	
		time.sleep(10) #every 10 sec 
	#	click_pos(462, 461)
		click_pos(111, 75)			

		
def on_press(key):   
    if any(key in hot_key for hot_key in hotkeys): 
        current.add(key)
        print(str(current))
        if any(all(key2 in current for key2 in hot_key) for hot_key in hotkeys): 					execute()


def on_release(key):     
    if any(key in hot_key for hot_key in hotkeys): 
        current.remove(key)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

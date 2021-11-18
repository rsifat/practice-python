import time
import pyautogui
import tkinter as ss


def screenshot():
    name = int(round(time.time()*1000))
    name = 'C:/ThisPC/Desktop/{}.png'.format(name)
    #img = pyautogui.screenshot('test.png')
    img = pyautogui.screenshot(name)
    img.show()
    
    
    
root = ss.Tk()
frame = ss.Frame(root)
frame.pack()

button = ss.Button(
    frame,
    text="Take Screenshot",
    command = screenshot
    )
button.pack(side=ss.RIGHT)

# close = ss.Button(
#     frame,
#     text="QUIT",
#     command = quit
#     )
# close.pack(side=ss.LEFT)

root.mainloop()




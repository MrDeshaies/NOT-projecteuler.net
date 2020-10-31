import tkinter as tk
from tkinter import font
import time
import colorsys

def time_millis():
    return int(round(time.time()*1000))

class FullScreenApp(object):
    def __init__(self, root, **kwargs):
        self.root=root
        # start full screen and hide the cursor
        root.attributes('-fullscreen', True)
        root.config(cursor='none')
        root.bind('<Escape>',self.exit)
        root.bind('<Key>',self.key_press)
        # create a full-screen canvas
        self.cv = tk.Canvas(self.root)
        self.cv.pack(expand=tk.YES, fill=tk.BOTH)
        # initialize our values. We'll vary the hue every 250ms
        self.current_hue = 0.0
        self.refresh_delay = 250
        self.last_sleep_change = time_millis()
        self.speed_text = None
        self.cv.after(self.refresh_delay, self.refresh_color)
    
    def key_press(self,event):
        if event.char == "-":
            self.slow_down(25)
        elif event.char == "+":
            self.speed_up(25)
    
    def speed_up(self,amount):
        self.refresh_delay -= amount
        if self.refresh_delay <= 0:
            self.refresh_delay = 25
        self.last_sleep_change = time_millis()
    
    def slow_down(self,amount):
        self.refresh_delay += amount
        if self.refresh_delay > 1000:
            self.refresh_delay = 1000
        self.last_sleep_change = time_millis()

    def exit(self,event):
        exit()
    
    def refresh_color(self):
        # loop over the HSV spectrum, varying the hue (color),
        # and keeping the saturation and value to the maximum, for bright colors.
        self.current_hue += 0.01
        if self.current_hue > 1.0:
            self.current_hue = 0.0
        next_rgb = colorsys.hsv_to_rgb(self.current_hue, 1.0, 1.0)
        next_tk_rgb = self.convert_to_tk_rgb(next_rgb)
        self.cv.configure(bg=next_tk_rgb)
        self.paint_sleep_delay()
        # reschedule to refresh
        self.cv.after(self.refresh_delay, self.refresh_color)
    
    def paint_sleep_delay(self):
        # delete the text after displaying for more than a second
        if (time_millis()-self.last_sleep_change > 1000) and self.speed_text is not None:
            self.cv.delete(self.speed_text)
            self.speed_text = None
            return
        
        # create the text if speed changed in the last second
        if time_millis()-self.last_sleep_change < 1000:
            if self.speed_text is None:
                helvetica48 = font.Font(family='Helvetica', size=48, weight='bold')
                self.speed_text = self.cv.create_text(100,100,
                    font=helvetica48, text=str(self.refresh_delay))
            else:
                self.cv.itemconfig(self.speed_text, text=str(self.refresh_delay))
    
    def convert_to_tk_rgb(self,rgb):
        """Converts from floating RGB values, between 0.0-1.0,
            to their usual 8-bit values (0-255), expressed in hex
            for Tk like #0A22FF"""
        tk_rgb = "#%02x%02x%02x" % (
            int(round(rgb[0]*255)),
            int(round(rgb[1]*255)),
            int(round(rgb[2]*255)))
        return tk_rgb

root=tk.Tk()
app=FullScreenApp(root)
root.mainloop()
import tkinter as tk
import time
import colorsys

class FullScreenApp(object):
    def __init__(self, root, **kwargs):
        self.root=root
        # start full screen and hide the cursor
        root.attributes('-fullscreen', True)
        root.config(cursor='none')
        root.bind('<Escape>',self.exit)
        # create a full-screen canvas
        self.cv = tk.Canvas(self.root)
        self.cv.pack(expand=tk.YES, fill=tk.BOTH)
        # initialize our values. We'll vary the hue every 250ms
        self.current_hue = 0.0
        self.refresh_delay = 250
        self.cv.after(self.refresh_delay, self.refresh_color)
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
        self.cv.after(self.refresh_delay, self.refresh_color)
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
import tkinter as tk
import time
import colorsys

class FullScreenApp(object):
    def __init__(self, root, **kwargs):
        self.root=root
        root.attributes('-fullscreen', True)
        root.config(cursor='none')
        root.bind('<Escape>',self.exit)

        self.cv = tk.Canvas(self.root)
        self.cv.pack(expand=tk.YES, fill=tk.BOTH)
        self.current_hue = 0.0
        self.refresh_delay = 250
        self.refresh_color()
        self.cv.after(self.refresh_delay, self.refresh_color)
    def exit(self,event):
        exit()
    def refresh_color(self):
        next_rgb = colorsys.hsv_to_rgb(self.current_hue, 1.0, 1.0)
        next_tk_rgb = self.convert_to_tk_rgb(next_rgb)
        self.cv.configure(bg=next_tk_rgb)
        self.cv.update()
        self.current_hue += 0.01
        self.cv.after(self.refresh_delay, self.refresh_color)
    def convert_to_tk_rgb(self,rgb):
        tk_rgb = "#%02x%02x%02x" % (
            int(round(rgb[0]*255)),
            int(round(rgb[1]*255)),
            int(round(rgb[2]*255)))
        return tk_rgb

root=tk.Tk()
app=FullScreenApp(root)
root.mainloop()
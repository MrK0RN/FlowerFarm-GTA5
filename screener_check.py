import time

from PIL import ImageGrab, Image
import os


class Screener:
    def __init__(self):
        self.name = "screenshots.png"
        self.screenshot = ImageGrab.grab(bbox=(348, 1065, 618, 1234))
        self.absolute_zero = (483, 1195)
        self.zero = (135, 130)
        ##self.screenshot.show()
        self.results = {}
        self.flower_color = (175,140,140)
        self.flower_area = 5
        self.button_coordinates = (1328, 1205)
        self.button_area = 9
        self.button_colour = (255, 255, 255)
        self.flower_percent = 0.6
        self.button_percent = 0.73

    def check_color_procent(self, colour1, colour2):
        result, flag = 0, True
        for i in range(3):
            if 1 - abs(colour1[i]-colour2[i])/256 < 0.84:
                flag = False
        if flag: result = 1 - abs(sum(colour2) - sum(colour1))/768

        return result

    def screenshot_full_rewrite(self):
        self.screenshot = ImageGrab.grab()
    def check_color(self, colour1, colour2):
        result = True
        for i in range(3):
            if abs(colour1[i]-colour2[i]) > 25:
                result = False
        if abs(sum(colour2) - sum(colour1)) > 70:
            result = False
        return result

    def rewrite(self):
        self.screenshot = ImageGrab.grab(bbox=(348, 1065, 618, 1234))
    def get_color(self, x, y):
        self.color = self.screenshot.getpixel((x, y))[:3]
        return self.color

    def show_me_area(self, x, y, around):
        ImageGrab.grab(bbox=(x-around, y-around, x+around, y+around)).show()

    def show_me_area_cropped(self, x, y, around):
        self.screenshot.crop((x-around, y-around, x+around, y+around)).show()

    def clear_results(self):
        self.results = {}

    def forward_tracker(self, step, multiply, color):
        if color == None:
            color = self.flower_color
        for i in range(1, step):

            #g.show_me_area_cropped(self.zero[0], self.zero[1]-3*i, 5)
            if self.check_color(color, self.get_color(self.zero[0], self.zero[1]-multiply*i)):
                #self.show_me_area_cropped(self.zero[0], self.zero[1] - multiply * i - (self.flower_area-1)// 2,(self.flower_area-1)// 2)
                ww = self.area_tracker(self.zero[0], self.zero[1]-multiply*i, color, self.flower_percent)

                if ww:
                    print("found: " + str((self.zero[0], self.zero[1]-multiply*i)))
                    #wself.show_me_area_cropped(self.zero[0], self.zero[1] - multiply*i - (self.flower_area-1)//2, (self.flower_area-1)//2)
                    self.results[multiply*i] = (self.zero[0], self.zero[1] - multiply*i)
                    print(self.results)
        self.rewrite()
    def save_map(self):
        os.chdir("maps")
        self.screenshot.save("map_1"+str(time.time())+".jpg")
        os.chdir("..")

    def load_map_as_scrshot(self):
        os.chdir("maps")
        self.screenshot = Image.open(os.listdir()[0])
    def forward_tracker_procent(self, step, multiply, x, y, color):
        result = []
        for i in range(1, step):
            result.append(self.check_color_procent(color, self.get_color(x, y-multiply*i)))
        return result

    def area_procent_get(self, zero_x, zero_y, color):
        area_results = sum(self.forward_tracker_procent(self.flower_area, 1, zero_x, zero_y, color))
        for i in range(1, (self.flower_area + 1) // 2):
            area_results += sum(self.forward_tracker_procent(self.flower_area, 1, zero_x - i, zero_y, color))
            area_results += sum(self.forward_tracker_procent(self.flower_area, 1, zero_x + i, zero_y, color))

        return area_results/self.flower_area**2
    def area_tracker(self, zero_x, zero_y, color, percent):

        area_results = self.area_procent_get(zero_x, zero_y, color)

        if area_results > percent:
            return True
        else:
            return False

    def find_button(self):
        self.show_me_area(1328, 1205, 9)
    def button_check(self):
        self.screenshot_full_rewrite()
        res = self.area_tracker(self.button_coordinates[0], self.button_coordinates[1] + (self.button_area - 1)//2, self.button_colour, self.button_percent)
        self.rewrite()
        return res
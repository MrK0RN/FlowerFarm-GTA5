from PIL import ImageGrab

class Screen:
    def __init__(self):
        self.name = "screenshots.png"
        self.screenshot = ImageGrab.grab()

    def rewrite(self):
        self.screenshot = ImageGrab.grab()

    def check_color(self, x, y):
        self.color = self.screenshot.getpixel((x, y))[:3]
        return self.color



g = Screen()

g.check_color(1000, 1000)

print(g.color)
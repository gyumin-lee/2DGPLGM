from pico2d import*


class TextGroup:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 32)

    def draw(self,boy):
        self.font.draw(boy.x , boy.y + 20,("Get the item"),(255,255,255))
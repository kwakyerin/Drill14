from pico2d import load_image


class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x, self.y = 400, 300

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 337, 184, 169, self.x, self.y, 120, 110)

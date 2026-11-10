from pico2d import load_image
import game_framework


class Bird:
    FRAME_DURATION = 0.1
    FRAME_SCALE = 120 / 184
    image = None
    FRAMES = (
        (34, 1, 180, 144), (216, 2, 362, 143),
        (398, 12, 544, 142), (555, 17, 726, 139),
        (728, 48, 910, 136), (34, 217, 180, 335),
        (216, 216, 362, 340), (398, 216, 544, 336),
        (580, 217, 726, 326), (762, 219, 908, 329),
        (34, 392, 180, 500), (216, 394, 362, 500),
        (376, 395, 544, 483), (546, 370, 726, 484),
    )

    def __init__(self, x=400, y=300):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.image = Bird.image
        self.x, self.y = x, y
        self.frame = 0
        self.elapsed_time = 0.0

    def update(self):
        self.elapsed_time += game_framework.frame_time
        while self.elapsed_time >= self.FRAME_DURATION:
            self.elapsed_time -= self.FRAME_DURATION
            self.frame = (self.frame + 1) % len(self.FRAMES)

    def draw(self):
        left, top, right, bottom = self.FRAMES[self.frame]
        width, height = right - left, bottom - top
        column = self.frame % 5
        row = self.frame // 5
        cell_center_x = column * 184 + 92
        cell_center_y = (84 + row * 169)
        frame_center_x = (left + right) / 2
        frame_center_y = (top + bottom) / 2
        draw_x = self.x + (frame_center_x - cell_center_x) * self.FRAME_SCALE
        draw_y = self.y + (cell_center_y - frame_center_y) * self.FRAME_SCALE
        source_y = self.image.h - bottom
        self.image.clip_draw(
            left, source_y, width, height, draw_x, draw_y,
            width * self.FRAME_SCALE, height * self.FRAME_SCALE)

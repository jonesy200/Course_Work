import pygame

class Spritesheet:
    def __init__(self, filename, path):
        self.path = path
        full_path = self.path / filename
        self.sheet = pygame.image.load(full_path).convert_alpha()

    def get_frame(self, x, y, width, height):
        frame = pygame.Surface((width, height), pygame.SRCALPHA)
        frame.blit(self.sheet, (0, 0), (x, y, width, height))
        return frame

    def get_frames_row(self, row_index, frame_width, frame_height, num_frames):
        frames = []
        for i in range(num_frames):
            x = i * frame_width
            y = row_index * frame_height
            frames.append(self.get_frame(x, y, frame_width, frame_height))
        return frames
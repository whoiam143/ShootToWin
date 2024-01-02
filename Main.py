import pygame
import random

pygame.init()

ARIAL_50 = pygame.font.SysFont("arial", 50)

WHITE = (255, 255, 255)


class Button:
    def __init__(self, x, y, width, height, text, image_path, hover_impage_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_impage_path:
            self.hover_image = pygame.image.load(hover_impage_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)

        self.is_hovered = False

    def draw_button(self, screen):  # Метод нарисовки кнопки
        if self.is_hovered:
            current_image = self.hover_image
        else:
            current_image = self.image
        screen.blit(current_image, self.rect.topleft)

        text_surface = ARIAL_50.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):  # Проверка ли мышь на кнопке
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Main:
    def __init__(self):
        self.width = 1920
        self.height = 1080

        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Title")
        self.display.fill(pygame.Color("black"))
        self.loop = True

        self.cursor = pygame.image.load("Texture/pricel.png").convert_alpha()
        pygame.mouse.set_visible(False)

        self.BackGround = Background("Texture/level1.png", [0, 0])
        self.display.blit(self.BackGround.image, self.BackGround.rect)

        self.butt1 = Button(self.width / 2 - (252 / 2), 500, 252, 75, "test1", "Texture/Phon.png", "Texture/logo.png")
        self.butt2 = Button(self.width / 2 - (252 / 2), 700, 252, 75, "test2", "Texture/logo.png", "Texture/Phon.png")

    def main_game_loop(self):
        while self.loop:
            self.display.blit(self.BackGround.image, self.BackGround.rect)

            self.butt1.draw_button(self.display)
            self.butt1.check_hover(pygame.mouse.get_pos())
            self.butt2.draw_button(self.display)
            self.butt2.check_hover(pygame.mouse.get_pos())
            pos = pygame.mouse.get_pos()
            if pygame.mouse.get_focused():
                self.display.blit(self.cursor, pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.loop = False

            pygame.display.flip()


if __name__ == "__main__":
    game = Main()
    game.main_game_loop()

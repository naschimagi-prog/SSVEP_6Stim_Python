import pygame
import time

from main import resource_path


def show_plus(screen, duration):

    width, height = screen.get_size()

    start = time.time()

    while time.time() - start < duration:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        screen.fill((200, 200, 200))

        pygame.draw.line(
            screen,
            (0, 0, 0),
            (width // 2 - 40, height // 2),
            (width // 2 + 40, height // 2),
            6
        )

        pygame.draw.line(
            screen,
            (0, 0, 0),
            (width // 2, height // 2 - 40),
            (width // 2, height // 2 + 40),
            6
        )

        pygame.display.flip()


def show_text(screen, text, duration):

    width, height = screen.get_size()

    font = pygame.font.Font(
        resource_path("THSarabunNew Bold.ttf"),
        60
    )

    start = time.time()

    while time.time() - start < duration:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        screen.fill((255, 255, 255))

        lines = text.split("\n")

        for i, line in enumerate(lines):

            t = font.render(
                line,
                True,
                (0, 0, 0)
            )

            rect = t.get_rect(
                center=(
                    width // 2,
                    height // 2 + i * 70
                )
            )

            screen.blit(t, rect)

        pygame.display.flip()


# ==========================================
# รอให้กด SPACE
# ==========================================

def wait_for_space(screen):

    width, height = screen.get_size()

    font = pygame.font.Font(
        resource_path("THSarabunNew Bold.ttf"),
        60
    )

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

                if event.key == pygame.K_SPACE:
                    return

        screen.fill((70, 70, 70))

        text = font.render(
            "กด SPACE เพื่อดำเนินการต่อ",
            True,
            (255, 255, 255)
        )

        rect = text.get_rect(
            center=(width // 2, height // 2)
        )

        screen.blit(text, rect)

        pygame.display.flip()


def run(screen):

    # ==========================================
    # เริ่มต้น
    # ==========================================

    show_plus(screen, 3)


    # ==========================================
    # การกระทำ
    # ==========================================

    for i in range(5):

        show_text(
            screen,
            "เคลื่อนไหวลิ้น\nลิ้นดันกระพุ้งแก้มขวา",
            10
        )

        show_plus(screen, 3)


    # ==========================================
    # หยุดรอ SPACE
    # ก่อนเข้าสู่การจินตนาการ
    # ==========================================

    wait_for_space(screen)


    # ==========================================
    # การจินตนาการ
    # ==========================================

    for i in range(5):

        show_text(
            screen,
            "จินตนาการลิ้น\nลิ้นดันกระพุ้งแก้มขวา",
            10
        )

        show_plus(screen, 3)


if __name__ == "__main__":

    pygame.init()

    screen = pygame.display.set_mode(
        (0, 0),
        pygame.FULLSCREEN
    )

    run(screen)

    pygame.quit()
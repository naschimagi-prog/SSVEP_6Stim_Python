import pygame
import sys
import os

def resource_path(relative_path):
    """รองรับทั้งตอนรันจาก Python และ .exe"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

from Stimuli import tongue_left
from Stimuli import tongue_right
from Stimuli import tongue_up
from Stimuli import tongue_down
from Stimuli import cheek_left
from Stimuli import cheek_right


# ------------------------
# 🔥 ฟังก์ชันวาดข้อความ (สวย + หนา + เงา)
# ------------------------
# ------------------------
# 🔥 ฟังก์ชันวาดข้อความ (สวย + หนา + เงา)
# ------------------------
def draw_text_center(screen, text, y, size=70):

    width, _ = screen.get_size()

    font_path = resource_path("THSarabunNew Bold.ttf")
    font = pygame.font.Font(font_path, size)

    # เงา
    shadow = font.render(text, True, (0, 0, 0))
    rect_shadow = shadow.get_rect(center=(width // 2, y))
    screen.blit(shadow, (rect_shadow.x + 3, rect_shadow.y + 3))

    # ตัวจริง
    txt = font.render(text, True, (255, 255, 255))
    rect = txt.get_rect(center=(width // 2, y))
    screen.blit(txt, rect)


# ------------------------
# 🔥 หน้า Title
# ------------------------
def show_title(screen):

    width, height = screen.get_size()
    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    running = False

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill((20, 22, 45))

        pygame.draw.rect(screen, (100,150,255), (0,0,width,12))
        pygame.draw.rect(screen, (100,150,255), (0,height-12,width,12))

        draw_text_center(screen, "การบันทึกข้อมูล", height//2 - 80, 95)
        draw_text_center(screen, "การเคลื่อนไหวลิ้น", height//2 + 40, 95)

        pygame.display.flip()


# ------------------------
# 🔥 หน้าแนะนำ (spacing สวย ไม่ซ้อน)
# ------------------------
def show_screen(screen,text):

    width,height = screen.get_size()
    lines = text.split("\n")

    spacing = 110
    start_y = height//2 - (len(lines)//2 * spacing)

    running=True

    while running:   

        for event in pygame.event.get():
       
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    running=False

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill((70,70,70))

        for i,line in enumerate(lines):
            draw_text_center(screen, line, start_y + i*spacing, 58)

        pygame.display.flip()


# ------------------------
# 🔥 โหลดรูปอัตโนมัติ
# ------------------------
def load_image_auto(path):

    possible = [
        resource_path(path),
        resource_path(path + ".jpg"),
        resource_path(path + ".png"),
        resource_path(path + ".jpeg")
    ]

    for p in possible:
        if os.path.exists(p):
            print("โหลดรูป:", p)
            return pygame.image.load(p)

    print("❌ ไม่พบรูป:", path)
    pygame.quit()
    sys.exit()

# ------------------------
# 🔥 หน้า "คำสั่ง + รูป"
# ------------------------
def show_instruction(screen, text, img_list):

    width, height = screen.get_size()

    images = []

    for img_path in img_list:
        img = load_image_auto(img_path)
        img = pygame.transform.scale(img, (320,200))
        images.append(img)

    spacing = 60
    total_width = (320 * 3) + (spacing * 2)
    start_x = (width - total_width) // 2
    y_pos = height // 2

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    running = False

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill((70,70,70))

        # 🔥 ข้อความใหญ่ + หนา + เงา
        draw_text_center(screen, text, height//4, 68)

        # 🔥 
        for i, img in enumerate(images):
            x = start_x + i * (320 + spacing)
            screen.blit(img, (x, y_pos))

        pygame.display.flip()


# ------------------------
# MAIN
# ------------------------
def main():

    pygame.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

    show_title(screen)

    show_screen(
        screen,
        "คำแนะนำการทดลอง\n\n"
        "มองเครื่องหมาย + ที่กลางจอ\n"
        "ทำตามคำสั่งที่ปรากฏ\n"
        "กด SPACE เพื่อเริ่ม"
    )

    show_instruction(screen,"ลิ้นแตะมุมปากซ้าย",
                     ["images/left1","images/left2","images/left3"])
    tongue_left.run(screen)

    show_instruction(screen,"ลิ้นแตะมุมปากขวา",
                     ["images/right1","images/right2","images/right3"])
    tongue_right.run(screen)

    show_instruction(screen,"ลิ้นแตะริมฝีปากบน",
                     ["images/up1","images/up2","images/up3"])
    tongue_up.run(screen)

    show_instruction(screen,"ลิ้นแตะริมฝีปากล่าง",
                     ["images/down1","images/down2","images/down3"])
    tongue_down.run(screen)

    show_instruction(screen,"ลิ้นดันแก้มซ้าย",
                     ["images/cheek_left1","images/cheek_left2","images/cheek_left3"])
    cheek_left.run(screen)

    show_instruction(screen,"ลิ้นดันแก้มขวา",
                     ["images/cheek_right1","images/cheek_right2","images/cheek_right3"])
    cheek_right.run(screen)

    pygame.quit()


if __name__ == "__main__":
    main()

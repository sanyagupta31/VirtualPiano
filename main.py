import pygame
import os

# Pygame initialize
pygame.init()
pygame.mixer.init()

# Paths handle करने के लिए
base_path = os.path.dirname(os.path.abspath(__file__))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)

# Keys mapping (Keyboard -> Sound Files)
keys = {
    pygame.K_a: {"sound": os.path.join(base_path, "sounds", "95328__ramas26__c.wav"), "pos": (50, 200)},
    pygame.K_s: {"sound": os.path.join(base_path, "sounds", "95329__ramas26__d.wav"), "pos": (150, 200)},
    pygame.K_d: {"sound": os.path.join(base_path, "sounds", "95330__ramas26__e.wav"), "pos": (250, 200)},
    pygame.K_f: {"sound": os.path.join(base_path, "sounds", "95331__ramas26__f.wav"), "pos": (350, 200)},
    pygame.K_g: {"sound": os.path.join(base_path, "sounds", "95332__ramas26__g.wav"), "pos": (450, 200)},
    pygame.K_h: {"sound": os.path.join(base_path, "sounds", "68437__pinkyfinger__piano-a.wav"), "pos": (550, 200)},
    pygame.K_j: {"sound": os.path.join(base_path, "sounds", "68438__pinkyfinger__piano-b.wav"), "pos": (650, 200)},
}

# Load Sounds
sounds = {key: pygame.mixer.Sound(value["sound"]) for key, value in keys.items()}

# Window setup
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Virtual Piano 🎹")

# Load background image
bg_image = pygame.image.load(os.path.join(base_path, "pianoimg.webp"))
bg_image = pygame.transform.scale(bg_image, (800, 400))

# Active keys storage
active_keys = set()

running = True
while running:
    screen.fill(WHITE)  # Clear Screen
    screen.blit(bg_image, (0, 0))  # Draw Background

    # Draw Virtual Keys
    for key, data in keys.items():
        color = YELLOW if key in active_keys else GRAY
        pygame.draw.rect(screen, color, (*data["pos"], 80, 150))  # Draw Key
        pygame.draw.rect(screen, BLACK, (*data["pos"], 80, 150), 3)  # Border

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Key Press Event
        if event.type == pygame.KEYDOWN and event.key in sounds:
            sounds[event.key].play()
            active_keys.add(event.key)

        # Key Release Event (Remove Highlight)
        if event.type == pygame.KEYUP and event.key in active_keys:
            active_keys.remove(event.key)

    pygame.display.update()

pygame.quit()

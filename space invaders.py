import pygame
import time
pygame.init()
WIDTH = 1000
HEIGHT = 750
TITLE = "space invaders"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
run = True
space = pygame.image.load("space.png")
red = pygame.image.load("red.png")
yellow = pygame.image.load("Yellow.png")
rec = pygame.Rect(497,0,6,750)
red_health = 10
yellow_health = 10

yellow_bullets = []
red_bullets = []
red_health = 10
yellow_health = 10

class Ship(pygame.sprite.Sprite):
  def __init__(self,x,y,image,angle):
    super().__init__()
    self.image = pygame.transform.scale(image,(50,50))
    self.image = pygame.transform.rotate(self.image,angle)
    self.rect = self.image.get_rect()
    self.rect.x =x
    self.rect.y = y
  def move(self,player,vx,vy):
    self.rect.x += vx
    self.rect.y += vy
    if self.rect.top <0:
      self.rect.top = 0
    if self.rect.bottom >HEIGHT:
      self.rect.bottom = HEIGHT
    if player == "red":
      if self.rect.left <0:
        self.rect.left = 0
      if self.rect.right >497:
        self.rect.right = 497
    if player == "yellow":
      if self.rect.left <503:
       self.rect.left = 503
      if self.rect.right >WIDTH:
       self.rect.right = WIDTH
    

red_ship = Ship(250,375,red,90)
yellow_ship = Ship(750,375,yellow,270)
sprite_group = pygame.sprite.Group()
sprite_group.add(red_ship)
sprite_group.add(yellow_ship)

def handle_bullets():
  global red_health,yellow_health
  for bullet in red_bullets:
    pygame.draw.rect(screen,"red",bullet)
    bullet.x += 2
  for bullet in yellow_bullets:
    pygame.draw.rect(screen,"yellow",bullet)
    bullet.x -= 2
  for bullet in red_bullets:
    if bullet.colliderect(yellow_ship.rect):
      yellow_health -= 1
      red_bullets.remove(bullet)
    if bullet.x > WIDTH:
      red_bullets.remove(bullet)
  for bullet in yellow_bullets:
    if bullet.colliderect(red_ship.rect):
      red_health -= 1
      yellow_bullets.remove(bullet)
    if bullet.x < 0:
      yellow_bullets.remove(bullet)



    
    
while run:
  screen.blit(space,(0,0))
  pygame.draw.rect(screen,"red",rec,0)
  sprite_group.draw(screen)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
     run = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_r:
        bullet = pygame.Rect(red_ship.rect.x+50,red_ship.rect.y+20,15,10)
        red_bullets.append(bullet)
      if event.key == pygame.K_y:
        bullet = pygame.Rect(yellow_ship.rect.x,yellow_ship.rect.y+20,15,10)
        yellow_bullets.append(bullet)
  font = pygame.font.SysFont("calibri",20)
  text = font.render("Health:"+str(red_health),True,"black")
  screen.blit(text,(10,10))
  font = pygame.font.SysFont("calibri",20)
  text = font.render("Health:"+str(yellow_health),True,"black")
  screen.blit(text,(900,10))
      
        
  keys_pressed = pygame.key.get_pressed()
  if keys_pressed[pygame.K_a]:
    red_ship.move("red",-1,0)
  if keys_pressed[pygame.K_w]:
    red_ship.move("red",0,-1)
  if keys_pressed[pygame.K_d]:
      red_ship.move("red",+1,0)
  if keys_pressed[pygame.K_s]:
      red_ship.move("red",0,+1)
  if keys_pressed[pygame.K_UP]:
      yellow_ship.move("yellow",0,-1)
  if keys_pressed[pygame.K_LEFT]:
      yellow_ship.move("yellow",-1,0)
  if keys_pressed[pygame.K_RIGHT]:
      yellow_ship.move("yellow",+1,0)
  if keys_pressed[pygame.K_DOWN]:
      yellow_ship.move("yellow",0,+1)
  
    
  handle_bullets()

  if red_health <= 0:
    font = pygame.font.SysFont("calibri",40)
    text = font.render("YELLOW WINS!!",True,"yellow")
    screen.blit(text,(350,350))
    pygame.display.update()
    time.sleep(5)
    run = False

  if yellow_health <= 0:
    font = pygame.font.SysFont("calibri",40)
    text = font.render("RED WINS!!",True,"yellow")
    screen.blit(text,(350,350))
    pygame.display.update()
    time.sleep(5)
    run = False

  
    
    
  
    
  pygame.display.update()
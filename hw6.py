import pygame
pygame.init()
screen_width,screen_height = 500,500
display_surface = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("adding image and background image ")
background_image = pygame.transform.scale(pygame.image.load("backgroung image.jpeg").convert(),(screen_width,screen_height))
bow_image = pygame.transform.scale(pygame.image.load("bow image.jpg").convert_alpha(),(200,200))
bow_rect = bow_image.get_rect(center = (screen_width//2,screen_height//2-30))
text = pygame.font.Font(None,36).render("hello world",True,pygame.Color("black"))
text_rect = text.get_rect(center = (screen_width//2,screen_height//2+110))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running = False
        display_surface.blit(background_image,(0,0))
        display_surface.blit(bow_image,bow_rect)
        display_surface.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__=="__main__":
    game_loop()

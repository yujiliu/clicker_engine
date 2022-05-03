import pygame, sys


def event_listener_menu(screen, start_button, settings_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_button.rect.collidepoint(pygame.mouse.get_pos()):
                start_button.active = True
                start_button.mode_menu = False
        elif event.type == pygame.MOUSEBUTTONUP:
            start_button.active = False


def update_screen_menu(screen, bg_color, start_button, settings_button):
    screen.fill(bg_color)
    start_button.output()
    settings_button.output()
    pygame.display.flip()


def event_listener_game(screen, main_game_button, mode_game, settings_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if main_game_button.rect.collidepoint(pygame.mouse.get_pos()):
                main_game_button.active = True
            break
        elif event.type == pygame.MOUSEBUTTONUP:
            main_game_button.active = False


def update_screen_game(screen, bg_color, main_game_button, settings_button):
    screen.fill(bg_color)
    main_game_button.output()
    settings_button.output()
    pygame.display.flip()

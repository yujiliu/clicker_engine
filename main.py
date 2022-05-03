import pygame

import controls
from controls import event_listener_menu, event_listener_game
from button import StartButton, SettingsButton
from main_game_button import MainGameButton


def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("INSERT YOUR GAME NAME HERE")
    bg_color = (0, 0, 0)

    start_button = StartButton(screen)
    settings_button = SettingsButton(screen)

    main_game_button = MainGameButton(screen)

    mode_game = False

    while True:
        if not start_button.mode_menu:
            mode_game = True
        if start_button.mode_menu:
            start_button.update()
            settings_button.update()
            controls.update_screen_menu(screen, bg_color, start_button, settings_button)
            event_listener_menu(screen, start_button, settings_button)
        if mode_game:
            main_game_button.update()
            settings_button.update()
            controls.update_screen_game(screen, bg_color, main_game_button, settings_button)
            event_listener_game(screen, main_game_button, mode_game, settings_button)


if __name__ == "__main__":
    main()

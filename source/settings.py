import json


# function to read from world_*.json file:
#       player information
#       tile information
#       game settings
#       shooting settings
import pygame


def read(path):
    with open(path, 'r') as file:
        content = json.load(file)
        world_tiles = content
    return world_tiles


# function to read from world_enemies.json information
def read_enemies(path):
    with open(path, 'r') as file:
        content = json.load(file)
        world_enemies = content
    return world_enemies


# function to read world_map.txt information
def read_map(path):
    with open(path, 'r') as file:
        content = file.read()
        temp_map = eval(content)
    return temp_map


while True:
    try:
        # input the name of directory on the game settings to load
        directory = input("Please enter directory (choose between template1/template2): ")

        # dictionary of game settings
        game_settings = read(f"data/{directory}/game_settings.json")

        # dictionary of attributes of player
        player_settings = read(f"data/{directory}/world_player.json")

        # list of enemy information dictionaries
        enemies = read_enemies(f"data/{directory}/world_enemies.json")

        # dictionary of titles images path like : id - path
        tiles = read(f"data/{directory}/world_tiles.json")

        # list of lists of the codes of tiles
        WORLD_MAP = read_map(f"data/{directory}/world_map.txt")

        # dictionary of shoot information
        shooting_info = read(f"data/{directory}/world_shoot.json")

        ui_settings = read(f"data/{directory}/world_ui.json")

        # player start position settings
        PLAYER_START_SCREEN_X = game_settings["width"] // 2
        PLAYER_START_SCREEN_Y = game_settings["height"] // 2

        entity_group = pygame.sprite.Group()
        break
    except FileNotFoundError:
        print("Invalid input of directory")

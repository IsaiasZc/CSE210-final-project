from pathlib import Path
import os

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "TowerDefense Alpha"

# The path forr he enemies
SCREEN_PATH = [[600,820],[600,720],[230,720],[230,220],[790,220],[790,520],[610,520],[610,340],[410,340],[410,620],[970,620],[970,110],[620,110],[620,-10]]

############################
TL = 1
TR = 0

# MOTION
LERP = 0.001
SPEED_MULTIPLIER = 5
MOVE_SPEED = 200
MOVE_SPEED_CHARGED = 0.8 * MOVE_SPEED

ENTITY_MS = 40

# ENTITY TYPES
E_ANT = 1
E_MOSQUITO = 2
E_SPIDER = 3
E_DUNG_BEETLE = 4
E_HP = 75

T_SPRAY = 10
T_LAMP = 11
T_VACUUM = 12
T_DMG = 30
T_COOLDOWN = 1
DMG_MULTIPLIER = 3
T_RANGE = 3

# ROWS
TOP_ROW = 0
MID_ROW = 1
BOT_ROW = 2

# VOLUME
VOLUME = 0.5

# UPDATE RATES FOR ENTITIES
UR_PLAYER = 1

UR_MOSQUITO = 5
UR_ANT = 25
UR_SPIDER = 25
UR_DUNG_BEETLE = 10

UR_SPRAY = 10
UR_LAMP = 8
UR_VACUUM = 10

UR_DMG = 5

# num of frames
F_ANT = 2
F_MOSQUITO = 2
F_SPIDER = 2
F_DUNG_BEETLE = 2

F_SPRAY = 4
F_LAMP = 4
F_VACUUM = 4

# BASE POSITIONS FOR TURRETS AND PLAYER
BP_PLAYER = [14, 7]
BP_SPRAY = [10, 12]
BP_LAMP = [15, 9]
BP_VACUUM = [11, 4]

# WAVES MANAGER
PREMADE_WAVES = 50

# TILES POSITIONS CHANGING DIRECTIONS
TILE_UP = [[12, 11], [16, 11], [29, 11], [7, 3], [8, 4], [15, 1], [16, 4]]
TILE_DOWN = [[4, 13], [6, 12], [13, 12], [20, 14], [22, 13], [24, 8], [12, 5], [20, 5], [21, 4]]
TILE_RIGHT = [[4, 12], [6, 11], [12, 12], [16, 14], [20, 13], [22, 11], [29, 12], [24, 7], [7, 4], [8, 5], [12, 1],
              [15, 4], [16, 5], [20, 4], [21, 3], [13, 11]]

PATH = {}
PATH['project'] = Path(os.path.dirname(__file__))
PATH['img'] = PATH['project'] / "images"
PATH['sound'] = PATH['project'] / "sounds"
PATH['maps'] = PATH['project'] / "tmx_maps"
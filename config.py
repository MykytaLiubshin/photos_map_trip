from os import path

CURRENT_DIRECTORY = path.dirname(path.realpath(__file__))
IMAGES_DIR_NAME = path.join(CURRENT_DIRECTORY, 'static', 'images')
IMAGES_DIR = path.join(CURRENT_DIRECTORY, IMAGES_DIR_NAME)
DEFAULT_DUMP_FILENAME = "all_data.xlsx"

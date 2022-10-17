from os import path, walk
from image_metadata_extraction import extract_all_metadata, decode_gps_data
from config import IMAGES_DIR, CURRENT_DIRECTORY
import pandas as pd


def run():
    print("Running")
    files_in_images = []
    for root, dirs, files in walk(path.join(IMAGES_DIR)):
        files_in_images = []
    metadata = extract_all_metadata(path.join(IMAGES_DIR, "IMG_20220808_123403.jpg"))
    gps_data = decode_gps_data(metadata)
    print(gps_data)
    data = pd.DataFrame(gps_data, index=[0])
    data.to_excel(path.join(CURRENT_DIRECTORY, "IMG_20220808_123403.jpg.xlsx"))

if __name__ == '__main__':
    run()

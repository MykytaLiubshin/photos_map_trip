from os import path, walk
from image_metadata_extraction import extract_all_metadata, decode_gps_data
from config import IMAGES_DIR, CURRENT_DIRECTORY, DEFAULT_DUMP_FILENAME
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


def get_all_needed_data(directory_path=IMAGES_DIR):
    files_in_images = []
    for _, _, files in walk(path.join(directory_path)):
        files_in_images = files

    all_data = pd.DataFrame()
    for i in range(len(files_in_images)):
        filename = files_in_images[i]
        metadata = extract_all_metadata(path.join(directory_path, filename))
        gps_data = decode_gps_data(metadata)
        if not gps_data:
            continue

        data = pd.DataFrame(gps_data, index=[filename])
        for key in metadata.keys():
            if key != "GPSInfo":
                data[key] = metadata[key]
        all_data = pd.concat([all_data, data])

    return all_data

def load_data(dirpath=CURRENT_DIRECTORY, filename=DEFAULT_DUMP_FILENAME):
    return pd.read_excel(path.join(CURRENT_DIRECTORY, filename))

def dump_data(all_data, dirpath=CURRENT_DIRECTORY, filename=DEFAULT_DUMP_FILENAME):
    all_data.to_excel(path.join(CURRENT_DIRECTORY, filename))

def run():
    all_data = load_data()
    y_x = all_data[["latitude", "longitude"]]
    ymax = max(y_x["latitude"])
    ymin = min(y_x["latitude"])
    xmax = max(y_x["longitude"])
    xmin = min(y_x["longitude"])
    print(f"ymax = {ymax}")
    print(f"ymin = {ymin}")
    print(f"xmax = {xmax}")
    print(f"xmin = {xmin}")
    yrange = ymax - ymin
    xrange = xmax - xmin
    biggest_range_y = yrange > xrange
    norm_y = list(map(lambda y:round((y - ymin)/yrange, 6),y_x['latitude']))
    norm_x = list(map(lambda x:round((x - xmin)/yrange, 6),y_x['longitude']))
    y_x['latitude'] = norm_y
    y_x['longitude'] = norm_x
    print(y_x)
    fig, ax = plt.subplots(figsize=(12,12))
    sns.scatterplot(data = y_x, x='longitude', y='latitude', ax=ax)
    fig.show()


if __name__ == '__main__':
    run()

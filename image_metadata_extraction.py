from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from math_utils import _convert_to_degress
needed_tags = [
    "DateTimeOriginal",
    "DateTimeDigitized",
    "Make",
    "Model",
    "GPSInfo",
]

def extract_all_metadata(filename):
    with Image.open(filename) as image:
        exifdata = image.getexif()

    data_dict = {}

    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = str(TAGS.get(tag_id, tag_id))
        data = exifdata.get(tag_id)

        # decode bytes
        if isinstance(data, bytes):
            data = data.decode()

        data_dict[tag] = data
    return data_dict

def decode_gps_data(filedata):
    GPSInfo = filedata['GPSInfo']

    data_dict = {
        "latitude_ref": GPSInfo[1],
        "latitude": str(_convert_to_degress(GPSInfo[2])),
        "longitude_ref": GPSInfo[3],
        "longitude": str(_convert_to_degress(GPSInfo[4])),
    }

    return data_dict

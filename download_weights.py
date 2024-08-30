import gdown
from src.utils.general import ROOT
import os


DETECTOR_URL = "https://drive.google.com/drive/folders/1OmxDFzY65rj5Nxtdz4S1XWT2QdrkwKZr"
POSE_URL = "https://drive.google.com/drive/folders/1XjlLCDhuuDNfYXmPo2rMr_RUSUDp2WMI"
SEG_URL = "https://drive.google.com/drive/folders/1tLPndFlSsV9SR8JKG2I2ijLuqsWkcHzt"

gdown.download_folder(
    url=DETECTOR_URL, 
    output=os.path.join(ROOT, "weights/detection"), 
    quiet=False,
    use_cookies=False)

gdown.download_folder(
    url=POSE_URL, 
    output=os.path.join(ROOT, "weights/pose"), 
    quiet=False,
    use_cookies=False)

gdown.download_folder(
    url=SEG_URL, 
    output=os.path.join(ROOT, "weights/segmentation"), 
    quiet=False,
    use_cookies=False)

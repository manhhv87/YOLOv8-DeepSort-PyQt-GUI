# YOLOv8-DeepSort/ByteTrack-PyQt-GUI
a GUI application, which uses YOLOv8 for  Object Detection/Tracking, Human Pose Estimation/Tracking from images, videos or camera. 

All python scripts performing detection, pose and segmentation using the YOLOv8 model in ONNX.

![GUI](./data/ui.png)

Supported AI tasks:
- [x] Detection
- [x] Pose Estimation
- [x] Segmentation

Supported Models:
- [x] YOLOv8n
- [x] YOLOv8s
- [x] YOLOv8m
- [x] YOLOv8l
- [x] YOLOv8x

Supported Trackers:
- [x] DeepSort
- [x] ByteTrack

Supported Input Sources:
- [x] local files: images or videos
- [x] Camera
- [x] RTSP-Stream

## Install

ubuntu20 apt-get update error:ModuleNotFoundError: No module named ‘apt_pkg‘
```
sudo apt-get remove --purge python-apt
sudo apt-get install python-apt -f
cd /usr/lib/python3/dist-packages/
sudo cp apt_pkg.cpython-38-x86_64-linux-gnu.so apt_pkg.cpython-39-x86_64-linux-gnu.so
```

Install required packages with pip:

```shell
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
pip install -r requirements.txt
```

or with conda:

https://repo.anaconda.com/archive/ --> Anaconda3-2023.03-1-Linux-x86_64.sh

```shell
conda env create -f environment.yml

# activate the conda environment
conda activate yolov8_gui

python3 -m pip install opencv-python opencv-python-headless
```

## Download weights

Download the model weights：

``````shell
python download_weights.py
``````

The model files are saved in the **weights/** folder.

## Run

```shell
python main.py
```


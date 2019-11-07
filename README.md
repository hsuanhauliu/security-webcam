# Security Webcam

A security camera system using computer webcam that auto-saves clips when a person's face is detected.

## How It Works

- After the program is executed, it will start recording via webcam on your computer. All frames are saved in a buffer which is used to keep only the most recent frames (size depends on the buffer_length set initially).
- Every time a face is detected, it will start recording all the frames until a few seconds after the face is no longer within the camera frame. The number of seconds it will wait before saving the clip also equals to the buffer_length. A .mov file will be created and named after the recorded time.
- The program will then resume to recording and repeat the same process until the user terminates the program.

## Features

- Custom FPS and buffer length settings.
- Real-time face detection.
- CLI provides easy execution.
- Ability to see the recording in real-time.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

See [here](requirements.txt) for a complete list of required modules.
- Python >= 3.6
- [face_recognition](https://github.com/ageitgey/face_recognition) >= 1.2.3
- OpenCV >= 3.4.2


### Installation

A step by step series of examples that tell you how to get a development env running.

Use the following command to install all packages.
```
pip install -r requirements.txt
```

Build the program from source.s
```
git clone https://github.com/hsuanhauliu/security-webcam
cd security-webcam
pip install .
```

### Usage

#### CLI

Follow the commands below to run the program.

```
security_webcam [-h] [-v] [-s] [-o OUTPUT] top_fps buffer_length
```
- top_fps: maximum fps allowed.
- buffer_length: the length (in seconds) of the segments before and after a face is detected.
- Use -o flag to specify video output path. The default path is the current directory where the program is executed.

Example:
```
security_webcam -v -o recordings 30 10
```

To quit the program, simply press Ctrl-C or ESC if -s flag is used.

#### Import As Python Package

You can also import the package in your code. See [demo.py](demo.py) for example.


## Future Works
- Use motion detection instead of facial recognition to decide when to start recording.
- Implement maximum video length to segment long video recordings.
- Add threads for recording and saving videos.

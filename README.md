# Security Webcam

A motion-sensing webcam-based security system that auto-saves important footages.

## How It Works

- After the program starts, it will start recording via webcam on your computer. All frames are saved in a buffer which is used to save the most recent frames (default to 5 seconds) before any motion is detected.
- Every time a movement is detected, it will start saving all the frames until motion is no longer being detected. All videos are saved in .mov format and stored in the specified directory (default to "recordings/" directory).
- The program will then resume to recording and repeat the same process until the user terminates the program.
- If the footage is longer than a certain amount of time (default to 5 minutes), the footage will be segmented into smaller video files.

## Features

- Customizable settings (fps, buffer length, segmentation length, etc)
- Motion detection ability to trigger recording.
- CLI provides easy execution.
- Ability to see the video stream happening in real-time.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

See [here](requirements.txt) for a complete list of required packages.
- Python >= 3.6
- OpenCV >= 3.4.2


### Installation

A step by step series of examples that tell you how to get a development env running.

Use the following command to install all packages.
```
pip install -r requirements.txt
```

Build the program from source.
```
git clone https://github.com/hsuanhauliu/security-webcam
cd security-webcam
pip install .
```

### Usage

#### CLI

To start the program with default settings, simply type

```
security_webcam
```

It also has options for you to customize the settings. You can also modify the config.json file for settings.

```
security_webcam [-h] [-v] [-t] [-s] [-o OUTPUT] [--fps] [--temp_buffer_len] [--vid_buffer_len] [--max_len]
```

- -h: help flag
- -v: verbose for showing more messages.
- -j: use config.json in the root directory for configuration. Note that by using this flag, all other flags will be ignored.
- -t: show time on the recordings. True by default.
- -s: show webcam stream.
- -o: output path. Default to "recordings/" directory.
- --top_fps: maximum fps allowed. Default to 30 fps.
- --temp_buffer_len: length (in seconds) of the video segments before and after important footage. Default to 5 seconds.
- --vid_buffer_len: length (in seconds) of the actual captured footage. Default to 60 seconds.
- --max_len: maximum length (in minutes) of the actual footage. Default to 5 minutes.


Example:
```
# Manually trigger flags for settings.
security_webcam -v -o recordings/ --fps 15 --max_len 3

# Use config.json file for settings.
security_webcam -j
```

To quit the program, simply press Ctrl-C or ESC if -s flag is used.

#### Import As Python Package

You can also import the package in your code. See [demo.py](demo.py) for examples.

## Demo
![screenshot](imgs/demo.gif "demo")

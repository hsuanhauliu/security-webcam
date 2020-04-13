# Security Webcam

A motion-sensing webcam-based security system that auto-saves important footages.

## How It Works

When motion is detected, the program will start saving all the frames until motion is no longer being detected. All videos are saved in .mov format and stored in a folder (default to "recordings/" folder in the current directory).

## Features

- Customizable settings (fps, buffer length, segmentation length, etc)
- Motion detection ability to trigger recording.
- CLI provides easy execution.
- Ability to see the video stream happening in real-time.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

See [here](./pyproject.toml) for a complete list of required packages.
- python = "^3.7"
- numpy = "^1.18.2"
- opencv-python = "^4.2.0"

### Installation

A step by step series of examples that tell you how to get a development env running.

```bash
$ git clone https://github.com/hsuanhauliu/security-webcam
$ cd security-webcam
$ pip install .
```

### Usage

#### CLI

To start the program with default settings, simply type

```bash
$ security_webcam
```

It also has options for you to customize the settings. You can also modify the config.json file for settings.

```bash
$ security_webcam [-h] [-v] [-t] [-s] [-o OUTPUT] [--fps] [--temp_buffer_len] [--vid_buffer_len] [--max_len]
```

-h: help flag  
-v: verbose for showing more messages.  
-j: read settings from the specified JSON file. See sample-config.json for an example. Note that by using this flag, all other flags will be ignored.  
-t: show time on the recordings. True by default.  
-s: show webcam stream.  
-o: output path. Default to "recordings/" directory.  
--top_fps: maximum fps allowed. Default to 30 fps.  
--temp_buffer_len: length (in seconds) of the video segments before and after important footage. Default to 5 seconds.  
--vid_buffer_len: length (in seconds) of the actual captured footage. Default to 60 seconds.  
--max_len: maximum length (in minutes) of the actual footage. Default to 5 minutes.

### Example

Manually trigger flags for settings.
```bash
$ security_webcam -v -o recordings/ --fps 15 --max_len 3
```

Use config.json file for settings.
```bash
$ security_webcam -j sample-config.json
```

#### Run via Poetry

You can also run the program directly with poetry.

```bash 
$ poetry install # install dependencies
$ poetry run python security_webcam
```

To quit the program, simply press Ctrl-C or ESC if -s flag is used.

#### Import As Python Package

You can also import the package in your code. See [demo.py](demo.py) for examples.

## Demo
![screenshot](imgs/demo.gif "demo")

## Development Guideline

- Run pylint (at least 8.5/10) and flake8 to check code.
- Use Black and iSort to format code.
- Use Bandit, Vulture, and Safety to check security vulnerabilities.
- Generate setup.py from pyproject.toml with DepHell with `~/Library/Python/3.7/bin/dephell deps convert`.
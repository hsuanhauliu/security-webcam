# Security Webcam

A security camera system using computer webcam that auto-saves clips when a person's face is detected.

How it works:
- After the program is executed, it will start using the webcam to record. All frames are saved in a buffer which will keep only the recent frames (depending on the buffer_length set).
- Once a face is detected, it will start recording all the frames until a few seconds after the face is no longer in the frame (the wait time is also depending on the buffer_length). After that, an mov file will be created and the name of the file is the recorded time.
- The program will then resume to recording repeat the same process until the user terminates the program.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python >= 3.6
- [face_recognition](https://github.com/ageitgey/face_recognition) >= 1.2.3
- OpenCV >= 3.4.2

### Installation

A step by step series of examples that tell you how to get a development env running.

```
git clone https://github.com/hsuanhauliu/security-webcam
cd security-webcam
pip install .
```

### Usage

Follow the commands below to run the program.

```
security_webcam [top_fps] [buffer_length]
```
- top_fps: maximum fps allowed.
- buffer_length: the length (in seconds) of the segments before and after a face is detected.
- Use -o flag to specify video output path. The default path is the current directory where the program is executed.

Example:
```
python3 main.py -v -o recordings/ 30 10
```

You can also import the package in your code. See demo.py for example.

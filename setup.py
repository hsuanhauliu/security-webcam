from setuptools import setup

setup(
    name='security_webcam',
    version='0.2',
    author='Hsuan-Hau Liu',
    description='Simple security camera system right on your computer.',
    packages=['security_webcam',],
    install_requires=['opencv-python', 'face_recognition'],
    entry_points={
        'console_scripts': [
            'security_webcam=security_webcam.__main__:main'
        ]
    }
)

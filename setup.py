from setuptools import setup

setup(
    name='security-webcam',
    version='0.1',
    author='Hsuan-Hau Liu',
    description='Simple security camera system right on your computer.',
    packages=['security_webcam',],
    install_requires=['opencv-python', 'numpy'],
    entry_points={
        'console_scripts': [
            'security_webcam=security_webcam.__main__:main'
        ]
    }
)

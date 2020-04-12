from setuptools import setup

setup(
    name='security-webcam',
    version='0.2',
    author='Hsuan-Hau Liu',
    description='Simple security camera system right on your computer.',
    url='https://github.com/hsuanhauliu/security-webcam',
    packages=['security_webcam'],
    package_dir={'security_webcam': 'security_webcam'},
    install_requires=[
        'opencv-python>=4.1.1.26',
        'numpy>=1.17.4'
    ],
    entry_points={
        'console_scripts': [
            'security_webcam=security_webcam.__main__:main'
        ]
    },
    python_requires='>=3.6'
)

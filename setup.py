"""MazeSolver python package configuration."""

from setuptools import setup

setup(
    name='MazeSolver',
    version='0.0.0',
    packages=['MazeSolver'],
    include_package_data=True,
    install_requires=[
        'numpy==1.18.1',
        'matplotlib',
        'imageio',
        'opencv-contrib-python',
    ],
)

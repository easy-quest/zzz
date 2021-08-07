from setuptools import setup

setup(
    name='zzz',
    version='0.1.0',
    py_modules=['zzz'],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'zzz = zzz:up',
        ],
    },
)

from setuptools import setup
setup(
    name = 'bevdb',
    version = '0.1.0',
    packages = ['bevdb'],
    entry_points = {
        'console_scripts': [
            'bevdb = bevdb.__main__:main'
        ]
    })
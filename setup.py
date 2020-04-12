from setuptools import setup
setup(
    name = 'dyom-cli',
    version = '0.1.0',
    packages = ['dyom'],
    entry_points = {
        'console_scripts': [
            'dyom = dyom.__main__:main'
        ]
    })

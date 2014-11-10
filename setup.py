from setuptools import setup, find_packages

setup(
    name = "piphelper",
    version = "0.1",
    packages = find_packages(),
    entry_points={
        'console_scripts': [
            'piphelper = piphelper.command:main'
        ]
    }
)

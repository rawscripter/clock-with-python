from setuptools import setup

APP = ['clock.py']
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)

# to build the app run this command
# python3 setup.py py2app

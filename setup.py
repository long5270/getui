import os
from setuptools import setup, find_packages
ROOT = os.path.dirname(os.path.realpath(__file__))

setup(
    name = "getui",
    version = "4.1.0.0",
    keywords = ("getui", "个推"),
    description = "Ge tui push python api",
    long_description = open(os.path.join(ROOT, 'README.md'), encoding='utf-8').read(),
    license = "MIT Licence",

    url = "https://github.com/uimeet/getui",
    author = "Getui",
    author_email = "business@getui.com",

    packages = find_packages(exclude=['*.test', '*.test.*', 'test.*', 'test', 'test.py']),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)

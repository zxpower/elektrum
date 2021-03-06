from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='elektrum',
    version='0.1',
    url='https://github.com/zxpower/elektrum',
    author='Reinholds Zviedris (zxpower)',
    author_email='reinholds@zviedris.lv',
    description="Utility to authorize and scrape your smart meter consumption data from Elektrum website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0 License",
        "Operating System :: OS Independent",
    ],
    packages=['elektrum'],
    python_requires=">=3.6",
)

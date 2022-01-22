import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(name='elektrum',
    version='0.1',
    description='Elektrum Electricity Consumption Scraper',
    url='https://github.com/zxpower/ha-elektrum',
    author='zxpower',
    author_email='reinholds@zviedris.lv',
    description="Utility to authorize and scrape your smart meter data from Elektrum website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "elektrum"},
    packages=['elektrum'],
    python_requires=">=3.6",
)

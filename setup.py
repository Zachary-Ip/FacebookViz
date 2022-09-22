from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="FacebookViz",
    version="0.0.1",
    packages=["FacebookViz"],
    include_package_data=True,
    author="Zach Ip",
    description="Tools to look at stats and vizualizations of a chat history",
    long_description=long_description,
    url="https://github.com/Zachary-Ip/FacebookViz",
    license="GNU GPLv3",
    install_requires=[
        "pandas",
        "matplotlib",
        "numpy",
        "ipykernel",
    ],
)

import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="dpern",
    version="0.0.3",
    description="Describe PERsian Numbers",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/amirashabani/dpern",
    author="Amir A. Shabani",
    author_email="amirashabani@zoho.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    packages=["dpern"],
    setup_requires=["wheel"]
)

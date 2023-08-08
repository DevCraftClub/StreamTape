from setuptools import setup

setup(
    name="streamtape",
    version="1.0.1",
    description="Unofficial python api wrapper from https://streamtape.com",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    keywords="api streamtape stream video hosting unlimited",
    url="https://github.com/DevCraftClub/StreamTape",
    author="Maxim Harder",
    author_email="dev@devcraft.club",
    packages=["streamtape"],
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    zip_safe=False,
)
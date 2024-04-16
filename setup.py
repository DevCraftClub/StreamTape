from setuptools import setup

setup(
	name="streamtape",
	version="1.0.3",
	description="Unofficial python api wrapper from https://streamtape.com",
	long_description=open("README.md", "r").read(),
	long_description_content_type="text/markdown",
	keywords="api streamtape stream video hosting unlimited",
	url="https://github.com/DevCraftClub/StreamTape",
	authors=[{
		"name" : "Maxim Harder",
		"email": "dev@devcraft.club",
	}],
	packages=["streamtape"],
	install_requires=[
		"requests",
	],
	requires_python=">=3.8",
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3.0",
		"Operating System :: OS Independent",
	],
	zip_safe=False,
)

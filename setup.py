from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in zakaterp/__init__.py
from zakaterp import __version__ as version

setup(
	name="zakaterp",
	version=version,
	description="zakat",
	author="avu",
	author_email="avu@gmaiil.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

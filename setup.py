from setuptools import setup, find_packages

setup(
	name="gac",
	version="1.0.0",
	entry_points={
		"console_scripts": [
			"gac = gac.main:main"
		]
	},
	packages=find_packages(),
)

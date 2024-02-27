from setuptools import setup, find_packages
from typing import List

#Hypen_E_Dot = '-e .'

'''def get_requiremet(file_path: str) -> List[str]:
    ''
    # this function returns the requirements list
    ''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]
        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)
    return requirements'''

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     


__version__ = "0.0.4"
REPO_NAME = "PythonPackage"
PKG_NAME= "PythonDatabaseconnectorpkg"
AUTHOR_USER_NAME = "pavansai247"
AUTHOR_EMAIL = "pavansai16247@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    #install_requires= get_requiremet("./requirements_dev.txt"),
    
    )
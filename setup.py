from setuptools import setup, find_packages
from typing import List


def get_requirements_list() -> List[str]:
    """
    Returns a list of requirements from the requirements.txt file, excluding
    the "-e ." line which is used to install the current package in editable mode.

    Returns:
        List[str]: a list of requirements read from the requirements.txt file
    """
    requirements_list = []
    try:
        with open("requirements.txt", "r") as file:
            for line in file:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirements_list

setup(
    name="networksecurity",
    version="0.0.1",
    author="sehajsingh",
    author_email="singhsp7977@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements_list(),
)
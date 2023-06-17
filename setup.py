from setuptools import find_packages,setup
from typing import List

hyphen_cons='-e .'
def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[r.replace("\n","") for r in requirements]

        if hyphen_cons in requirements:
            requirements.remove(hyphen_cons)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Dishaa',
    author_email='dishaaagarwal.100@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
from setuptools import find_packages, setup
from typing import List

Hypen_e_dot = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    The function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ req.replace('\n',' ') for req in requirements] 

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    
    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    description='a base ml project',
    author='shivam yadav',
    author_email='shivamyadav62320@gmail.com',
    packages=find_packages(), #it will look for packages associated with all the __init__.py files in the project
    requires = get_requirements('requirements.txt') 
)
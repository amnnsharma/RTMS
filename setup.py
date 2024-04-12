from setuptools import find_packages, setup

def get_requirements(file_path):
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

    print(requirements)
    if requirements[-1]=="-e .":
        print("Here")
        return requirements[:-1]
    else:
        return requirements
    


setup(
    name="RTMS Project Local",
    version="1.0",
    author="Aman Sharma",
    author_email="amnnsharma@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
import os
import sys
from setuptools import setup, find_packages

# check for root user
if os.getuid() != 0:
    print('ERROR: Need to run as root')
    sys.exit(1)

# Install the requirements if the system does not have it installed
print('INFO: Checking and installing requirements')
os.system('! dpkg -S python-imaging-tk && apt-get -y install python-imaging-tk')

# Generate the requirements from the file for old instructions
print('INFO: Generating the requirements')
packages = []
for line in open('requirements.txt', 'r'):
    if not line.startswith('#'):
        packages.append(line.strip())

# Run setuptools for pip
setup(
    name='Magic mirror',
    version='1.0.0',
    description='Magic mirror displays time, schedule, weather, calendar events and current news headlines',
    author='Ram Pratik Aadityan S',
    url='https://github.com/SrpAadityan/Magic-Mirror',
    install_requires=packages,
    packages=find_packages(),
)

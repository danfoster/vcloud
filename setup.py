import os
from setuptools import setup, find_packages


setup(
    name = "vcloud",
    version = "0.0.1",
    author = "Dan Foster",
    author_email = "dan@zem.org.uk",
    description = "libvirt based cloud-init command line",
    license = "Apache License 2.0",
    packages = find_packages(),
    long_description="""libvirt based cloud-init command line""",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    install_requires=[
        "click",
        "libvirt-python",
        "tabulate",
        "pyyaml",
    ],
    entry_points = {
        'console_scripts': [
            'vcloud=vcloud.cli:main'
        ],
        
    }
)

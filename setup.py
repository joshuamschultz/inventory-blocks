import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setup(
    name="inventory_blocks",
    version="0.0.1",
    author="Joshua Schultz  ",
    author_email="joshuamschultz@gmail.com",
    description="A package to convert your Jupyter Notebook",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/joshuamschultz/inventory-blocks",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
setuptools.setup(
    name="inventory-blocks",
    version="0.0.1",
    author="Joshua Schultz",
    author_email="joshuamschultz@gmail.com",
    description="A Python library of blocks used in creating in custom inventory optimization models.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0-only",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)
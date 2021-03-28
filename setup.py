import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytipeee", 
    version="1.1.2",
    author="Carlo Alberto Carrucciu",
    author_email="carloalbertocarrucciu@outlook.it",
    description="Python scraper for tipeee",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alberts96/pytipeee",
    project_urls={
        "Bug Tracker": "https://github.com/alberts96/pytipeee/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
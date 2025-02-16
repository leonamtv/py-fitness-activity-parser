from setuptools import setup, find_packages

setup(
    name="fitness activity parser",
    version="1.0",
    author="Leo Vasconcelos (@leonamtv)",
    python_requires=">=3.10",
    packages=find_packages(exclude=['test']),
    install_requires=[],
    project_urls={
        "Source": "https://github.com/leonamtv/py-fitness-activity-parser"
    }
)
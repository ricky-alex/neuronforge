from setuptools import setup, find_packages

setup(
    name="neuronforge",
    version="0.1.0",
    author="Ricky Alex",
    packages=find_packages(),
    python_requires=">=3.9",
    extras_require={"dev": ["pytest>=7.0"]},
)

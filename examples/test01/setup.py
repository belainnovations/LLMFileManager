from setuptools import setup, find_packages

setup(
    name="shape-inheritance-example",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytest==7.3.1",
        "sphinx==6.2.1",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple example project demonstrating inheritance with geometric shapes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/shape-inheritance-example",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
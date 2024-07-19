from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="llm_file_operations",
    version="0.1.0",
    author="Bela Komoroczy",
    author_email="bela.komoroczy@belainnovations.com",
    description="A tool for performing file operations using LLM-generated instructions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/llm_file_operations",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pyperclip",
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "llm_file_operations=llm_file_operations.src.main:main",
        ],
    },
)
from setuptools import setup, find_packages

setup(
    name="pygenieacs",  # PyPI package name
    version="0.1.0",    # Update this with each release
    description="Python API client for GenieACS TR-069 / CWMP server",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="uberkie",
    author_email="your@email.com",
    url="https://github.com/uberkie/pygenieacs",
    packages=find_packages(exclude=["tests", "examples"]),
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
        "toml>=0.10.0",  # optional if you parse pyproject.toml internally
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="genieacs acs tr069 cwmp client networking",
    include_package_data=True,
)

from setuptools import setup, find_packages

setup(
    name="forgecord",
    version="0.1.0",
    author="Owen Pink",
    author_email="owenpink@proton.me",
    description="A Discord API wrapper using JSON for configuration.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ImLimiteds/ForgeCord",
    packages=find_packages(),
    install_requires=[
        "discord.py>=2.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

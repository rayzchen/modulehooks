from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="modulehooks",
    version="1.0.0",
    author="Ray Chen",
    author_email="tankimarshal2@gmail.com",
    description="Wrapping modules with attribute hooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rayzchen/modulehooks",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[],
    py_modules=["modulehooks"],
    python_requires=">=3.6",
)

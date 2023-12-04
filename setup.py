#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open("requirements.txt", encoding="utf-8") as requirements_file:
    requirements = requirements_file.readlines()

test_requirements = []

setup(
    author="Kestin Goforth",
    author_email="kgoforth1503@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="Automaically update your desktop wallpaper, how ever often you want.",
    entry_points={
        "console_scripts": [
            "apod_wallpaper_updater=apod_wallpaper_updater.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords="apod_wallpaper_updater",
    name="apod_wallpaper_updater",
    packages=find_packages(
        include=["apod_wallpaper_updater", "apod_wallpaper_updater.*"]
    ),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/kforth/apod_wallpaper_updater",
    version="0.1.0",
    zip_safe=False,
)

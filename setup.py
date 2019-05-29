""" joe's python test package
"""

import setuptools

REQUIRED = [
        "numpy",
        "pandas"
        ]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
        name="joe_pypack_test",
        version="0.0.1",
        author="joe",
        description="python packaging test package",
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        url="https://github.com/jazzathoth/pypack_test_repo",
        packages=setuptools.find_packages(),
        python_requires=">=3.1",
        install_requires=REQUIRED,
        classifiers=[
            "Programming Language :: Python ::3",
            "Licesne :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ],
        )

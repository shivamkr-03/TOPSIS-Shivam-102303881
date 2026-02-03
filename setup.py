from setuptools import setup, find_packages

setup(
    name="TOPSIS-Shivam-102303881",   # PyPI name 
    version="0.0.1",
    author="Shivam Kumar",
    description="TOPSIS implementation using Python",
    packages=find_packages(),        # finds topsis_shivam_102303881
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis=topsis_shivam_102303881.topsis:main"
        ]
    },
)

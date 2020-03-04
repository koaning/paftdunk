import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


base_packages = ["numpy>=1.15.4", "scipy>=1.2.0", "scikit-learn>=0.20.2",
                 "pandas>=0.23.4", "matplotlib>=3.0.2", "plotnine>=0.5.1",
                 "jupyter>=1.0.0", "jupyterlab>=0.35.4", "tqdm>=4.28.1",
                 "Click>=7.0", "fastapi>=0.52.0", "uvicorn>=0.11.3"]

dev_packages = ["pip", "pytest-cov", "pytest", "flake8", "mkdocs>=1.1", 
                "mkdocs-material>=4.6.3", "pre-commit>=2.1.1", "mkdocs-jupyter==0.10.2"]

module_name = "paftdunk"

setup(
    name=module_name,
    version="0.0.1",
    packages=find_packages(exclude=['data', 'notebooks']),
    long_description=read('readme.md'),
    install_requires=base_packages,
    entry_points={
        'console_scripts': [
            f'{module_name}cli = {module_name}.cli:main',
        ],
    },
    extras_require={
        "dev": dev_packages
    }
)

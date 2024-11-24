from setuptools import setup, find_packages

setup(
    name='circuit-simulator',
    version='0.1.0',
    description='A program to draw and simulate electrical circuits',
    author='Cameron-Bains',
    author_email='cmbains12@gmail.com',
    url='https://github.com/cmbains/circsim',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'sympy',
        'pygame',
        'setuptools'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
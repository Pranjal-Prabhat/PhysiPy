from setuptools import setup, find_packages

setup(
    name='physics',
    version='0.1.0',
    description='A library to make calculations in physics easy',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Pranjal Prabhat',
    author_email='pranjalprabhat1@gmail.com',
    url='https://github.com/yourusername/physics',
    packages=find_packages(),
    install_requires=[
        'sympy',

    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

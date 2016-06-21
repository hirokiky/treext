from setuptools import setup, find_packages

long_description = open('./README.md').read()


setup(
    name='treext',
    version='0.1',
    packages=find_packages(),
    description='TREE eXTructor: Extracting file tree structure as JSON.',
    long_description=long_description,
    url='https://github.com/hirokiky/treext',
    author='Hiroki KIYOHARA',
    author_email='hirokiky@gmail.com',
    license='MIT',
    entry_points={
        'console_scripts': [
            'treext = treext.main:main',
        ]
    }
)
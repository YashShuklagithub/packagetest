from setuptools import setup, find_packages

setup(
    name='myapp',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'django>=3.0',
    ],
    include_package_data=True,
    description='A simple Hello World app',
    author='Yash Shukla',
    author_email='yash.shukla.csds21@ggits.net',
)

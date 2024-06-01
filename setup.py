from setuptools import setup, find_packages

setup(
    name='Tower of Hanoi',
    version='0.1.0',
    packages=find_packages(),
    author='kubzar',
    author_email='jakub.pawel.zarebski@gmail.com',
    description='The Tower of Hanoi puzzle is a classic problem often used in computer science and mathematics.',
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kubzar/Tower-of-Hanoi/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

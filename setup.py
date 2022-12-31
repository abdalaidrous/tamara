import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tamara',
    version='0.1.0',
    author="Abdullah AL-Aidrous",
    author_email="abd.alaidrous@gmail.com",
    description='Tamara Python SDK',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/abdalaidrous/tamara-sdk-pyhton/',
    project_urls={
        "Bug Tracker": "https://github.com/abdalaidrous/tamara-sdk-pyhton/-/issues",
        "repository": "https://github.com/abdalaidrous/tamara-sdk-pyhton/",
    },
    install_requires=[
        'requests>=2.28.1, <3.0',
        'jsonpickle>=3.0.1 , <4.0',
        'python-dateutil>=2.8.2, <3.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "tamara"},
    packages=setuptools.find_packages(where="tamara"),
    py_modules=['__init__', 'base', 'client', 'configuration'],
    python_requires=">=3.6"
)

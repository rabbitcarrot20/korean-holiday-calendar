import setuptools
 
with open("README.md", "r",encoding = 'UTF8') as fh:
    long_description = fh.read()

project_urls_ = {
    'Homepage 2' : 'https://github.com/gadarangeo/korean-holiday-calendar'
}
    
setuptools.setup(
    name="korean_holiday_calendar",
    version="1.0.0",
    author="rabbitcarrot20, gadarangeo",
    author_email="butterfly36082@gmail.com, yuuhy1020@gmail.com",
    description="korean-specialized holiday calendar based on [python-holidays] package by dr-prodigy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rabbitcarrot20/korean-holiday-calendar",
    project_urls = project_urls_,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
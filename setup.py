import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tiktok-api",
    packages=setuptools.find_packages(),
    version="0.0.1",
    license='MIT',
    author="ShashankxD",
    author_email="sharmashashank091@gmail.com",
    description="Unofficial TikTok API wrapper in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/theshashankk",
    download_url='https://github.com/theshashankk/Py-TiktokApi/tarball/master',
    keywords=['tiktok', 'python', 'api', 'tiktok-api', 'tiktok api'],
    install_requires=[
        'requests',
        'pyppeteer',
        "pyppeteer_stealth"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    include_package_data=True
)

from setuptools import setup

setup(
    name="babla",
    version="0.1.1",
    author="Sławomir Zborowski",
    author_email="slawomir.zborowski@nokia.com",
    url='https://github.com/szborows/babla',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    description="bab.la dictionary CLI tool",
    scripts=["bin/babla"],
    install_requires=["BeautifulSoup4", "lxml"],
)

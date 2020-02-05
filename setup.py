from setuptools import setup, find_packages
setup(
    name="SpaceApiCli",
    version="0.1rc1",
    packages=find_packages(),
    scripts=["SpaceApiCli.py"],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["requests>=2.22.0"],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst", "*.md"],
        # And include any *.msg files found in the "hello" package, too:
        # "hello": ["*.msg"],
    },

    # metadata to display on PyPI
    author="Reiko Kaps",
    author_email="r31k@k4p5.de",
    description="A simple Commandline Tool to access the hackspace api",
    keywords="spaceapi hackspace cli tool",
    url="https://github.com/reikkaps/spaceapicli",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://github.com/reikkaps/spaceapicli/issues",
        "Documentation": "https://github.com/reikkaps/spaceapicli/blob/master/README.md",
        "Source Code": "https://github.com/reikkaps/spaceapicli",
    },
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ]

    # could also include long_description, download_url, etc.
)

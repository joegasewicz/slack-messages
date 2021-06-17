from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="slack-messages",
    version="0.0.1",
    description="Slack messages made easy. Send slack messages to channels from you backend api etc.",
    py_modules=["password_mixin"],
    install_requires=[
        "requests=*",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joegasewicz/slack-messages",
    author="Joe Gasewicz",
    author_email="joegasewicz@gmail.com",
)
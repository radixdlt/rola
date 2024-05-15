from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def parse_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()


requirements = parse_requirements("requirements.txt")

setup(
    name="rola",
    version="0.1.0",
    author="radix publishing",
    author_email="radixpublishing@rdx.works",
    description="A Python library for radix off ledger auth",
    url="https://github.com/radixdlt/rola",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requirements,
)

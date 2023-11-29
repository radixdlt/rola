import pipenv
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def load_dependencies(dev=False):
    # Load dependencies from Pipfile
    requirements = pipenv.convert.from_pipfile()
    if dev:
        return [str(req) for req in requirements["dev-packages"]]
    return [str(req) for req in requirements["packages"]]


setup(
    name="rola",
    version="0.1.0",
    author="radix publishing",
    author_email="radixpublishing@rdx.works",
    description="A Python library for radix off ledger auth",
    url="https://github.com/radixdlt/rola",
    packages=find_packages(),
    python_requires=">=3.8",
)

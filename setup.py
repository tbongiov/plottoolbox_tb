import shlex
import subprocess
import sys

from setuptools import setup

pkg_name = "plottoolbox"

version = open("VERSION").readline().strip()

if sys.argv[-1] == "publish":
    subprocess.run(shlex.split("cleanpy ."), check=True)
    subprocess.run(shlex.split("python setup.py sdist"), check=True)
    subprocess.run(
        shlex.split(f"twine upload --skip-existing dist/{pkg_name}-{version}.tar.gz"),
        check=True,
    )
    sys.exit()

setup()

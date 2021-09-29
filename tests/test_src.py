import re

from mypackage import __version__


def test_version():
    assert re.match(r"^\d\.\d\.\d$", __version__)

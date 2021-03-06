import unittest
import pytest

from inhoj.version import Version


class TestVersion(unittest.TestCase):

    def test_set_version(self):
        ver = Version("1.0.3")
        self.assertEqual(ver.number, "1.0.3")

    def test_version_immutable(self):
        ver = Version("1.0.3")
        with pytest.raises(TypeError) as e:
            ver.number = "1.1.3"
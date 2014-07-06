import unittest
from template.util import obscure
from template.util import deobscure

class UtilTest(unittest.TestCase):


    def test_deobscure(self):
        obs = obscure("xyz", "abc")
        deobs = deobscure(out, "abc")
        self.assertEqual("xyz", deobs)

    def test_obscure(self):
        out = obscure("xyz", "xyz")
        self.assertEqual("", out)


if __name__ == '__main__':
    unittest.main()

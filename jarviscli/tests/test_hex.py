import unittest
from tests import PluginTest
from plugins import hex
from unittest.mock import patch, call

class HexTest(PluginTest):
    def setUp(self):
        self.test = self.load_plugin(hex.binary)

    def test_0(self):
        self.test.run("0")
        self.assertEqual(self.history_say().last_text(), "0")

    def test_empty_negative(self):
        self.queue_input("-1")
        self.test.run("")
        self.assertEqual(self.history_say().last_text(), "-1")

    def test_empty_2(self):
        self.queue_input("2")
        self.test.run("")
        self.assertEqual(self.history_say().last_text(), "2")

    def test_not_a_number(self):
        self.test.run("nan")
        self.assertEqual(self.history_say().view_text(0), "That's not a number!")

    def test_2(self):
        self.test.run("2")
        self.assertEqual(self.history_say().last_text(), "2")

    def test_4932(self):
        self.test.run("4932")
        self.assertEqual(self.history_say().last_text(), "1344")

    def test_negative_1205(self):
        self.test.run("-1205")
        self.assertEqual(self.history_say().last_text(), "-4B5")

    def test_negative_9413021(self):
        self.test.run("9413021")
        self.assertEqual(self.history_say().last_text(), "8FA19D")


if __name__ == '__main__':
    unittest.main()

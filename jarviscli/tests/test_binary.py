import unittest
from tests import PluginTest
from plugins import binary


class BinaryTest(PluginTest):
    def setUp(self):
        self.test = self.load_plugin(binary.binary)

    def test_simple_1(self):
        self.test.run("0")
        self.assertEqual(self.history_say().last_text(), "0")

    def test_simple_2(self):
        self.test.run("2")
        self.assertEqual(self.history_say().last_text(), "10")

    def test_simple_3(self):
        self.test.run("73")
        self.assertEqual(self.history_say().last_text(), "1001001")

    def test_large_1(self):
        self.test.run("1978273")
        self.assertEqual(self.history_say().last_text(), "111100010111110100001")

    def test_negative_1(self):
        self.test.run("-1")
        self.assertEqual(self.history_say().last_text(), "-1")

    def test_negative_2(self):
        self.test.run("-7289")
        self.assertEqual(self.history_say().last_text(), "-1110001111001")

    def test_not_a_number(self):
        self.test.run("A")
        self.assertEqual(self.history_say().last_text(), "This is no number, right?")

    def test_empty(self):
        self.queue_input("0")
        self.test.run("")

        self.assertEqual(self.history_say().last_text(), "0")

    def test_empty_nan(self):
        self.queue_input("A")
        self.test.run("")

        self.assertEqual(self.history_say().last_text(), "This is no number, right?")

    def test_empty_negative(self):
        self.queue_input("-1")
        self.test.run("")

        self.assertEqual(self.history_say().last_text(), "-1")




if __name__ == '__main__':
    unittest.main()

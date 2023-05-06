import unittest

from improved_code import (
    build_client_base,
    develop_reputation,
    maintain_work_life_balance,
)


class TestBuildClientBase(unittest.TestCase):
    def test_build_client_base(self):
        expected_output = "Client base built successfully."
        self.assertEqual(build_client_base(), expected_output)


class TestDevelopReputation(unittest.TestCase):
    def test_develop_reputation(self):
        expected_output = "Reputation developed successfully."
        self.assertEqual(develop_reputation(), expected_output)


class TestMaintainWorkLifeBalance(unittest.TestCase):
    def test_maintain_work_life_balance(self):
        expected_output = "Work-life balance maintained successfully."
        self.assertEqual(maintain_work_life_balance(), expected_output)


if __name__ == "__main__":
    unittest.main()

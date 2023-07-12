import unittest
import bank


class TestBank(unittest.TestCase):
    def test_init(self):
        test_account = bank.Bank("Joe", 1, 100)
        self.assertEqual(test_account.name, "Joe")
        self.assertEqual(test_account.balance, 100)
        self.assertEqual(test_account.account_number, 1)

    def test_withdraw(self):
        test_account = bank.Bank("Joe", 1, 100)
        self.assertEqual(test_account.withdraw(50), 50)
        self.assertEqual(test_account.withdraw(20), 30)
        with self.assertRaises(ValueError):
            test_account.withdraw(100)

    def test_deposit(self):
        test_account = bank.Bank("Joe", 20, 100)
        self.assertEqual(test_account.deposit(50), 150)
        self.assertEqual(test_account.deposit(40), 190)

    def test_balance(self):
        test_account = bank.Bank("Joe", 1, 100)
        self.assertEqual(test_account.print_balance(), 100)
        test_account.deposit(50)
        self.assertEqual(test_account.print_balance(), 150)


if __name__ == "__main__":
    unittest.main()

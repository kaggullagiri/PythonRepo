import unittest
from src.Assignment19.util import valid_email_or_not, filtered_emails

class TestEmailValidation(unittest.TestCase):
    def test_valid_email_or_not(self):
        valid_email = 'test@example.com'
        invalid_email = 'invalid-email'

        self.assertTrue(valid_email_or_not(valid_email))
        self.assertFalse(valid_email_or_not(invalid_email))

    def test_filtered_emails(self):
        emails = ['test@example.com', 'invalid-email', 'another@example.org']

        result = filtered_emails(emails)

        self.assertListEqual(result, ['another@example.org', 'test@example.com'])

if __name__ == '__main__':
    unittest.main()
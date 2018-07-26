from django.test import TestCase
from blacklist import models
from django.db.utils import IntegrityError
from blacklist.brain import (
    is_ip_blacklisted,
    is_email_blacklisted,
    is_email_host_blacklisted,
)


class BrainTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(BrainTests, cls).setUpClass()
        cls.lower_case_blacklisted_ip = "2001:0:3238:dfe1:63::fefb"
        cls.not_blacklisted_ip = "255.254.253.251"
        cls.lower_case_blacklisted_email = "a@spam.com"
        cls.not_blacklisted_email = "a@test.com"
        cls.lower_case_blacklisted_host = "spam.com"
        cls.not_blacklisted_host = "test.com"

        ip_entry = models.IPEntry(entry_value=cls.lower_case_blacklisted_ip)
        ip_entry.save()
        email_entry = models.EmailEntry(entry_value=cls.lower_case_blacklisted_email)
        email_entry.save()
        host_entry = models.EmailHostEntry(entry_value=cls.lower_case_blacklisted_host)
        host_entry.save()

    def test_is_ip_blacklisted_with_lower_case_blacklisted_ip_and_lower_case_query(
        self
    ):
        """
        Test that checking a blacklisted ip correctly returns True.
        """

        self.assertTrue(is_ip_blacklisted(self.lower_case_blacklisted_ip))

    def test_is_ip_blacklisted_with_lower_case_blacklisted_ip_and_upper_case_query(
        self
    ):
        """
        Test that checking a blacklisted ip correctly returns True,
        even if the query is in upper-case and the ip is saved with lower case
        in our database.
        """

        self.assertTrue(is_ip_blacklisted(self.lower_case_blacklisted_ip.upper()))

    def test_is_ip_blacklisted_with_not_blacklisted_ip(self):
        """
        Test that checking a non blacklisted ip correctly returns False.
        """

        self.assertFalse(is_ip_blacklisted(self.not_blacklisted_ip))

    def test_is_email_blacklisted_with_lower_case_blacklisted_email_and_lower_case_query(
        self
    ):
        """
        Test that checking a blacklisted email correctly returns True.
        """

        self.assertTrue(is_email_blacklisted(self.lower_case_blacklisted_email))

    def test_is_email_blacklisted_with_lower_case_blacklisted_email_and_upper_case_query(
        self
    ):
        """
        Test that checking a blacklisted email correctly returns True,
        even if the query is in upper-case and the email is saved with lower case
        in our database.
        """

        self.assertTrue(is_email_blacklisted(self.lower_case_blacklisted_email.upper()))

    def test_is_email_blacklisted_with_not_blacklisted_email(self):
        """
        Test that checking a non blacklisted email correctly returns False.
        """

        self.assertFalse(is_email_blacklisted(self.not_blacklisted_email))

    def test_is_email_blacklisted_with_lower_case_blacklisted_host_and_lower_case_query(
        self
    ):
        """
        Test that checking a blacklisted email correctly returns True,
        even if only the email host is in our database.
        """

        self.assertTrue(is_email_blacklisted(f"a@{self.lower_case_blacklisted_host}"))

    def test_is_email_blacklisted_with_lower_case_blacklisted_host_and_upper_case_query(
        self
    ):
        """
        Test that checking a blacklisted email correctly returns True,
        even if the query is in upper-case and only the email host is saved
        with lower case in our database.
        """

        self.assertTrue(
            is_email_blacklisted(f"a@{self.lower_case_blacklisted_host.upper()}")
        )

    def test_is_email_blacklisted_with_not_blacklisted_host(self):
        """
        Test that checking a non blacklisted email correctly returns False.
        """

        self.assertFalse(is_email_blacklisted(f"a@{self.not_blacklisted_host}"))

    def test_is_email_host_blacklisted_with_lower_case_blacklisted_host_and_lower_case_query(
        self
    ):
        """
        Test that checking a blacklisted email host correctly returns True.
        """

        self.assertTrue(is_email_host_blacklisted(self.lower_case_blacklisted_host))

    def test_is_email_host_blacklisted_with_lower_case_blacklisted_host_and_upper_case_query(
        self
    ):
        """
        Test that checking a blacklisted email host correctly returns True,
        even if the query is in upper-case and the email host is saved with lower case
        in our database.
        """

        self.assertTrue(
            is_email_host_blacklisted(self.lower_case_blacklisted_host.upper())
        )

    def test_is_email_host_blacklisted_with_not_blacklisted_host(self):
        """
        Test that checking a non blacklisted email host correctly returns False.
        """

        self.assertFalse(is_email_host_blacklisted(self.not_blacklisted_host))


class ModelTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ModelTests, cls).setUpClass()

        cls.ip = "2001:0:3238:dfe1:63::fefc"
        cls.email = "a@spam.com"
        cls.email_host = "spam.com"

        ip_entry = models.IPEntry(entry_value=cls.ip)
        ip_entry.save()
        email_entry = models.EmailEntry(entry_value=cls.email)
        email_entry.save()
        email_host_entry = models.EmailHostEntry(entry_value=cls.email_host)
        email_host_entry.save()

    def test_add_existing_ip_in_database(self):
        """
        Test that checking if correctly we cannot add an existing ip in our database.
        """
        new_ip_entry = models.IPEntry(entry_value=self.ip)
        self.assertRaises(IntegrityError, lambda: new_ip_entry.save())

    def test_add_existing_ip_in_database_in_different_case(self):
        """
        Test that checking if correctly we cannot add an existing ip in our database,
        even if it has different case.
        """
        new_ip_entry = models.IPEntry(entry_value=self.ip.upper())
        self.assertRaises(IntegrityError, lambda: new_ip_entry.save())

    def test_add_existing_email_in_database(self):
        """
        Test that checking if correctly we cannot add an existing email in our database.
        """
        new_email_entry = models.EmailEntry(entry_value=self.email)
        self.assertRaises(IntegrityError, lambda: new_email_entry.save())

    def test_add_existing_email_in_database_in_different_case(self):
        """
        Test that checking if correctly we cannot add an existing email in our database,
        even if it has different case.
        """
        new_email_entry = models.EmailEntry(entry_value=self.email.upper())
        self.assertRaises(IntegrityError, lambda: new_email_entry.save())

    def test_add_existing_email_host_in_database(self):
        """
        Test that checking if correctly we cannot add an existing email host in our database.
        """
        new_email_host_entry = models.EmailHostEntry(entry_value=self.email_host)
        self.assertRaises(IntegrityError, lambda: new_email_host_entry.save())

    def test_add_existing_email_host_in_database_in_different_case(self):
        """
        Test that checking if correctly we cannot add an existing email host in our database,
        even if it has different case.
        """
        new_email_host_entry = models.EmailHostEntry(entry_value=self.email_host.upper())
        self.assertRaises(IntegrityError, lambda: new_email_host_entry.save())

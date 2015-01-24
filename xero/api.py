from __future__ import unicode_literals
from .manager import Manager


class Xero(object):
    """An ORM-like interface to the Xero API"""

    OBJECT_LIST = (
            'Accounts',
            'BankTransactions',
            'BankTransfers',
            'BrandingThemes',
            'ContactGroups',
            'Contacts',
            'CreditNotes',
            'Currencies',
            'Invoices',
            'Items',
            'Journals', 
            'ManualJournals',
            'Organisation',
            'Payments',
            'RepeatingInvoices',
            #'Reports',
            'TaxRates',
            'TrackingCategories',
            'Users',
        )

    def __init__(self, credentials):
        # Iterate through the list of objects we support, for
        # each of them create an attribute on our self that is
        # the lowercase name of the object and attach it to an
        # instance of a Manager object to operate on it
        for name in self.OBJECT_LIST:
            if "Reports" == name:
                setattr(self, name.lower(), ReportsManager(name, credentials))
                continue 
            setattr(self, name.lower(), Manager(name, credentials))

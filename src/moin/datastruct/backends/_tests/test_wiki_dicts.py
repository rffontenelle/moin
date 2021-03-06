# Copyright: 2003-2004 by Juergen Hermann <jh@web.de>
# Copyright: 2007 by MoinMoin:ThomasWaldmann
# Copyright: 2009 by MoinMoin:DmitrijsMilajevs
# Copyright: 2010 by MoinMoin:ReimarBauer
# License: GNU GPL v2 (or any later version), see LICENSE.txt for details.

"""
    MoinMoin - moin.datastruct.backends.wiki_dicts tests
"""


from moin.datastruct.backends._tests import DictsBackendTest
from moin.datastruct.backends import wiki_dicts
from moin.constants.keys import SOMEDICT
from moin._tests import become_trusted, update_item

import pytest


DATA = "This is a dict item."


class TestWikiDictsBackend(DictsBackendTest):

    # Suppose that default configuration for the dicts is used which
    # is WikiDicts backend.

    @pytest.fixture(autouse=True)
    def custom_setup(self):
        become_trusted()

        somedict = {u"First": u"first item",
                    u"text with spaces": u"second item",
                    u'Empty string': u'',
                    u"Last": u"last item"}
        update_item(u'SomeTestDict', {SOMEDICT: somedict}, DATA)

        somedict = {u"One": u"1",
                    u"Two": u"2"}
        update_item(u'SomeOtherTestDict', {SOMEDICT: somedict}, DATA)

    def test__retrieve_items(self):
        wikidict_obj = wiki_dicts.WikiDicts()
        result = wiki_dicts.WikiDicts._retrieve_items(wikidict_obj, u'SomeOtherTestDict')
        expected = {u'Two': u'2', u'One': u'1'}
        assert result == expected


coverage_modules = ['moin.datastruct.backends.wiki_dicts']

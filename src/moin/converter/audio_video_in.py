# Copyright: 2010 MoinMoin:ThomasWaldmann
# License: GNU GPL v2 (or any later version), see LICENSE.txt for details.

"""
MoinMoin - Audio/Video converter

Convert audio/video to <object> tag for the DOM Tree.

Note: currently this is quite same as image_in.
"""


from emeraldtree import ElementTree as ET

from moin.util.iri import Iri
from moin.util.tree import moin_page, xlink


class Converter(object):
    """
    Convert audio/video to the corresponding <object> in the DOM Tree
    """
    @classmethod
    def _factory(cls, input, output, **kw):
        return cls(input_type=input)

    def __init__(self, input_type):
        self.input_type = input_type

    def __call__(self, rev, contenttype=None, arguments=None):
        item_name = rev.item.name
        attrib = {
            moin_page.type_: unicode(self.input_type),
            xlink.href: Iri(scheme='wiki', authority='', path='/' + item_name,
                            query='do=get&rev={0}'.format(rev.revid)),
        }
        obj = moin_page.object_(attrib=attrib, children=[u'Your Browser does not support HTML5 audio/video element.', ])
        body = moin_page.body(children=(obj, ))
        return moin_page.page(children=(body, ))


from . import default_registry
from moin.util.mime import Type, type_moin_document
default_registry.register(Converter._factory, Type('video/mp4'), type_moin_document)
default_registry.register(Converter._factory, Type('video/ogg'), type_moin_document)
default_registry.register(Converter._factory, Type('video/webm'), type_moin_document)

default_registry.register(Converter._factory, Type('audio/mpeg'), type_moin_document)
default_registry.register(Converter._factory, Type('audio/ogg'), type_moin_document)
default_registry.register(Converter._factory, Type('audio/webm'), type_moin_document)
default_registry.register(Converter._factory, Type('audio/x-wav'), type_moin_document)

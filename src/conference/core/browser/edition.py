# -*- coding:utf-8 -*-
from five import grok
from conference.core.content.edition import IEdition


class View(grok.View):
    grok.context(IEdition)
    grok.require('zope2.View')

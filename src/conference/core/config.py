# -*- coding:utf-8 -*-
from five import grok

from collective.grok import gs
from collective.grok import i18n

from Products.CMFPlone.interfaces import INonInstallable

from conference.core import MessageFactory as _

PROJECTNAME = 'conference.core'
PROFILE_ID = 'conference.core:default'


# Default Profile
gs.profile(name=u'default',
           title=_(u'conference.core'),
           description=_(u'Installs conference.core'),
           directory='profiles/default')

# Uninstall Profile
gs.profile(name=u'uninstall',
           title=_(u'Uninstall conference.core'),
           description=_(u'Uninstall conference.core'),
           directory='profiles/uninstall')

i18n.registerTranslations(directory='locales')

class HiddenProfiles(grok.GlobalUtility):

    grok.implements(INonInstallable)
    grok.provides(INonInstallable)
    grok.name('conference.core')

    def getNonInstallableProfiles(self):
        profiles = ['conference.core:uninstall', ]
        return profiles

#!/usr/bin/python
# -*- coding: utf-8 -*-

from plugin import *
import json
import urllib2
import re

class lautstaerke(Plugin):
    
    @register("de-DE", ".*musik .*leiser.*")
    def musikleiser(self, speech, language):
        if language == 'de-DE':
            value = self.ask(u"Auf was soll die Lautstärke geändert werden?")
            os.system("amixer set Master \"{0}\" ".format(value))
            self.say(u"Ok, ich habe die Lautstärke für dich auf \"{0}\" gesetzt.".format(value))

    @register("de-DE", ".*musik .*lauter.*")
    def musikleiser(self, speech, language):
        if language == 'de-DE':
            value = self.ask(u"Auf was soll die Lautstärke geändert werden?")
            os.system("amixer set Master \"{0}\" ".format(value))
            self.say(u"Ok, ich habe die Lautstärke für dich auf \"{0}\" gesetzt.".format(value))


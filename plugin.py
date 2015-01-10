###
# Copyright (c) 2014, Dozo
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

class dozo(callbacks.Plugin):
    """Add the help for "@plugin help Dozo-plugin" here
    This should describe *how* to use this plugin."""
    def __init__(self, irc):
        callbacks.Plugin.__init__(self, irc)

		
    def dozo(self, irc, msg, args):
        """
        PLS
        """
        irc.reply('more like bozo amirite', prefixNick=False)

    dozo = wrap(dozo)

    def bentou(self, irc, msg, args):
        """
        lel
        """
        irc.reply('.kb ' + msg.nick, prefixNick=False)
    bentou = wrap(bentou)

    def ayy(self, irc, msg, args):
        """
        lmao
        """
        irc.reply('lmayyo', prefixNick=False)
    ayy = wrap(ayy)
	
    #def destinyfucker(self, irc, msg, args):
    #    """
    #    kek
    #    """
    #    irc.reply('wat', prefixNick=False)
    #destinyfucker = wrap(destinyfucker)

    def panic(self, irc, msg, args):
        """
        ohshit
        """
        irc.reply('4OH SHIT SON!!!!', prefixNick=False)
    panic = wrap(panic)

    def notpanic(self, irc, msg, args):
        """
        ohshit heh
        """
        irc.reply('3GREAT SUCCESS!!!!', prefixNick=False)
    notpanic = wrap(notpanic)

    #def blame(self, irc, msg, args):
    #    """
    #    ohshit heh
    #    """
    #    irc.reply('Episode 9 of Daito is at Dozo and is never getting finished! Give up!', prefixNick=False)
    #blame = wrap(blame)

    def bench(self, irc, msg, args):
        """
        ohshit heh
        """
        irc.reply('http://bentou.me/Software/prime95/p95v279.win64.zip', prefixNick=False)
    bench = wrap(bench)

    def rcombs(self, irc, msg, args):
        """
        kek
        """
        irc.reply('rcombs more like ERR:CANNOT FIND INSULT', prefixNick=False)
    rcombs = wrap(rcombs)

    def nm(self, irc, msg, args):
        """
        kek
        """
        irc.reply('http://niceme.me/', prefixNick=False)
    nm = wrap(nm)

    def dium(self, irc, msg, args):
        """
        kek
        """
        irc.reply('dium more like dum amirite', prefixNick=False)
    dium = wrap(dium)

    #def nbk(self, irc, msg, args):
    #    """
    #    kek
    #    """
    #    irc.reply('.k nbk', prefixNick=False)
    #nbk = wrap(nbk)

    def isdozodrunk(self, irc, msg, args):
        """
        kek
        """
        irc.reply('Nope. He just wishes he was.', prefixNick=False)
    isdozodrunk = wrap(isdozodrunk)

    def vendorpony(self, irc, msg, args):
        """
        kek
        """
        irc.reply('chill bro.', prefixNick=False)
    vendorpony = wrap(vendorpony)

    def sozo(self, irc, msg, args):
        """
        kek
        """
        irc.reply('Dozo pls. Are you drunk?', prefixNick=False)
    sozo = wrap(sozo)

    def eien(self, irc, msg, args):
        """
        kek
        """
        irc.reply('Eien stinx', prefixNick=False)
    eien = wrap(eien)

Class = dozo


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:

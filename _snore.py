# Puts DNS to sleep

try:
    import pkg_resources
    pkg_resources.require("dragonfly >= 0.6.5beta1.dev-r99")
except ImportError:
    pass

import natlink
from dragonfly import (Grammar, CompoundRule, Config, Section, Item)

#---------------------------------------------------------------------------

class SnoreRule(CompoundRule):
    spec = "snore"
    def _process_recognition(self, node, extras):
        natlink.setMicState("sleeping")

#---------------------------------------------------------------------------

grammar = Grammar("Snore")
grammar.add_rule(SnoreRule())
grammar.load()
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

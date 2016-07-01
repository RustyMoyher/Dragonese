# Simple commands that should always be working

import time
mod_init_time = time.time()
print 'loading _simple module'
def timing_stats(msg):
    print '%s:'%msg, (time.time() - mod_init_time)

#import pkg_resources
import natlink
import natlinkmain
from dragonfly import (Grammar, MappingRule, Config, Section, Item, Key)

#---------------------------------------------------------------------------

release = Key("shift:up, ctrl:up")

def T(s, pause=0.0002, **kws):
	return Text(s, pause=pause, **kws)

def K(*args, **kws):
	return Key(*args, **kws)

class CharRule(MappingRule):
	mapping = {
		"slap": Key("enter")
		, "chook": Key("backspace")
        , "quit": Key("escape")
        , "save": release + Key("c-s")
        , "paste": release + Key("c-v")
        , "copy": release + Key("c-c")
        , "cut": release + Key("c-x")
        , "select all": release + Key("c-a")
		, "(undo | scratch)": release + Key("c-z")
		, "redo": release + Key("c-y")
	}

#---------------------------------------------------------------------------

grammar = Grammar("Simple")
grammar.add_rule(CharRule())
grammar.load()
def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
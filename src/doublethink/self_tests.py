# -*- coding: utf-8 -*-
# Copyright: (C) 2020 Lovac42
# Support: https://github.com/lovac42/Doublethink
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html


# This only tests for correct wrapping.
# It does not account for name changes.

import unicodedata
from anki.hooks import addHook


def onBridgeCmd():
    testWrap("欄廊朗虜")

def importNotes():
    testWrap("類猪神")

def _onSearchActivated():
    testWrap("祥福諸")

def testWrap(non_norm):
    processed = unicodedata.normalize("NFC", non_norm)
    assert non_norm == processed, "Addon Doublethink failed to work"

def runTests():
    for func in (onBridgeCmd,importNotes,_onSearchActivated):
        func()
    # print("Addon Doublethink loaded successfully")

addHook("profileLoaded", runTests)


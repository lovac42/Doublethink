# -*- coding: utf-8 -*-
# Copyright: (C) 2020 Lovac42
# Support: https://github.com/lovac42/Doublethink
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html


import unicodedata
from anki.hooks import addHook



def onBridgeCmd():
    "Called by card editor"
    from aqt.editor import Editor
    testMethodName(Editor, "onBridgeCmd")
    testWrap("欄廊朗虜神")


def importNotes():
    "Called by note importer"
    from anki.importing.csvfile import TextImporter
    testMethodName(TextImporter, "importNotes")
    testWrap("朗虜類猪神")


def _onSearchActivated():
    "Called by browser searches"
    from aqt.browser import Browser
    testMethodName(Browser, "_onSearchActivated")
    testWrap("欄廊祥福諸")




def testWrap(non_norm):
    "test if wrap was successful"
    processed = unicodedata.normalize("NFC", non_norm)
    assert non_norm == processed, "Addon Doublethink failed to work"


def testMethodName(className, methodName):
    "test if method name is still the same between different anki versions"
    assert hasattr(className, methodName) and callable(getattr(className, methodName)), f"The method {methodName} required by the addon Doublethink is no longer available."


def runTests():
    for func in (onBridgeCmd, importNotes, _onSearchActivated):
        func()
    # print("Addon Doublethink loaded successfully")

addHook("profileLoaded", runTests)


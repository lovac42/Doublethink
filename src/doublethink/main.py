# -*- coding: utf-8 -*-
# Copyright: (C) 2019-2020 Lovac42
# Support: https://github.com/lovac42/Doublethink
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html


import sys
import unicodedata


normalized=unicodedata.normalize

def nonnormalized_passthrough_filter(form, txt):
    if form == "NFC":
        for i in range (1,5): #filter calling function
            try:
                if sys._getframe(i).f_code.co_name in (
                    "onBridgeCmd", "importNotes", "_onSearchActivated"
                ):
                    return txt
            except ValueError:
                break
    return normalized(form, txt)

unicodedata.normalize=nonnormalized_passthrough_filter

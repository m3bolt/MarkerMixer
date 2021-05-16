# Copyright (c) 2017 Ruben Dulek
# The PostProcessingPlugin is released under the terms of the AGPLv3 or higher.

import re #To perform the search and replace.

from ..Script import Script


class AutoReplace(Script):
    """Performs a search-and-replace on all g-code.

    Due to technical limitations, the search can't cross the border between
    layers.
    """

    def getSettingDataString(self):
        return """{
            "name": "AutoReplace",
            "key": "AutoReplace",
            "metadata": {},
            "version": 2,
            "settings":
            {
                
            }
        }"""

    def execute(self, dataT0):
        search_stringT0 = "T0"
        if not self.getSettingValueByKey("is_regex"):
            search_stringT0 = re.escape(search_stringT0) #Need to search for the actual string, not as a regex.
        search_regexT0 = re.compile(search_stringT0)

        replace_stringT0 = "x"

        for layer_number, layer in enumerate(dataT0):
            dataT0[layer_number] = re.sub(search_regexT0, replace_stringT0, layer) #Replace all.

        return dataT0
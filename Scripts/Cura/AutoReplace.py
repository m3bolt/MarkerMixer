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

    def execute(self, data):
        search_string = "T0"
        if not self.getSettingValueByKey("is_regex"):
            search_string = re.escape(search_string) #Need to search for the actual string, not as a regex.
        search_regex = re.compile(search_string)

        replace_string = "x"

        for layer_number, layer in enumerate(data):
            data[layer_number] = re.sub(search_regex, replace_string, layer) #Replace all.

        return data
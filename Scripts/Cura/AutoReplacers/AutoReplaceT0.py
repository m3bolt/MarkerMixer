# Copyright (c) 2017 Ruben Dulek
# The PostProcessingPlugin is released under the terms of the AGPLv3 or higher.

import re #To perform the search and replace.

from ..Script import Script


class AutoReplaceT0(Script):
    """Performs an automatic search-and-delete on all g-code.

    """

    def getSettingDataString(self):
        return """{
            "name": "AutoReplaceT0",
            "key": "AutoReplaceT0",
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

        replace_stringT0 = ""

        for layer_number, layer in enumerate(dataT0):
            dataT0[layer_number] = re.sub(search_regexT0, replace_stringT0, layer) #Replace all.

		
        return dataT0
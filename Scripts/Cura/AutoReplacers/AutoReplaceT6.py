# Copyright (c) 2017 Ruben Dulek
# The PostProcessingPlugin is released under the terms of the AGPLv3 or higher.

import re #To perform the search and replace.

from ..Script import Script


class AutoReplaceT6(Script):
    """Performs an automatic search-and-delete on all g-code.

    """

    def getSettingDataString(self):
        return """{
            "name": "AutoReplaceT6",
            "key": "AutoReplaceT6",
            "metadata": {},
            "version": 2,
            "settings":
            {
                
            }
        }"""

    def execute(self, dataT6):
        search_stringT6 = "T6"
		
        if not self.getSettingValueByKey("is_regex"):
            search_stringT6 = re.escape(search_stringT6) #Need to search for the actual string, not as a regex.
        search_regexT6 = re.compile(search_stringT6)

        replace_stringT6 = ""

        for layer_number, layer in enumerate(dataT6):
            dataT6[layer_number] = re.sub(search_regexT6, replace_stringT6, layer) #Replace all.

		
        return dataT6
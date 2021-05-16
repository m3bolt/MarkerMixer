# Copyright (c) 2017 Ruben Dulek
# The PostProcessingPlugin is released under the terms of the AGPLv3 or higher.

import re #To perform the search and replace.

from ..Script import Script


class AutoReplaceT2(Script):
    """Performs an automatic search-and-delete on all g-code.

    """

    def getSettingDataString(self):
        return """{
            "name": "AutoReplaceT2",
            "key": "AutoReplaceT2",
            "metadata": {},
            "version": 2,
            "settings":
            {
                
            }
        }"""

    def execute(self, dataT2):
        search_stringT2 = "T2"
		
        if not self.getSettingValueByKey("is_regex"):
            search_stringT2 = re.escape(search_stringT2) #Need to search for the actual string, not as a regex.
        search_regexT2 = re.compile(search_stringT2)

        replace_stringT2 = ""

        for layer_number, layer in enumerate(dataT2):
            dataT2[layer_number] = re.sub(search_regexT2, replace_stringT2, layer) #Replace all.

		
        return dataT2
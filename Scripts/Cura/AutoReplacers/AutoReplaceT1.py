# Copyright (c) 2017 Ruben Dulek
# The PostProcessingPlugin is released under the terms of the AGPLv3 or higher.

import re #To perform the search and replace.

from ..Script import Script


class AutoReplaceT1(Script):
    """Performs an automatic search-and-delete on all g-code.

    """

    def getSettingDataString(self):
        return """{
            "name": "AutoReplaceT1",
            "key": "AutoReplaceT1",
            "metadata": {},
            "version": 2,
            "settings":
            {
                
            }
        }"""

    def execute(self, dataT1):
        search_stringT1 = "T1"
		
        if not self.getSettingValueByKey("is_regex"):
            search_stringT1 = re.escape(search_stringT1) #Need to search for the actual string, not as a regex.
        search_regexT1 = re.compile(search_stringT1)

        replace_stringT1 = ""

        for layer_number, layer in enumerate(dataT1):
            dataT1[layer_number] = re.sub(search_regexT1, replace_stringT1, layer) #Replace all.

		
        return dataT1
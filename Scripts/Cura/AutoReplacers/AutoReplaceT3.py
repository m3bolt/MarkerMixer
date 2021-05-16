# Copyright (c) 2017 Ruben Dulek
# The PostProcessingPlugin is released under the terms of the AGPLv3 or higher.

import re #To perform the search and replace.

from ..Script import Script


class AutoReplaceT3(Script):
    """Performs an automatic search-and-delete on all g-code.

    """

    def getSettingDataString(self):
        return """{
            "name": "AutoReplaceT3",
            "key": "AutoReplaceT3",
            "metadata": {},
            "version": 2,
            "settings":
            {
                
            }
        }"""

    def execute(self, dataT3):
        search_stringT3 = "T3"
		
        if not self.getSettingValueByKey("is_regex"):
            search_stringT3 = re.escape(search_stringT3) #Need to search for the actual string, not as a regex.
        search_regexT3 = re.compile(search_stringT3)

        replace_stringT3 = ""

        for layer_number, layer in enumerate(dataT3):
            dataT3[layer_number] = re.sub(search_regexT3, replace_stringT3, layer) #Replace all.

		
        return dataT3
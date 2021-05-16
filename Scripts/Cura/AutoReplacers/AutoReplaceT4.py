# Copyright (c) 2017 Ruben Dulek
# The PostProcessingPlugin is released under the terms of the AGPLv3 or higher.

import re #To perform the search and replace.

from ..Script import Script


class AutoReplaceT4(Script):
    """Performs an automatic search-and-delete on all g-code.

    """

    def getSettingDataString(self):
        return """{
            "name": "AutoReplaceT4",
            "key": "AutoReplaceT4",
            "metadata": {},
            "version": 2,
            "settings":
            {
                
            }
        }"""

    def execute(self, dataT4):
        search_stringT4 = "T4"
		
        if not self.getSettingValueByKey("is_regex"):
            search_stringT4 = re.escape(search_stringT4) #Need to search for the actual string, not as a regex.
        search_regexT4 = re.compile(search_stringT4)

        replace_stringT4 = ""

        for layer_number, layer in enumerate(dataT4):
            dataT4[layer_number] = re.sub(search_regexT4, replace_stringT4, layer) #Replace all.

		
        return dataT4
# Copyright (c) 2017 Ruben Dulek
# The PostProcessingPlugin is released under the terms of the AGPLv3 or higher.

import re #To perform the search and replace.

from ..Script import Script


class AutoReplaceT7(Script):
    """Performs an automatic search-and-delete on all g-code.

    """

    def getSettingDataString(self):
        return """{
            "name": "AutoReplaceT7",
            "key": "AutoReplaceT7",
            "metadata": {},
            "version": 2,
            "settings":
            {
                
            }
        }"""

    def execute(self, dataT7):
        search_stringT7 = "T7"
		
        if not self.getSettingValueByKey("is_regex"):
            search_stringT7 = re.escape(search_stringT7) #Need to search for the actual string, not as a regex.
        search_regexT7 = re.compile(search_stringT7)

        replace_stringT7 = ""

        for layer_number, layer in enumerate(dataT7):
            dataT7[layer_number] = re.sub(search_regexT7, replace_stringT7, layer) #Replace all.

		
        return dataT7
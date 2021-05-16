# Copyright (c) 2017 Ruben Dulek
# The PostProcessingPlugin is released under the terms of the AGPLv3 or higher.

import re #To perform the search and replace.

from ..Script import Script


class AutoReplaceT5(Script):
    """Performs an automatic search-and-delete on all g-code.

    """

    def getSettingDataString(self):
        return """{
            "name": "AutoReplaceT5",
            "key": "AutoReplaceT5",
            "metadata": {},
            "version": 2,
            "settings":
            {
                
            }
        }"""

    def execute(self, dataT5):
        search_stringT5 = "T5"
		
        if not self.getSettingValueByKey("is_regex"):
            search_stringT5 = re.escape(search_stringT5) #Need to search for the actual string, not as a regex.
        search_regexT5 = re.compile(search_stringT5)

        replace_stringT5 = ""

        for layer_number, layer in enumerate(dataT5):
            dataT5[layer_number] = re.sub(search_regexT5, replace_stringT5, layer) #Replace all.

		
        return dataT5
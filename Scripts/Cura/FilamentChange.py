
from typing import List
from ..Script import Script

class FilamentChange(Script):

    _layer_keyword = ";LAYER:"

    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name":"The Magic Marker Mixer",
            "key": "FilamentChange",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "layer_number_S1E":
                {
                    "label": "Servo One Engage Layer",
                    "description": "Layer height where servo one turns on. Specify multiple color changes with a comma.",
                    "unit": "",
                    "type": "str",
                    "default_value": "1"
                },
                "layer_number_S1R":
                {
                    "label": "Servo One Retract Layer",
                    "description": "Layer height where servo one turns off. Specify multiple color changes with a comma.",
                    "unit": "",
                    "type": "str",
                    "default_value": "2"
                }

                
                
            }
        }"""

    def execute(self, data: List[str]):
        """Inserts the filament change g-code at specific layer numbers.

        :param data: A list of layers of g-code.
        :return: A similar list, with filament change commands inserted.
        """
        layer_nums_S1E = self.getSettingValueByKey("layer_number_S1E")
        layer_nums_S1R = self.getSettingValueByKey("layer_number_S1R") 
        servo1_engage = "P1_24 S255"
        servo1_retract = "P1_24 S0"
        servo1_engage = servo1_engage + " ; engage servo one \n"
        servo1_retract = servo1_retract + " ; retract servo one \n"

        layer_targets_S1E = layer_nums_S1E.split(",")
        if len(layer_targets_S1E) > 0:
            for layer_num_S1E in layer_targets_S1E:
                try:
                    layer_num_S1E = int(layer_num_S1E.strip()) + 1 #Needs +1 because the 1st layer is reserved for start g-code.
                except ValueError: #Layer number is not an integer.
                    continue
                if 0 < layer_num_S1E < len(data):
                    data[layer_num_S1E] = servo1_engage + data[layer_num_S1E]

        

        layer_targets_S1R = layer_nums_S1R.split(",")
        if len(layer_targets_S1R) > 0:
            for layer_num_S1R in layer_targets_S1R:
                try:
                    layer_num_S1R = int(layer_num_S1R.strip()) + 1 #Needs +1 because the 1st layer is reserved for start g-code.
                except ValueError: #Layer number is not an integer.
                    continue
                if 0 < layer_num_S1R < len(data):
                    data[layer_num_S1R] = servo1_retract + data[layer_num_S1R]

        return data
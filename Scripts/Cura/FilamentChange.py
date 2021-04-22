 Magic Marker Mixer
 #Github: https://github.com/m3bolt/MarkerMixer
 #Designers:
 #Code: https://github.com/kackle1998 
 #Mech Design: https://github.com/m3bolt/ , https://github.com/kackle1998 
 #WIP
 #Initial Arduino+Cura proof of concept for 1in-1out multicolor 3D Printing

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
                },
                "layer_number_S2E":
                {
                    "label": "Servo Two Engage Layer",
                    "description": "Layer height where servo two turns on. Specify multiple color changes with a comma.",
                    "unit": "",
                    "type": "str",
                    "default_value": "1"
                },
                "layer_number_S2R":
                {
                    "label": "Servo Two Retract Layer",
                    "description": "Layer height where servo two turns off. Specify multiple color changes with a comma.",
                    "unit": "",
                    "type": "str",
                    "default_value": "2"
                },
                "layer_number_S3E":
                {
                    "label": "Servo Three Engage Layer",
                    "description": "Layer height where servo three turns on. Specify multiple color changes with a comma.",
                    "unit": "",
                    "type": "str",
                    "default_value": "1"
                },
                "layer_number_S3R":
                {
                    "label": "Servo Three Retract Layer",
                    "description": "Layer height where servo three turns off. Specify multiple color changes with a comma.",
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
        #Servo1
        layer_nums_S1E = self.getSettingValueByKey("layer_number_S1E")
        layer_nums_S1R = self.getSettingValueByKey("layer_number_S1R") 
        servo1_engage = "MarkerOneEngage"
        servo1_retract = "MarkerOneRetract"
        servo1_engage = servo1_engage + " ; engage servo one \n"
        servo1_retract = servo1_retract + " ; retract servo one \n"
        #Servo2
        layer_nums_S2E = self.getSettingValueByKey("layer_number_S2E")
        layer_nums_S2R = self.getSettingValueByKey("layer_number_S2R") 
        servo2_engage = "MarkerTwoEngage"
        servo2_retract = "MarkerTwoRetract"
        servo2_engage = servo2_engage + " ; engage servo two \n"
        servo2_retract = servo2_retract + " ; retract servo two \n"
         #Servo3
        layer_nums_S3E = self.getSettingValueByKey("layer_number_S3E")
        layer_nums_S3R = self.getSettingValueByKey("layer_number_S3R") 
        servo3_engage = "MarkerThreeEngage"
        servo3_retract = "MarkerThreeRetract"
        servo3_engage = servo3_engage + " ; engage servo three \n"
        servo3_retract = servo3_retract + " ; retract servo three \n"

        #Servo1
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

        #Servo2
        layer_targets_S2E = layer_nums_S2E.split(",")
        if len(layer_targets_S2E) > 0:
            for layer_num_S2E in layer_targets_S2E:
                try:
                    layer_num_S2E = int(layer_num_S2E.strip()) + 1 #Needs +1 because the 1st layer is reserved for start g-code.
                except ValueError: #Layer number is not an integer.
                    continue
                if 0 < layer_num_S2E < len(data):
                    data[layer_num_S2E] = servo2_engage + data[layer_num_S2E]

        layer_targets_S2R = layer_nums_S2R.split(",")
        if len(layer_targets_S2R) > 0:
            for layer_num_S2R in layer_targets_S2R:
                try:
                    layer_num_S2R = int(layer_num_S2R.strip()) + 1 #Needs +1 because the 1st layer is reserved for start g-code.
                except ValueError: #Layer number is not an integer.
                    continue
                if 0 < layer_num_S2R < len(data):
                    data[layer_num_S2R] = servo2_retract + data[layer_num_S2R]
        
        #Servo3
        layer_targets_S3E = layer_nums_S3E.split(",")
        if len(layer_targets_S3E) > 0:
            for layer_num_S3E in layer_targets_S3E:
                try:
                    layer_num_S3E = int(layer_num_S3E.strip()) + 1 #Needs +1 because the 1st layer is reserved for start g-code.
                except ValueError: #Layer number is not an integer.
                    continue
                if 0 < layer_num_S3E < len(data):
                    data[layer_num_S3E] = servo3_engage + data[layer_num_S3E]

        layer_targets_S3R = layer_nums_S3R.split(",")
        if len(layer_targets_S3R) > 0:
            for layer_num_S3R in layer_targets_S3R:
                try:
                    layer_num_S3R = int(layer_num_S3R.strip()) + 1 #Needs +1 because the 1st layer is reserved for start g-code.
                except ValueError: #Layer number is not an integer.
                    continue
                if 0 < layer_num_S3R < len(data):
                    data[layer_num_S3R] = servo3_retract + data[layer_num_S3R]
        
        return data
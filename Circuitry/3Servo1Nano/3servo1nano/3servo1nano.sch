EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Conn_01x03_Female Servo1
U 1 1 60989BD0
P 4850 2000
F 0 "Servo1" H 4878 2026 50  0000 L CNN
F 1 "Conn_01x03_Female" H 4878 1935 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 4850 2000 50  0001 C CNN
F 3 "~" H 4850 2000 50  0001 C CNN
	1    4850 2000
	0    -1   -1   0   
$EndComp
$Comp
L MCU_Module:Arduino_Nano_v3.x A1
U 1 1 6098434D
P 5250 3450
F 0 "A1" H 5250 2361 50  0000 C CNN
F 1 "Arduino_Nano_v3.x" H 5250 2270 50  0000 C CNN
F 2 "Module:Arduino_Nano" H 5250 3450 50  0001 C CIN
F 3 "http://www.mouser.com/pdfdocs/Gravitech_Arduino_Nano3_0.pdf" H 5250 3450 50  0001 C CNN
	1    5250 3450
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x03_Female Servo2
U 1 1 6098A39F
P 5300 2000
F 0 "Servo2" H 5328 2026 50  0000 L CNN
F 1 "Conn_01x03_Female" H 5328 1935 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 5300 2000 50  0001 C CNN
F 3 "~" H 5300 2000 50  0001 C CNN
	1    5300 2000
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Conn_01x03_Female Servo3
U 1 1 60994250
P 5700 2000
F 0 "Servo3" H 5728 2026 50  0000 L CNN
F 1 "Conn_01x03_Female" V 5728 1935 50  0001 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 5700 2000 50  0001 C CNN
F 3 "~" H 5700 2000 50  0001 C CNN
	1    5700 2000
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5450 2450 5700 2450
Wire Wire Line
	5700 2450 5700 2200
Wire Wire Line
	5450 2450 5350 2450
Wire Wire Line
	5300 2450 5300 2200
Connection ~ 5450 2450
Connection ~ 5350 2450
Wire Wire Line
	5350 2450 5300 2450
Wire Wire Line
	4850 2450 4850 2200
Connection ~ 5150 2450
Wire Wire Line
	5150 2450 4850 2450
Connection ~ 5300 2450
Wire Wire Line
	5300 2450 5150 2450
Wire Wire Line
	5250 4450 4600 4450
Wire Wire Line
	4600 4450 4600 2200
Wire Wire Line
	4600 2200 4750 2200
Wire Wire Line
	5250 4450 5350 4450
Wire Wire Line
	5600 4450 5600 2200
Connection ~ 5250 4450
Connection ~ 5350 4450
Wire Wire Line
	5350 4450 5600 4450
Wire Wire Line
	5250 4450 5250 2200
Wire Wire Line
	5250 2200 5200 2200
$EndSCHEMATC

import unittest
from main import *

class NamesTestCase(unittest.TestCase):
    def test_CasesInSameLine(self):
        current_station     = 'شبرا الخيمة'
        destination_station = 'العباسية'
        station_info = get_StationInfo(current_station,destination_station)
        current_line     = lines[station_info['CurrentLine']]
        destination_line = lines[station_info['SecLine']]
        switcher = GetSwitcherStation(current_line,destination_line,current_station)
        StationInfo = get_StationInfo(current_station,switcher)
        Station2Info = get_StationInfo(switcher,destination_station)
        StationCounter = (StationInfo['StationCount'] + Station2Info['StationCount']) - 1 # 1 represnt of duplicated station in current line and destination line
        price = CalcPrice(StationCounter,current_station,destination_station)
        self.assertEqual(switcher,'العتبة')
        self.assertEqual(station_info['CurrentLine'],'shobra')
        self.assertEqual(station_info['SecLine'],'airport')
        self.assertEqual(StationInfo['Direction'],'المنيب')
        self.assertEqual(Station2Info['Direction'],'نادي الشمس')
        self.assertEqual(StationCounter,13)
        self.assertEqual(price,7)
            

    
    
    def test_DirectionsInSameLine(self):
        current_station     = 'شبرا الخيمة'
        destination_station = 'الجيزة'
        Station2Info = get_StationInfo(current_station,destination_station)
        price = CalcPrice(Station2Info['StationCount'],current_station,destination_station)
        self.assertEqual(Station2Info['Direction'],'المنيب')
        self.assertEqual(Station2Info['StationCount'],17)
        self.assertEqual(price,7)
        
    def test_Random001(self):
        current_station     = 'الجيزة'
        destination_station = 'الشهداء'
        Station2Info = get_StationInfo(current_station,destination_station)
        price = CalcPrice(Station2Info['StationCount'],current_station,destination_station)
        self.assertEqual(Station2Info['Direction'],'شبرا الخيمة')
        self.assertEqual(Station2Info['StationCount'],10)
        self.assertEqual(price,5)

    def test_Random002(self):
        current_station     = 'الشهداء'
        destination_station = 'الجيزة'
        Station2Info = get_StationInfo(current_station,destination_station)
        price = CalcPrice(Station2Info['StationCount'],current_station,destination_station)
        self.assertEqual(Station2Info['Direction'],'المنيب')
        self.assertEqual(Station2Info['StationCount'],10)
        self.assertEqual(price,5)
        
    def test_Random003(self):
        current_station     = 'الشهداء'
        destination_station = 'كلية الزراعة'
        Station2Info = get_StationInfo(current_station,destination_station)
        price = CalcPrice(Station2Info['StationCount'],current_station,destination_station)
        
        self.assertEqual(Station2Info['Direction'],'شبرا الخيمة')
        self.assertEqual(Station2Info['StationCount'],7)
        self.assertEqual(price,3)
    
    def test_Random004(self):
        current_station     = 'الشهداء'
        destination_station = 'جامعة حلوان'
        Station2Info = get_StationInfo(current_station,destination_station)
        price = CalcPrice(Station2Info['StationCount'],current_station,destination_station)
        self.assertEqual(Station2Info['Direction'],'محطة حلوان')
        self.assertEqual(Station2Info['StationCount'],20)
        self.assertEqual(price,7)
        
    def test_CasesInSameLine(self):
        current_station     = 'منشية الصدر'
        destination_station = 'الجيزة'
        station_info = get_StationInfo(current_station,destination_station)
        current_line     = lines[station_info['CurrentLine']]
        destination_line = lines[station_info['SecLine']]
        switcher = GetSwitcherStation(current_line,destination_line,current_station)
        StationInfo = get_StationInfo(current_station,switcher)
        Station2Info = get_StationInfo(switcher,destination_station)
        StationCounter = (StationInfo['StationCount'] + Station2Info['StationCount']) - 1 # 1 represnt of duplicated station in current line and destination line
        price = CalcPrice(StationCounter,current_station,destination_station)
        self.assertEqual(switcher,'الشهداء')
        self.assertEqual(station_info['CurrentLine'],'marg')
        self.assertEqual(station_info['SecLine'],'shobra')
        self.assertEqual(StationInfo['Direction'],'محطة حلوان')
        self.assertEqual(Station2Info['Direction'],'المنيب')
        self.assertEqual(StationCounter,13)
        self.assertEqual(price,5)
        
if __name__ == '__main__':
    unittest.main()
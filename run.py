from main import *
current_station     = str(input())
destination_station =  str(input())    
station_info = get_StationInfo(current_station,destination_station)
if (station_info['same_line'] == True):
    # if station_info == True then the current and destination station in the same line
    ticket_price = CalcPrice(station_info['StationCount'],current_station,destination_station)
    # get the ticket price
    StationsNumbersIs = station_info['StationCount'] # get number of stations
    DirectionIs = station_info['Direction'] # get the dirction
    print('ticket price is : ' + str(ticket_price) + ' LE')
    print('ride the subway destined to ' + DirectionIs)
    print(str(StationsNumbersIs) + ' Stops way from current station ')
    print('will be you arrive ' + destination_station)
else:
    # The current station and destionation station is not in same line
    current_line     = lines[station_info['CurrentLine']] # get name of current line
    destination_line = lines[station_info['SecLine']] # get name of destionation line

    switcher = GetSwitcherStation(current_line,destination_line,current_station)
    # get swticher station
    
    StationInfo = get_StationInfo(current_station,switcher) # will
    print('-----Make This In First Line------')
    Station2Info = get_StationInfo(switcher,destination_station)
    StationCounter = (StationInfo['StationCount'] + Station2Info['StationCount']) - 1
    # 1 represnt of duplicated swticher station in current line and destination line
    price = CalcPrice(StationCounter,current_station,destination_station)

    print('ticket price is : ' + str(price) + ' LE')
    print('Go to direction of : ' + StationInfo['Direction'])
    print(':::::::- and get down in ' + switcher + ' station' )
    print('From- '+ switcher + ' ride the subway destined to ' + Station2Info['Direction'])
    print(str(Station2Info['StationCount']) + ' Stops way from switcher station')
    print('will be you arrive ' + destination_station)
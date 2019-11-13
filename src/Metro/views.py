from django.shortcuts import render
from .forms import MainForm
import os
from django.conf import settings
# comment
def index(request):
    current_station = None
    drop_station = None
    TransferStation = None
    counts = None
    TicketPrice = 'Default'
    FirstDir = None
    SecDir = None
    StationOfChanger = None
    form = MainForm() 
    if request.method == 'POST':
        form = MainForm(request.POST)        
        if form.is_valid():
            current_station = form.cleaned_data['CurrentStation']
            drop_station = form.cleaned_data['DropStation']
            def GetTransferStation(arr1,arr2):
                countArr1 = len(arr1)
                countArr2 = len(arr2) # 5
                for i in range(countArr2):
                    for x in range(countArr1):
                        if arr2[i] in arr1[x]:
                            return arr1[x]
                                  				
            def selectLiveAndDrop(current_location,drop_location):
                marg = []
                shobra = []
                embaba = []
                module_dir = os.path.dirname(__file__)
                margFile = os.path.join(module_dir, 'marg.txt')

                with open(margFile,encoding='utf-8') as margFile:
                    for i in margFile:
                        item = i.strip()
                        marg.append(item)
                shobraFile = os.path.join(module_dir, 'shobra.txt')
                with open(shobraFile,encoding='utf-8') as shobraFile:
                    for i in shobraFile:
                        item = i.strip()
                        shobra.append(item)
                embabaFile = os.path.join(module_dir, 'embaba.txt')
                with open(embabaFile,encoding='utf-8') as embabaFile:
                    for i in embabaFile:
                        item = i.strip()
                        embaba.append(item)

                line = [marg,shobra,embaba]
                
                if current_location in line[0] and drop_location in line[0]:
                    if line[0].index(current_location) < line[0].index(drop_location):
                        FirstDir = line[0][-1]
                    else:
                        FirstDir = line[0][0]

                    if line[0].index(drop_location) > line[0].index(current_location):
                        StationCounter = line[0].index(drop_location) - line[0].index(current_location)+1
                    else:
                        StationCounter =line[0].index(current_location) - line[0].index(drop_location)+1

                elif current_location in line[1] and drop_location in line[1]:
                    if line[1].index(current_location) < line[1].index(drop_location):
                        FirstDir = line[1][-1]
                    else:
                        FirstDir = line[1][0]
                    if line[1].index(drop_location) > line[1].index(current_location):
                        StationCounter = line[1].index(drop_location) - line[1].index(current_location)+1
                    else:
                        StationCounter = line[1].index(current_location) - line[1].index(drop_location)+1
                elif current_location in line[2] and drop_location in line[2]:
                    if line[2].index(current_location) < line[2].index(drop_location):
                        FirstDir = line[2][-1]
                    else:
                        FirstDir = line[2][0]
                    if line[2].index(drop_location) > line[2].index(current_location):
                        StationCounter = line[2].index(drop_location) - line[2].index(current_location)+1
                    else:
                        StationCounter = line[2].index(current_location) - line[2].index(drop_location)+1

                    
                else:
                    for i,x,e in zip(*line):
                        if drop_location in i:
                            Drop_Station_Line = line[0]

                        elif drop_location in x:
                            Drop_Station_Line = line[1]

                        elif drop_location in e:
                            Drop_Station_Line = line[2]

                        if current_location in i:
                            Location_Station_line = line[0]
                        elif current_location in x:
                            Location_Station_line = line[1]
                        elif current_location in e:
                            Location_Station_line = line[2]
                        
                    StationOfChanger = GetTransferStation(Location_Station_line,Drop_Station_Line)
                    if Location_Station_line.index(current_location) > Location_Station_line.index(StationOfChanger):
                        FirstDir = Location_Station_line[0]
                    else:
                        lenghtList = len(Location_Station_line)
                        FirstDir = Location_Station_line[lenghtList-1]
                        
                    
                    if Drop_Station_Line.index(drop_location) < Drop_Station_Line.index(StationOfChanger):
                        SecDir = Drop_Station_Line[0]
                    else:
                        lenghtList = len(Drop_Station_Line)
                        SecDir = Drop_Station_Line[lenghtList-1]

                    StationChangerIndexDropLine = Drop_Station_Line.index(StationOfChanger)+1
                    StationChangerIndexCurrentLine = Location_Station_line.index(StationOfChanger)+1
                    DropStationIndex = Drop_Station_Line.index(drop_location)+1
                    CurrentStationIndex = Location_Station_line.index(current_location)+1
                    
                    if CurrentStationIndex > StationChangerIndexCurrentLine and DropStationIndex > StationChangerIndexDropLine:
                        StationCounterInCurrentLine = CurrentStationIndex - StationChangerIndexCurrentLine
                        StationCounterInDropLine = DropStationIndex - StationChangerIndexDropLine +1
                        StationCounter = StationCounterInCurrentLine + StationCounterInDropLine
                        
                    elif CurrentStationIndex < StationChangerIndexCurrentLine and DropStationIndex > StationChangerIndexDropLine:
                        StationCounterInCurrentLine = StationChangerIndexCurrentLine - CurrentStationIndex +1
                        StationCounterInDropLine = DropStationIndex - StationChangerIndexDropLine
                        StationCounter = StationCounterInDropLine + StationCounterInCurrentLine
                    elif CurrentStationIndex > StationChangerIndexCurrentLine and DropStationIndex < StationChangerIndexCurrentLine:
                        StationCounterInCurrentLine = CurrentStationIndex - StationChangerIndexCurrentLine +1
                        StationCounterInDropLine = StationChangerIndexDropLine - DropStationIndex
                        StationCounter = StationCounterInCurrentLine + StationCounterInDropLine

                    elif CurrentStationIndex < StationChangerIndexCurrentLine and DropStationIndex < StationChangerIndexDropLine:
                        StationCounterInCurrentLine = StationChangerIndexCurrentLine - CurrentStationIndex +1
                        StationCounterInDropLine = StationChangerIndexDropLine - DropStationIndex
                        StationCounter = StationCounterInDropLine + StationCounterInCurrentLine
                    elif CurrentStationIndex < StationChangerIndexCurrentLine and DropStationIndex > StationChangerIndexDropLine:
                        StationCounterInCurrentLine = StationChangerIndexCurrentLine - CurrentStationIndex  +1
                        StationCounterInDropLine = DropStationIndex - StationChangerIndexDropLine  
                        StationCounter = StationCounterInCurrentLine + StationCounterInDropLine
                try:
                    return StationCounter,StationOfChanger,FirstDir,SecDir,line[0],line[1],line[2]
                except:
                    return StationCounter,'None',FirstDir,'None',line[0],line[1],line[2]
                
            StationsCounts = selectLiveAndDrop(current_station,drop_station)
            try:     
                counts = StationsCounts[0]
                TransferStation = StationsCounts[1]
            except:
                counts = StationsCounts
            try:
                FirstDir = StationsCounts[2]
                SecDir = StationsCounts[3]
            except:
                pass
            if current_station in StationsCounts[4] or drop_station in StationsCounts[4] or current_station in StationsCounts[5] or drop_station in StationsCounts[5]:
                if counts <= 9:
                    TicketPrice = 3
                elif counts > 9 and counts <= 16:
                    TicketPrice = 5
                elif counts > 16 and counts <= 37:
                    TicketPrice = 7
            if current_station in StationsCounts[6] or drop_station in StationsCounts[6]:
                
                if counts <= 9:
                    TicketPrice = 5
                elif counts > 9 and counts <= 16:
                    TicketPrice = 7
                elif counts > 16 and counts <= 37:
                    TicketPrice = 10

    context = {
        'title' : 'Get Directions Of Egypt Metro',
        'form' : form,
        'current_station' : current_station,
        'drop_station' : drop_station,
        'StationsCounts' : counts,
        'TransferStation' : TransferStation,
        'TicketPrice' : TicketPrice,
        'FirstDir' : FirstDir,
        'SecDir' : SecDir,
    }

    return render(request,'Metro/index.html',context)



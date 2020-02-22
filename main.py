lines ={
    'shobra' : ['المنيب', 'ساقية مكي', 'ام المصريين', 'الجيزة', 'فيصل', 'جامعة القاهرة', 'البحوث', 'الدقي', 'الاوبرا', 'السادات', 'محمد نجيب', 'العتبة', 'الشهداء', 'مسرة', 'روض الفرج', 'سانت تريز', 'الخلفاوي', 'المظلات', 'كلية الزراعة', 'شبرا الخيمة'], 
    'marg'   : ['المرج الجديدة', 'المرج', 'عزبة النخل', 'محطة عين شمس', 'المطرية', 'حلمية الزيتون', 'حدائق الزيتون', 'سراي القبة', 'حمامات القبة', 'كوبري القبة', 'منشية الصدر', 'الدمرداش', 'غمرة', 'الشهداء', 'عرابي', 'ناصر', 'السادات', 'سعد زغلول', 'السيدة زينب', 'الملك الصالح', 'مار جرجس', 'الزهراء', 'دار السلام', 'حدائق المعادي', 'المعادي', 'ثكنات المعادي', 'طره البلد', 'كوتسيكا', 'طره الاسمنت', 'المعصرة', 'حدائق حلوان', 'وادي حوف', 'جامعة حلوان', 'عين حلوان', 'محطة حلوان'],
    'airport': ['نادي الشمس', 'الف مسكن', 'هليوبليس', 'هارون', 'الاهرام', 'كلية البنات', 'الاستاد', 'ارض المعارض', 'العباسية', 'عبده باشا', 'الجيش', 'باب الشعرية', 'العتبة']
}

def CountAndDirStations(current,destination,line):
# Count Number between stations by index (in the list) and get the direction subway
#    Ex : The index of Shobra is 17 and index of Giza is 0
#          if my current station is Giza the result of the subtraction process will be
#          negative and at the same time well be direction of train is the Shobra because
#          it is the last station .
          
    num = current - destination
    if num < 0:
        num *= -1
        return {'StationCount' : num +1,
                'Direction':line[0]}
    else:

        return {'StationCount' : num +1,
                'Direction':line[-1]
                }
def get_StationInfo(From,To):
    #Check if current station and destination station in same line
    # and if true will be return an counts of them of station line if not same line return false
    context = { 'same_line' : False }
    for line in lines:
        if From  in lines[line] and To in lines[line] :
        # If the current station in shobra[shobra stations...]
        # and destination in the same list the condition return True            
            To   = lines[line].index(To) # and here i get index of destination station 
            From = lines[line].index(From) # and here i get index of current station
            StationCountsAndDirction =  CountAndDirStations(To,From,lines[line])
            #Return which direction must be take it to go the destination and number of stations
            context = { 'same_line' : True,
                        'StationCount' : StationCountsAndDirction['StationCount'],
                        'Direction': StationCountsAndDirction['Direction']}
        else:
        # That`s condition will be run if the current station and destination are not in same line
        # and the function will return which destination and current station lines
            for line in lines:
                if From in lines[line]: 
                    context['CurrentLine'] = line
                if To in lines[line]:
                    context['SecLine'] = line
    return context

def CalcPrice(StationCounter,current_station,destination_station):
    # The Ticket price in the airport line of subway is diffrent between other lines
    if  destination_station in lines['airport'] or current_station in lines['airport']:
        # if the destination or current station in airport line 
        # the ticket price will calculated by this conditions
        
        if StationCounter <= 9: # less than or equal 9 stations ticket price is 5
            price = 5
        elif StationCounter <= 16: #bigger than 9 and less that or equal 16 stations ticket price is 7
            price = 7
        elif StationCounter > 16: #bigger than ticket price is 10
            price = 10;
    else:
        if StationCounter <= 9:
            price = 3
        elif StationCounter <= 16:
            price = 5
        elif StationCounter > 16:
            price = 7;
    return price

def GetSwitcherStation(CurrentLine,SecLine,From):
    StationsSwitcher = [x for x in CurrentLine if x in SecLine]
    # this return shared stions with current line and second line
    SharedStations = {}
    for switcher in StationsSwitcher:
    # because in some cases the shared stations is more than 1 station        
        NumbersBetweenSwitcherCurrent = abs((CurrentLine.index(From) - CurrentLine.index(switcher)))
        SharedStations[switcher] = NumbersBetweenSwitcherCurrent
    # i used abs method here because
    # if current station index is 0 and first shared station index is 13 the res will be : -13
    # and the sec shared station is index 14 the result of substraction process is : -14
    # those results stored in SharedStations and if i need get the nearset station that will be return
    # the station is index -14 because it i used the abs to convert the negative to positive
    switcher = min(SharedStations, key=SharedStations.get)
    return switcher 


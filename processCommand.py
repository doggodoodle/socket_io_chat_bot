'''
parseIM takes the IM syntax as input and parses into human readable label and returns it as a string

J 165/150 ps x187 .02/.025	        April 2016 1.65/1.50 Put Spread crossed 1.87 .02/.025
j16 1.50/1.65 psprd x1.87 2/2.5	        April 2016 1.65/1.50 Put Spread crossed 1.87 .02/.025
u16 175p x211 vs f17 175p x255 3.3/3.8	Sep16 1.75 Put crossed 2.11 vs. Jan17 1.75 Put crossed 2.55 .033/.038
U16/F17 1.75 ps x2.11/2.55 .033/.038	Sep16 1.75 Put crossed 2.11 vs. Jan17 1.75 Put crossed 2.55 .033/.038

'''
import re
import time
import sys

#Initialize the codes
monthCode = {'F':'Jan','G':'Feb','H':'Mar','J':'Apr','K':'May','M':'Jun','N':'Jul','Q':'Aug','U':'Sep','V':'Oct','X':'Nov','Z':'Dec'}
stratCode = {'ps':'Put Spread','psprd':'Put Spread','psd':'Put Spread','pspd':'Put Spread','puts':'Put Spread','fence':'Fence'}

def parseIM(argv):    
    #initialize the final Label


    
    #Get the IM syntax
    if len(argv) == 1:
        #print(argv[0])
        syntax = input("Enter IM syntax: ")
    else:
        syntax = argv[1]

    #Split the IM Syntax by spaces
    p = re.compile(r'\s+')
    m=p.split(syntax)
    #print(m)
    if len(m) < 5:
        print("Invalid input!")
        sys.stdout.flush()
        return None

    #Temp variables
    fence = 0
    header = ""
    year = ""
    tempLabel = ""
    prices = ""
    strike = ""
    spread = ""
    strategy = ""

    #Get Month and Year
    tempHeader = re.compile(r'([a-zA-Z])(\d*)/*([a-zA-Z]*)(\d*)')
    m2 = tempHeader.match(m[0])
    month = monthCode[str.upper(m2.group(1))]
    #print('Month:',month)
    year = m2.group(2)
    if len(year) == 2:
        year = "20"+year
    elif year == "":
        year = time.localtime()[0]
        
    #print('Year:',year)

    '''
    #Get 2nd year and month
    if(len(m2.groups())>2):
    print(m2.groups())
    '''

    #get prices
    tempPrices = re.match(r'.+/.+',m[1])
    if tempPrices is None:
        print("Invalid price!")
        sys.stdout.flush()
        return None
    else:
        prices = m[1]
        #print("Price:",prices)
        
    #Get the strategy 
    if len(m) == 5:
        strategy = stratCode[str.lower(m[2])]
    
    #print("Strategy:",strategy)

    #get strike
    tempStrike = re.compile(r'x(.+)')
    m2 = tempStrike.match(m[3])
    if m2 is None:
        print("Invalid strike!")
        sys.stdout.flush()
        return None
    else:
        strike = m2.group(1)
        #print("Strike:",strike)
    
    #get spread
    tempSpread = re.match(r'.+/.+',m[4])
    if tempSpread is None:
        print("Invalid spread!")
        sys.stdout.flush()
        return None
    else:
        spread = m[4]
        #print("Spread:",spread)

    #Concatenate the label
    resultLabel = month + " "+ str(year) + " " + str(prices) + " " + strategy + " crossed " + str(strike) + " " + str(spread)
    print(resultLabel)
    sys.stdout.flush()
    
    return resultLabel
 

if __name__ == "__main__":
    import sys
    parseIM(sys.argv)


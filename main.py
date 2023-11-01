"""
Program Name: main.py
Programmer: goodpasturer
Purpose: sh*ts n giggles
Date: 10/31/2023
"""

##################################################################
##                                                              ##
##                          Initialize                          ##
##                                                              ##
##################################################################

import os
import json
import time
import glob

##############################################################
#                           Choices                          #
##############################################################
#                                                            #
bannerChoice = 0                                             #
#banners key                                                 #
#0 honeycomb                                                 #
#1 double helix                                              #
#2 hearts                                                    #
#3 fence                                                     #
#4 hexa-triangle thingies                                    #
#5 none/blank                                                #
#                                                            #
totlines = 6 #total number of lines the banner will occupy   #
#                                                            #
##############################################################

files = glob.glob('*.json') #list what files are available

for l in range(len(files)):             #print out all files available and what to enter to index them
    print(f'{str(l+1)}:  {files[l]}') 

pickedFile = int(input('which file from the index above?(number please)')) #ask which file to choose and define "pickedFile" value

path = "" #sets the working directory. Currently this one.
file = files[pickedFile-1] #defines the name of the file to be opened, SPECIFICALLY the json output of transcribe


##################################################################
##                                                              ##
##                          Functions                           ##
##                                                              ##
##################################################################


def dictBreakDown(js): #strips each input dictionary(line) of its content, putting a \n after each sentence                 "js" is a dict pulled from the .json
    if (type(js) != dict):  #check if "js" is a dict
        print('Not a dict, type =',str(type(js))) #if it's not a dict, print error message and actual variable type
        return()
    vals = []    #create empty list for 
    jsKeys = list(js.keys())  #pull keys from js

    if (js[jsKeys[0]] == 'pronunciation'):   #if it's a word, output as a word
        for i in range(len(jsKeys)):
            vals.append(js[jsKeys[i]])
        val1 = vals[1][0]
        val1keys = list(val1.keys())
        if 'content' in val1keys:
            return(" " + val1['content'])
        
    elif (js[jsKeys[0]] == 'punctuation'): #if it's a punctuation, output as a punctuation
        for i in range(len(jsKeys)):
            vals.append(js[jsKeys[i]])
        val1 = vals[1][0]
        val1keys = list(val1.keys())
        #print('punk')
        if 'content' in val1keys:
            if (val1['content'] == '.' or val1['content'] == '!' or val1['content'] == '?'): #make a new line if it's the end of a sentence
                return(val1['content'] +"\n")
            else:
                return(val1['content'])
    else:
        print(js[jsKeys[0]]) 


##################################################################
##                                                              ##
##                      .json processing                        ##
##                                                              ##
##################################################################


jason = open(path+file) #opens the .json as jason (moreso just takes the file and gives us the details of it)

jasonLoad = json.load(jason) #loads the file (actually opens it to look at its contents)

jasonLoadItems = tuple(jasonLoad.items()) #breaks out the .json into a tuple(was dict, can't reference dict by position)

jasonJob = list(jasonLoadItems[0]) #finds the title of the video index 0 is "jobName", index 1 is the title

#jasonStatus = list(jasonLoadItems[2]) #pulls the status of the job(likely COMPLETED) index 0 is "status", index 1 is the status

jasonOutput = list(jasonLoadItems[3]) #pulls the results/output of the job, index 0 is "results" index 1 is the output (formatted as a dictionary)

jasonOutput2 = jasonOutput[1] #pulls the results from its header/title (formatted as a dictionary)

jasonOutput2Keys = list(jasonOutput2.keys()) #pulls the keys of the dictionary of the output

jasonItems = jasonOutput2[jasonOutput2Keys[1]] #pulls the output of the dictionary labled with the key "items" (excludes initial transcription, for that print with index 0)

werds = "" #creates empty output word list
for t in range(len(jasonItems)): #loops through each line(?) in the "items"
    werds += dictBreakDown(jasonItems[t]) #runs the "line" through the dictBreakdown() function to strip the excess info and format it


##################################################################
##                                                              ##
##                            Banner                            ##
##                                                              ##
##################################################################


bannerLines = [ [''],[''],[''],[''],[''],['']]
bannerLines[0] = [     #honecomb index 0
    ' /    \      /    \      /    \      /    \      /    \      /    \   ',
    '/      \____/      \____/      \____/      \____/      \____/      \__',
    '\      /    \      /    \      /    \      /    \      /    \      /  ',
    ' \____/      \____/      \____/      \____/      \____/      \____/   '
]

bannerLines[1] = [     #double helix(?) index 1
    "  .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-.   .-.-",
    " / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ \ / / \ ",
    "`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'   `-`-'"
]

bannerLines[2] = [     #hearts index 2
    " .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  .-.-.  ",
    "=`. .'==`. .'==`. .'==`. .'==`. .'==`. .'==`. .'==`. .'==`. .'= ",
    '   "      "      "      "      "      "      "      "      "    ' 
]
bannerLines[3] = [     #fence(I think???) index 3
    "              ,'|     _ |`,      _            ,'|     _ |`,      _      ",
    '(:\          ///     /:) \ \    (:\          ///     /:) \ \    (:\     ',
    ' \:\        )//     /:/   \ (    \:\        )//     /:/   \ (    \:\    ',
    '==\:(======/:(=====):/=====):\====\:(======/:(=====):/=====):\====\:(===',
    '   ) \    /:/     //(       \:\    ) \    /:/     //(       \:\    ) \  ',
    '    \ \  (:/     ///         \:)    \ \  (:/     ///         \:)    \ \ ',
    "     `.|  '     |.'           '      `.|  '     |.'           '      `.|"
    ]

bannerLines[4] = [     #hexa-triangle thingies index 4
'     /   __/     /   __/     /   __/     /   __/     /   __/     /   _',
'__   \__/  \__   \__/  \__   \__/  \__   \__/  \__   \__/  \__   \__/ ',
'  \__/  \     \__/  \     \__/  \     \__/  \     \__/  \     \__/  \ ',
'__/     /   __/     /   __/     /   __/     /   __/     /   __/     / ',
'  \__   \__/  \__   \__/  \__   \__/  \__   \__/  \__   \__/  \__   \_',
'     \__/  \     \__/  \     \__/  \     \__/  \     \__/  \     \__/ ',
'   __/     /   __/     /   __/     /   __/     /   __/     /   __/    ',
'__/  \__   \__/  \__   \__/  \__   \__/  \__   \__/  \__   \__/  \__  ',
'  \     \__/  \     \__/  \     \__/  \     \__/  \     \__/  \     \_',
'  /   __/     /   __/     /   __/     /   __/     /   __/     /   __/ ',
'  \__/  \__   \__/  \__   \__/  \__   \__/  \__   \__/  \__   \__/  \_',
'__/  \     \__/  \     \__/  \     \__/  \     \__/  \     \__/  \    '
]
bannerLines[5] = [     #none/blank index 5
    ""
]

bannerLine = bannerLines[bannerChoice]

banner = ''

for b in range(totlines):
    n = b % len(bannerLine)
    banner = banner + bannerLine[n] + '\n'


##################################################################
##                                                              ##
##                            Output                            ##
##                                                              ##
##################################################################


werds = f'Video File Name: {jasonJob[1]}\nGenerated at: {time.asctime(time.gmtime())} UTC\n \n \n{banner} \n \n{werds} \n \n{banner}\n \n{jasonJob[1]}.txt' #format the text output


############################################################################################
#                                     Example Format                                       #
############################################################################################
#                                                                                          #
#Video File Name: {Name}                                                                   #
#Generated at: {Weekday} {Month} {Day} {Hours}:{Minutes}:{Seconds} {Year} {Time Zone(UTC)} #
#                                                                                          #
#                                                                                          #
#{Banner}                                                                                  #
#                                                                                          #
#                                                                                          #
#{Transcript}                                                                              #
#                                                                                          #
#                                                                                          #
#{banner}                                                                                  #
#                                                                                          #
#                                                                                          #
#{Name}.txt                                                                                #
#                                                                                          #
############################################################################################


werdBytes = str.encode(werds) #encode the formatted text to be written

outie = os.open(f'{jasonJob[1]}.txt',os.O_RDWR|os.O_CREAT) #create/define the output file 

os.write(outie, werdBytes) #write to the output file

os.close(outie) #close the output file
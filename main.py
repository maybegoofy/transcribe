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

myOs = os.name #find what kind of machine being run on
#print(myOs)

#determines what kind of slash is needed to work with the filesystem
if myOs == 'nt':
    fileSystemSlash = "\ "
else:
    fileSystemSlash = '/'
#print(fileSystemSlash)

path = os.getcwd()  #sets the working directory. Currently this one.
pathVid = f'{path}{fileSystemSlash}in{fileSystemSlash}' #sets the directory where videos will be stored
pathIn = f'{path}{fileSystemSlash}out{fileSystemSlash}transcribe{fileSystemSlash}' #sets directory where .json files are stored 
pathOut = f'{path}{fileSystemSlash}out{fileSystemSlash}html{fileSystemSlash}' #sets directory where the .html files will be output

files = glob.glob(f'{pathIn}*.json') #list what files are available

for l in range(len(files)):             #print out all files available and what to enter to index them
    print(f'{str(l+1)}:  {files[l]}') 

pickedFile = int(input('which file from the index above?(number please)')) #ask which file to choose and define "pickedFile" value


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
                return(val1['content'] +"<br>\n\t\t")
            else:
                return(val1['content'])
    else:
        print(js[jsKeys[0]]) 

def fileCopy(file,dest):
    oldFile = os.open(file, os.O_RDONLY)
    newfile = os.open(dest, os.O_RDWR|os.O_CREAT)
    sz = os.path.getsize(file)
    oldBytes = os.read(oldFile,sz)
    os.write(newfile,oldBytes)
    os.close(oldFile)
    os.close(newfile)


##################################################################
##                                                              ##
##                      .json processing                        ##
##                                                              ##
##################################################################


jason = open(file) #opens the .json as jason (moreso just takes the file and gives us the details of it)

jasonLoad = json.load(jason) #loads the file (actually opens it to look at its contents)

jasonLoadItems = tuple(jasonLoad.items()) #breaks out the .json into a tuple(was dict, can't reference dict by position)

jasonJob = list(jasonLoadItems[0]) #finds the title of the video index 0 is "jobName", index 1 is the title

jasonTitle = jasonJob[1][8:] #removes project- from title

pathOutFile = str(jasonJob[1][:len(jasonJob[1])-4]) #defines folder where files will go

#jasonStatus = list(jasonLoadItems[2]) #pulls the status of the job(likely COMPLETED) index 0 is "status", index 1 is the status

jasonOutput = list(jasonLoadItems[3]) #pulls the results/output of the job, index 0 is "results" index 1 is the output (formatted as a dictionary)

jasonOutput2 = jasonOutput[1] #pulls the results from its header/title (formatted as a dictionary)

jasonOutput2Keys = list(jasonOutput2.keys()) #pulls the keys of the dictionary of the output

jasonItems = jasonOutput2[jasonOutput2Keys[1]] #pulls the output of the dictionary labled with the key "items" (excludes initial transcription, for that print with index 0)

werds = "\t\t" #creates empty output word list
for t in range(len(jasonItems)): #loops through each line(?) in the "items"
    werds += dictBreakDown(jasonItems[t]) #runs the "line" through the dictBreakdown() function to strip the excess info and format it


##################################################################
##                                                              ##
##                            Banner                            ##
##                                                              ##
##################################################################


bannerLines = [ [''],[''],[''],[''],[''],['']]

bannerLines[0] = [     #honecomb index 0
    '|&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;|',
    '|/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\____/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\____/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\____/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\____/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\____/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__|',
    '|\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;|',
    '|&nbsp;\____/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\____/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\____/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\____/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\____/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\____/&nbsp;&nbsp;&nbsp;|'
]

bannerLines[1] = [     #double helix(?) index 1
    "|&nbsp;&nbsp;.-.-.&nbsp;&nbsp;&nbsp;.-.-.&nbsp;&nbsp;&nbsp;.-.-.&nbsp;&nbsp;&nbsp;.-.-.&nbsp;&nbsp;&nbsp;.-.-.&nbsp;&nbsp;&nbsp;.-.-.&nbsp;&nbsp;&nbsp;.-.-.&nbsp;&nbsp;&nbsp;.-.-&nbsp;|"
    "|&nbsp;/&nbsp;/&nbsp;\&nbsp;\&nbsp;/&nbsp;/&nbsp;\&nbsp;\&nbsp;/&nbsp;/&nbsp;\&nbsp;\&nbsp;/&nbsp;/&nbsp;\&nbsp;\&nbsp;/&nbsp;/&nbsp;\&nbsp;\&nbsp;/&nbsp;/&nbsp;\&nbsp;\&nbsp;/&nbsp;/&nbsp;\&nbsp;\&nbsp;/&nbsp;/&nbsp;\&nbsp;|"
    "|`-'&nbsp;&nbsp;&nbsp;`-`-'&nbsp;&nbsp;&nbsp;`-`-'&nbsp;&nbsp;&nbsp;`-`-'&nbsp;&nbsp;&nbsp;`-`-'&nbsp;&nbsp;&nbsp;`-`-'&nbsp;&nbsp;&nbsp;`-`-'&nbsp;&nbsp;&nbsp;`-`-'&nbsp;&nbsp;&nbsp;&nbsp;|"
]

bannerLines[2] = [     #hearts index 2
    "|&nbsp;.-.-.&nbsp;&nbsp;.-.-.&nbsp;&nbsp;.-.-.&nbsp;&nbsp;.-.-.&nbsp;&nbsp;.-.-.&nbsp;&nbsp;.-.-.&nbsp;&nbsp;.-.-.&nbsp;&nbsp;.-.-.&nbsp;&nbsp;.-.-.&nbsp;&nbsp;|",
    "|=`.&nbsp;.'==`.&nbsp;.'==`.&nbsp;.'==`.&nbsp;.'==`.&nbsp;.'==`.&nbsp;.'==`.&nbsp;.'==`.&nbsp;.'==`.&nbsp;.'=&nbsp;|",
    '|&nbsp;&nbsp;&nbsp;"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"&nbsp;&nbsp;&nbsp;&nbsp;|'

]

bannerLines[3] = [     #fence(I think???) index 3
    "|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;,'|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_&nbsp;|`,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;,'|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_&nbsp;|`,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|",
    '|(:\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;///&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/:)&nbsp;\&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;(:\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;///&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/:)&nbsp;\&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;(:\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|',
    '|&nbsp;\:\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)//&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/:/&nbsp;&nbsp;&nbsp;\&nbsp;(&nbsp;&nbsp;&nbsp;&nbsp;\:\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)//&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/:/&nbsp;&nbsp;&nbsp;\&nbsp;(&nbsp;&nbsp;&nbsp;&nbsp;\:\&nbsp;&nbsp;&nbsp;&nbsp;|',
    '|==\:(======/:(=====):/=====):\====\:(======/:(=====):/=====):\====\:(===|',
    '|&nbsp;&nbsp;&nbsp;)&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;/:/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//(&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\:\&nbsp;&nbsp;&nbsp;&nbsp;)&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;/:/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//(&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\:\&nbsp;&nbsp;&nbsp;&nbsp;)&nbsp;\&nbsp;&nbsp;|',
    '|&nbsp;&nbsp;&nbsp;&nbsp;\&nbsp;\&nbsp;&nbsp;(:/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;///&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\:)&nbsp;&nbsp;&nbsp;&nbsp;\&nbsp;\&nbsp;&nbsp;(:/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;///&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\:)&nbsp;&nbsp;&nbsp;&nbsp;\&nbsp;\&nbsp;|',
    "|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.|&nbsp;&nbsp;'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|.'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.|&nbsp;&nbsp;'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|.'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.&nbsp;|"
  
]

bannerLines[4] = [     #hexa-triangle thingies index 4
    '|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;_|',
    '|__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;|',
    '|&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;|',
    '|__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;|',
    '|&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\_|',
    '|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;|',
    '|&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;|',
    '|__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;|',
    '|&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\_|',
    '|&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;__/&nbsp;|',
    '|&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\__&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\_|',
    '|__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\__/&nbsp;&nbsp;\&nbsp;&nbsp;&nbsp;&nbsp;|'
]

bannerLines[5] = [     #none/blank index 5
    ""
]

bannerLine = bannerLines[bannerChoice]

banner = ''

for b in range(totlines):
    n = b % len(bannerLine)
    banner = banner + '\t\t' + bannerLine[n] + '<br>\n'

#print(banner)
##################################################################
##                                                              ##
##                            Output                            ##
##                                                              ##
##################################################################


#werdsHTML = f'Video File Name: {jasonJob[1]}\nGenerated at: {time.asctime(time.gmtime())} UTC\n \n \n{banner} \n \n{werds} \n \n{banner}\n \n{jasonJob[1]}.txt' #format the text output
werdsHTML = '<!DOCTYPE html>\n<html lang="en">\n\n<head>\n\t<title>\n\t\t'+str(jasonTitle)+'\n\t</title>\n\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\n\t<style>\n\t\theader {\n\t\t\tfont-family: Franklin Gothic Medium, Arial Narrow, Arial, sans-serif;\n\t\t\tfont-size: 40px;\n\t\t\ttext-align: center;\n\t\t}\n\n\t\ttime {\n\t\t\tfont-family: Franklin Gothic Medium, Arial Narrow, Arial, sans-serif;\n\t\t\tfont-size: 13px;\n\t\t\ttext-align: center;\n\t\t}\n\n\t\th2 {\n\t\t\tfont-family: monospace;\n\t\t\tfont-size: 18px;\n\t\t\ttext-align: center;\n\t\t}\n\n\t\tbody {\n\t\t\tfont-family: Franklin Gothic Medium, Arial Narrow, Arial, sans-serif;\n\t\t}\n\n\t\tfooter {\n\t\t\tfont-family: Franklin Gothic Medium, Arial Narrow, Arial, sans-serif;\n\t\t\tfont-size: 10px;\n\t\t\ttext-align: center;\n\t\t}\n\t\tvideo {\n\t\t\tmax-width: 100%;\n\t\t\theight: auto;\n\t\t}\n\t</style>\n</head>\n\n<header>\n\t<h1>\n\t\t'+str(jasonTitle)+'\n\t</h1>\n</header>\n\n<time>\n\t<p>\n\t\tGenerated at: '+str(time.asctime(time.gmtime()))+' UTC\n\t</p>\n</time>\n\n<body>\n\t<h2>\n\t\t<br>\n'+str(banner)+'\t\t<br>\n\t</h2>\n\n\t<center>\n\t\t<video width=90% controls="controls">\n\t\t\t<source src="'+str(jasonTitle)+'" type="video/mp4" />\n\t\t</video>\n\t</center>\n\n\t<p>\n\t\t<br>\n'+str(werds)+'<br>\n\t</p>\n\n\t<h2>\n\t\t<br>\n'+str(banner)+'\t\t<br>\n\t</h2>\n</body>\n\n<footer>\n\t<p>\n\t\t'+str(jasonJob[1])+'.html\n\t</p>\n</footer>\n\n</html>'

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
#{Name}.html                                                                               #
#                                                                                          #
############################################################################################


werdBytes = str.encode(werdsHTML) #encode the formatted text to be written

os.mkdir(f'{pathOut}{pathOutFile}')

fileCopy(f'{pathVid}{jasonTitle}',f'{pathOut}{pathOutFile}{fileSystemSlash}{jasonTitle}')

outie = os.open(f'{pathOut}{pathOutFile}{fileSystemSlash}{jasonJob[1]}.html',os.O_RDWR|os.O_CREAT) #create/define the output file 

os.write(outie, werdBytes) #write to the output file

os.close(outie) #close the output file
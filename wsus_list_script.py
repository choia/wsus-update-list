import re

#URL string that concatenate with KB
kbURL = "http://support.microsoft.com/kb/"

#Creating empty lists that KB numbers will append
generalWindowsList = []
systemCenterList = []
server2003List = []
server2008List = []
server2012List = []
sqlList = []
windows7List = []
windows8List = []
officeList = []

# Creating a list with keywords that will be used to search in text file
kwGeneralWindows = ['General Windows', 'Malicious Software Removal Tool', 'Windows Defender']
kwSystemCenter = ['System Center']
kwServer2003 = ['Server 2003']
kwServer2008 = ['Server 2008']
kwServer2012 = ['Server 2012']
kwSql = ['SQL']
kwWindows7 = ['Windows 7']
kwWindows8 = ['Windows 8']
kwOffice = ['Office', 'Project', 'Skype', 'Word', 'Visio', 'PowerPoint', 'Excel', 'Outlook', 'OneNote', 'OneDrive', \
          'Access', 'SharePoint']

# Function that takes two argument: First Arg (keyword lists), Second Arg (empty lists)
def listRegex (keyWordList, emptyList):
        for i in range(len(keyWordList)):                      # Loop through keywords in the list
            if keyWordList[i] in item:                         # If there is keyword in the line
                kb = re.compile(r'KB\d+')                   # Creating matching pattern like 'KB123456'
                kbNumber = kb.search(item)                  # Search for 'KB' following numbers and put that into variable
                return emptyList.append(kbNumber.group())   # Append it to emptylists(Second Arg) and return it
            else:
                "None"

# Fucntion that takes two argument: Checks and writes 
def writeFile (keyWordList, emptyList):
    w.write(keyWordList[0]+'\n')
    for i in set(emptyList):                    # Remove duplicates in list, loop only once
        w.write(kbURL+i[2:]+'\n')               # Concatenate the URL and write Files
    w.write('\n')


with open(r'd:\GitProject\wsus_list_script\Files\wsuslist.txt') as f: 
    for item in f:
        listRegex(kwOffice, officeList)
        listRegex(kwSql, sqlList)
        listRegex(kwSystemCenter, systemCenterList)
        listRegex(kwServer2003, server2003List)
        listRegex(kwServer2008, server2008List)
        listRegex(kwServer2012, server2012List)
        listRegex(kwWindows7, windows7List)
        listRegex(kwWindows8, windows8List)
        listRegex(kwGeneralWindows, generalWindowsList)

        
with open(r'd:\GitProject\wsus_list_script\Files\result.txt', 'w+') as w:
    writeFile(kwOffice, officeList)
    writeFile(kwSql, sqlList)
    writeFile(kwSystemCenter, systemCenterList)
    writeFile(kwServer2003, server2003List)
    writeFile(kwServer2008, server2008List)
    writeFile(kwServer2012, server2012List)
    writeFile(kwWindows7, windows7List)
    writeFile(kwWindows8, windows8List)
    writeFile(kwGeneralWindows, generalWindowsList)
    w.close()


        


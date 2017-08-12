from bs4 import BeautifulSoup
import requests
import xml.etree.cElementTree as ET
import os, os.path
import types

#Create Root element for all albums
albums = ET.Element("albums")

#In this case the old website did not have album info so all lyrics will be sorted in the same unknown album
#TODO loop through all albums if info available in old files
album = ET.SubElement(albums, "album", name="add album name here", year="add album year here", buy="add link to shop here")

#configuration : Set here the directory where you put your old lyrics files
directory = 'old/'

#Loop through all files in directory
for filename in os.listdir(directory):
    soup = BeautifulSoup(open(directory+filename).read(), "lxml")
    #r = requests.get("http://localhost/unionjacklyrics/1939.htm")
    #r  = requests.get("http://" +url)

    #data = r.text


    #My old files were poorly written, so I had to remove all BR from it
    for br in soup.findAll('br'):
        br.extract()

    myLyrics = []
    title = ''

    #brows through all Paragraph in the file
    for p in soup.find_all('p'):

        for item in p.contents :
            if( item != '\n'):
                if (item.name == "span" or item.name == "p"):
                    #Titles usually have a "class=style27" in my example
                    if (item.get('class')[0]=="Style27"):
                        if (item.strong is not None):
                            titleArr = item.strong.contents
                            titleContents = ''
                            for titleCont in titleArr :
                                titleContents += titleCont
                            title = titleCont
                    elif (item.strip() != '') :
                        #If this is not a title, it's lyric part
                        myLyrics.append(item.strip())
                elif (item.name == None and item.strip() != ''):
                    #Sometimes title have no class item, so 1st text is title
                    if(title==''):
                        title = item.strip()
                    else :
                        #If this is not a title, it's lyric part
                        myLyrics.append(item.strip())
                if (item.name == "strong"):
                    #Some items are
                    contents =''
                    for var in item.contents:
                        contents += var
                    myLyrics.append(contents.strip())


    #Create the song XML element, add the title to it
    song = ET.SubElement(album, "song", name=title)
    print("Title : "+title)

    #Run through the myLyrics array to add parts to the song Xml element
    for lyric in myLyrics :
        part = ET.SubElement(song, "part", type="a ajouter")
        part.text = lyric
        print("Lyric : "+lyric)


tree = ET.ElementTree(albums)
#Generate XML file
tree.write("songs.xml",encoding='utf-8', xml_declaration=True )

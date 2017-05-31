import os
from xml.dom import minidom

from data_entry import data_container

def generate_list(ws):
    cwf = os.getcwd() + "\\_database\\" + ws + "\\" + ws + ".xml"
    
    if (os.path.exists(cwf)):
        #load and parse the selected database
        doc = minidom.parse(cwf)
        entries = doc.getElementsByTagName('entry')
        return_list = []

        #iterate through the list of available entries found
        #in the database.
        for entry in entries:
            year = "unknown"
            description = "unknown"
            genre = "unknown"
            players = "unknown"
            rating = "unknown"
            visible = "unknown"

            name = entry.getAttribute('name')
            yr_ck = entry.getElementsByTagName('players')[0].childNodes
            ds_ck = entry.getElementsByTagName('description')[0].childNodes
            gn_ck = entry.getElementsByTagName('genre')[0].childNodes
            pl_ck = entry.getElementsByTagName('players')[0].childNodes
            rt_ck = entry.getElementsByTagName('rating')[0].childNodes
            vs_ck = entry.getElementsByTagName('visible')[0].childNodes
            if yr_ck:
                year = entry.getElementsByTagName('year')[0].childNodes[0].nodeValue
            if ds_ck:
                description = entry.getElementsByTagName('description')[0].childNodes[0].nodeValue
            if gn_ck:
                entry.getElementsByTagName('genre')[0].childNodes[0].nodeValue
            if pl_ck:
                players = entry.getElementsByTagName('players')[0].childNodes[0].nodeValue
            if rt_ck:
                rating = entry.getElementsByTagName('rating')[0].childNodes[0].nodeValue
            if vs_ck:
                visible = entry.getElementsByTagName('visible')[0].childNodes[0].nodeValue    
                
            #create a new object and add it to the 
            #returning array
            new_entry = data_container(name, description, genre, year, players, rating, visible)   
            return_list.append(new_entry)
        #return the array of objects
        return return_list
    else:
        #the specified database could not be loaded
        print "unable to load " + ws + ".xml"
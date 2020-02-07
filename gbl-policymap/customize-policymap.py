import csv
import json
import os
from datetime import datetime
​
single_dict = { #dictionary to translate single-value Dublin Core/GBL fields into GBLJson
    "layer-slug":["layer_slug_s"],
    "dc_identifier_s":["dc_identifier_s"],
    "title":["dc_title_s"],
    "description":["dc_description_s"],
    "solr year":["solr_year_i"],
    "provenance":["dct_provenance_s"],
    "format":["dc_format_s"],
    "geometry type":["layer_geom_type_s"],
    "rights":["dc_rights_s"],
    "solr_geom":["solr_geom"]
    }
multiple_dict = { #dictionary to translate multivalue Dublin Core/GBL fields into GBLJson
    "is part of":["dct_isPartOf_sm"],
    "subject":["dc_subject_sm"],
    "temporal coverage":["dct_temporal_sm"],
    "spatial coverage":["dct_spatial_sm"],
    "creator":["dc_creator_sm"],
    "language":["dc_language_s"],
    "type":["dc_type_s"]
    }
if not os.path.exists("json"): #create a folder to store the jsons if one does not already exist
    os.mkdir("json")
​
csvfile = open('policy-map-data-directory.csv', 'r') #opens the csv with the GBL data. Change this as needed
​
reader = csv.DictReader(csvfile)
date_modified = datetime.today().strftime('%Y-%m-%d')+"T"+datetime.today().strftime('%X')+"Z" #sets date modified to the current date
​
for row in reader: #each row is a dictionary
    identifier = ""
    ref = []
    small_dict = {"geoblacklight_version":"1.0","layer_modified_dt":date_modified} #starting dictionary with set values
    for key,val in row.items():
        if key == "identifier":
            identifier = val
            if not os.path.exists("json/" + val): #makes a new folder for each id
                os.mkdir("json/" + val)
        if key in single_dict:
            for fieldname in single_dict[key]:
                small_dict[fieldname] = val
        if key in multiple_dict:
            for fieldname in multiple_dict[key]:
                small_dict[fieldname] = val.split('|') #creates a list with the multiple values
        if key == "more details" and val != '':
            to_append = '"http://schema.org/url":"' + val + '"'
            #print(to_append)
            ref.append(to_append)
        if key == "documentation" and val != '':
            to_append = '"http://lccn.loc.gov/sh85035852":"' + val + '"'
            ref.append(to_append)
        if key == "download" and val != '':
            to_append = '"ttp://schema.org/downloadUrl":"' + val + '"'
            ref.append(to_append)
        if key == "MapServer" and val != '':
            to_append = '"urn:x-esri:serviceType:ArcGIS#DynamicMapLayer":"' + val + '"'
            ref.append(to_append)
        if key == "FeatureServer" and val != '':
            to_append = '"urn:x-esri:serviceType:ArcGIS#FeatureLayer":"' + val + '"'
            ref.append(to_append)
        if key == "ImageServer" and val != '':
            to_append = '"urn:x-esri:serviceType:ArcGIS#ImageMapLayer":"' + val + '"'
            ref.append(to_append)
        if key == "ISO Metadata" and val != '':
            to_append = '"http://www.isotc211.org/schemas/2005/gmd/":"' + val + '"'
            ref.append(to_append)
        if key == "FGDC Metadata" and val != '':
            to_append = '"http://www.opengis.net/cat/csw/csdgm":"' + val + '"'
            ref.append(to_append)
        if key == "WFS" and val != '':
            to_append = '"http://www.opengis.net/def/serviceType/ogc/wfs":"' + val + '"'
            ref.append(to_append)
        if key == "WMS" and val != '':
            to_append = '"http://www.opengis.net/def/serviceType/ogc/wms":"' + val + '"'
            ref.append(to_append)
        if key == "WCS" and val != '':
            to_append = '"http://www.opengis.net/def/serviceType/ogc/wcs":"' + val + '"'
            ref.append(to_append)
        if key == "HTML" and val != '':
            to_append = '"http://www.w3.org/1999/xhtml":"' + val + '"'
            ref.append(to_append)
        if key == "IIIF" and val != '':
            to_append = '"http://iiif.io/api/image":"' + val + '"'
            ref.append(to_append)
        if key == "Manifest" and val != '':
            to_append = '"http://iiif.io/api/presentation#manifest":"' + val + '"'
            ref.append(to_append)
        if key == "IndexMaps" and val != '':
            to_append = '"https://openindexmaps.org":"' + val + '"'
            ref.append(to_append)
    small_dict["dct_references_s"] = '{' + (','.join(ref)) + '}'
    iden = row['identifier']
    filename = "geoblacklight.json"
    with open("json/"+identifier+"/"+filename, 'w') as jsonfile: #writes to a json with the identifier as the filename
        json.dump(small_dict,jsonfile,indent=2)

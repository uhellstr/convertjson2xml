#!/usr/bin/env python
# coding: UTF-8

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Simple Python routine to convert JSON to XML
    Example: python convert.py /home/hellsulf/orascript/json2xml/JSON/2020_8_f1.json

    Note: Requires json2xml
    pip install json2xml
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    
"""


import sys
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
from pathlib import Path 


def gen_xmlfile_from_json_file(inputfile):

    jsonfile = Path(inputfile).name
    xmlname = jsonfile.replace("json", "xml")
    return xmlname

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Main 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
def main():

    jsonfile = str(sys.argv[1])
    outdir = str(sys.argv[2])
    xmlname = gen_xmlfile_from_json_file(jsonfile)
    xmlfilename = outdir + '/' + xmlname
    outfilemk = open(xmlfilename,"w")
    data = readfromjson(jsonfile)
    outfile.write(json2xml.Json2xml(data, attr_type=False).to_xml())
    outfile.close()

if __name__ == "__main__":
    main()
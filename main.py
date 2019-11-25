from pypdf2xmlfolder import pdf2xml
import re


import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XML, fromstring, tostring
def get_xmldata(pdf_path):
    xml_data = pdf2xml(pdf_path, 'rb')
    xml_data=fromstring(xml_data)
    tree = ET.ElementTree(xml_data)
    root = tree.getroot()
    xml_data_list=[]
    col_data={}
    for ele in root:
        temp_col1=[]
        for sub_ele in ele:
            print(sub_ele.text)
            xml_data_list.append(sub_ele.text)
    return xml_data_list

    

list_of_xmldata=get_xmldata('xyz.pdf')

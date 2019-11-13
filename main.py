from pypdf2xmlfolder import pdf2xml
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XML, fromstring, tostring
def get_xmldata(pdf_path):#,addlist,col_headerlist):
    xml_data = pdf2xml(pdf_path, 'rb')
    xml_data=fromstring(xml_data)
    tree = ET.ElementTree(xml_data)
    root = tree.getroot()
    adds={}
    adds1={}
    col_data={}
    for ele in root:
        temp_col1=[]
        for sub_ele in ele:
            print(sub_ele.text)

    

get_xmldata('C:/Users/Techforce/Downloads/01.Apr-18_GSTR3B.pdf')

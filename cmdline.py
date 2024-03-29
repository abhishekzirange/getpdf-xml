import sys, getopt
import main
def main1(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <pdffile_path>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
   print 'pdf_path is "', inputfile
   return inputfile

if __name__ == "__main__":
   pdf_path=main1(sys.argv[1:])
   main.get_xmldata(pdf_path)

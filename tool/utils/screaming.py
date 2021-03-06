import csv
import io

def readcsvraport(csvfileraw):
     decoded_file = csvfileraw.file.read().decode('utf-8').strip()
     io_string = io.StringIO(decoded_file)
     csv_reader = csv.reader(io_string,delimiter=',', quotechar='"')
     csvlist=list(csv_reader)

     try:
         print(csvlist[236][1])
     except:
         csvlist[236] = [0,0,0]
     if csvlist[237][1] == None:
         csvlist[237] = [0,0,0]
     if csvlist[238][1] == None:
         csvlist[238] = [0, 0, 0]
     if csvlist[239][1] == None:
         csvlist[239] = [0, 0, 0]
     if csvlist[240][1] == None:
         csvlist[240] = [0, 0, 0]
     if csvlist[241][1] == None:
         csvlist[241] = [0, 0, 0]

     try:
         print(csvlist[246][1])
     except:
          csvlist[246] = [0, 0, 0]
     try:
         print(csvlist[274][1])
     except:
          csvlist.append([0, 0, 0])
     try:
         print(csvlist[275][1])
     except:
         csvlist.append([0, 0, 0])
     try:
         print(csvlist[276][1])
     except:
          csvlist.append([0, 0, 0])
     return csvlist


def readcsvallraport(csvfileraw):
    decoded_file = csvfileraw.file.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    csv_reader = csv.reader(io_string, delimiter=',', quotechar='"')
    csvlist = list(csv_reader)[1:]
    return (csvlist)


class NameScreaming():

    def read():
        with open('tool/utils/crawl_overview.csv', encoding="UTF-8") as csvfile:
            spamreader = list(csv.reader(csvfile, delimiter=',', quotechar='"'))
            return spamreader

    def rownumber(number):
        row = NameScreaming.read()
        rownumber = row[number]
        return rownumber

    def service():
        return NameScreaming.rownumber(1)[1]

    def summary():
        a = NameScreaming.rownumber(6)
        b = NameScreaming.rownumber(7)
        c = NameScreaming.rownumber(8)
        d = NameScreaming.rownumber(9)
        return a,b,c,d

    def internal():
        internal = list()
        for i in range(17, 24):
            internal.append(NameScreaming.rownumber(i))
        return internal

    def response_codes():
        lista = list()
        for i in range(41,51):
            lista.append(NameScreaming.rownumber(i))
        return lista

    def uri():
        URI = list()
        for i in range(58, 64):
            URI.append(NameScreaming.rownumber(i))
        return URI

    def page_titles():
        page_titles= list()
        for i in range(67, 75):
            page_titles.append(NameScreaming.rownumber(i))
        return page_titles

    def meta_description():
        meta_description= list()
        for i in range(78, 85):
            meta_description.append(NameScreaming.rownumber(i))
        return meta_description

    def h1():
        h1 = list()
        for i in range(94, 98):
            h1.append(NameScreaming.rownumber(i))
        return h1

    def h2():
        h2 = list()
        for i in range(101, 105):
            h2.append(NameScreaming.rownumber(i))
        return h2

    def images():
        images = list()
        for i in range(108, 111):
            images.append(NameScreaming.rownumber(i))
        return images


#
# def readcsvraporttest(csvfileraw):
#
#      csv_reader = csv.reader(csvfileraw,delimiter=',', quotechar='"')
#      csvlist=list(csv_reader)
#      for index, i in enumerate(csvlist):
#          print(str(index)+' '+ str(i))
#
#
#      return csvlist
#
#
# def opener():
#         with open('crawl_overview.csv') as readfile:
#             readcsvraporttest(readfile)
# opener()
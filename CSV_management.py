import pandas as pd
import numpy as np
import time
import progressbar
from ECC_encryption import *
import csv
from listElementToBytes import *
import fontstyle

widgets = [' [',
           progressbar.Timer(format='elapsed time: %(elapsed)s'),
           '] ',
           progressbar.Bar('*'), ' (',
           progressbar.ETA(), ') ',
           ]

def CSV_to_encrycsv(path, pubkey, path2):
    text = fontstyle.apply('ENCRYPTING', 'bold/red/BLACK_BG')
    print("   ********                             ********")
    print("  **********                           **********")
    print(" ************       ",text,"      ************")
    print("  **********                           **********")
    print("   ********                             ********")
    list1 = []
    with open(path) as file_obj:
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            list1.append(row)
    index = list1[0]
    list1.pop(0)
    # <<<<<<<<<<<EncryptionProcess>>>>>>>>>>>>
    bar = progressbar.ProgressBar(max_value=len(list1),
                                  widgets=widgets).start()
    for i in range(len(list1)):
        bar.update(i)
        for j in range(len(list1[0])):
            k = str(list1[i][j]).encode("utf-8")
            k1 = encrypt_ECC(k, pubkey)
            list1[i][j] = k1
    # <<<<<<<<<<<<<<<Save as csv>>>>>>>>>>>>>>>>>>>>
    list1.append(index)
    myFile = open(path2, 'w')
    writer = csv.writer(myFile)
    writer.writerow(index)
    for data_list in list1:
        writer.writerow(data_list)
    myFile.close()
    return list1



def CSV_to_decrycsv(list1,index,privatekey,path2):
    text = fontstyle.apply('DECRYPTING', 'bold/red/BLACK_BG')
    print("   ********                             ********")
    print("  **********                           **********")
    print(" ************       ",text,"      ************")
    print("  **********                           **********")
    print("   ********                             ********")
    #<<<<<<<<<<<EncryptionProcess>>>>>>>>>>>>
    bar = progressbar.ProgressBar(max_value=len(list1), 
                              widgets=widgets).start()
    for i in range (0,len(list1)):
      bar.update(i)
      for j in range (0,len(list1[0])):
        res=list1[i][j]
        res=pickle.loads(res)
        k1=decrypt_ECC(res,privatekey)
        list1[i][j]=k1.decode('utf-8')
    #<<<<<<<<<<<<<<<Save as csv>>>>>>>>>>>>>>>>>>>>
    myFile = open(path2, 'w')
    writer = csv.writer(myFile)
    writer.writerow(index)
    for data_list in list1:
        writer.writerow(data_list)
    myFile.close()
    return list1


def list_to_csv(name,list1,column):
  myFile = open(name, 'w')
  writer = csv.writer(myFile)
  writer.writerow(column)
  for data_list in list1:
    writer.writerow(data_list)
  myFile.close()
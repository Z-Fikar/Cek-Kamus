import os
import sys
import polib
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def cekkamus(kata):
    with open ('Kamus.txt', 'r') as myfile:
        data=myfile.readlines()
    return data

def main(alamat):
    hitung=0
    print 'Memproses :',alamat
    print '-'*50
    po = polib.pofile(alamat)
    for entry in po:
        kalimat = stemmer.stem(entry.msgstr.encode('utf-8')).split(' ')
        for kata in kalimat:
            if kata and all(kata.lower() != (kamus.split('\n'))[0] for kamus in cekkamus(kata)):
                hitung+=1
                print 'Kesalahan ke-%d'%hitung
                print 'msgstr :',entry.msgstr
                print 'kata   :',kata
                print
    print '-'*50
    print 'Jumlah Kesalahan:',hitung
    
def awal():
    print '='*50
    print ' |',' '*7,'CekKamus dibuat oleh Zulfikar',' '*6,'|'
    print '='*50

if __name__ == '__main__':
    awal()
    if (len(sys.argv) >= 2):
        p = sys.argv[1]
        if (os.path.isfile(p) and p[-3:] == '.po'):
            main(p)
        else:
            print 'Tidak ada file PO yang bernama \'%s\''%p
    else:
        print('Penggunaan : python cekkamus.py alamat/ke/file.po')

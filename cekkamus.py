import os
import sys
import polib
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def cekkamus(kata):
    with open ('Kamus/%s.txt'%kata[:1].upper(), 'r') as myfile:
        data=myfile.readlines()
    return data

def cekerror(alamat):
    print 'Memproses :',alamat
    print '-'*50
    po = polib.pofile(alamat)
    for entry in po:
        kalimat = stemmer.stem(entry.msgstr.encode('utf-8')).split(' ')
        for kata in kalimat:
            if kata:
                kbbi=cekkamus(kata)
                listk=[]
                for word in kbbi:
                    kk=(word.split(' '))[0].lower()
                    if kk[-1:]==',':
                        kk=kk[:-1]
                    listk.append(kk)
                if all(kata.lower() != kamus for kamus in listk):
                    print 'msgstr :',entry.msgstr
                    print 'kata   :',kata
                    print
def judul():
    print '='*50
    print ' |',' '*7,'CekKamus dibuat oleh Zulfikar',' '*6,'|'
    print '='*50

if __name__ == '__main__':
    judul()
    if (len(sys.argv) >= 2):
        p = sys.argv[1]
        if (os.path.isfile(p) and p[-3:] == '.po'):
            cekerror(p)
        else:
            print 'Tidak ada file PO yang bernama \'%s\''%p
    else:
        print('Penggunaan : python cekkamus.py alamat/ke/file.po')

import os
import sys
import polib
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def cekkamus():
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
            try:
                if kata and all(kata.lower() != (kamus.split('\n'))[0] for kamus in cekkamus()):
                    print 'msgstr :',entry.msgstr
                    print 'kata   :',kata
                    dekat=[]
                    depan=[]
                    belakang=[]
                    for kamus in cekkamus():
                        lema=(kamus.split('\n'))[0]
                        if kata in lema:
                            if lema[:len(kata)]==kata and len(lema)<=(len(kata)+1):
                                dekat.append(lema)
                        for i in range(3,len(kata)+1):
                            awal=stemmer.stem(kata[:i])
                            if awal==lema:
                                string=kata[:i]+' '+kata[i:]
                                if string not in depan:
                                    depan.append(string)
                        for j in range(0,len(kata)-2):
                            awal=stemmer.stem(kata[j:]:
                            if awal==lema:
                                string=kata[:j]+' '+kata[j:]
                                if string not in belakang:
                                    belakang.append(string)
                        
                    if dekat!=[]:
                        print '# Mendekati:\n#',dekat
                    saran=list(set(depan) & set(belakang))
                    if saran!=[]:
                        print '# Apa yang anda maksud ini:\n#',sorted(saran)
                    print
            except KeyboardInterrupt:
                print '# Dilewati\n'
    print '-'*50
    
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

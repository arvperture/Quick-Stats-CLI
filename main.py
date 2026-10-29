import inputDataset
import math
from inputDataset import dataset as lst
from inputDataset import divider

banyakData = len(lst)
print(f'N = {banyakData}')

def meanTunggal(data):
    mean = sum(data) / len(data)
    print(f'Mean \t= {mean}')
    return mean

def medianTunggal(data):
    median = 0
    if banyakData % 2 == 0:
        med1 = (banyakData // 2) - 1
        med2 = (banyakData // 2)
        operasi = (data[med1] + data[med2]) / 2
        median += operasi
    else:
        med = (banyakData // 2)
        operasi = data[med]
        median += operasi
    print(f'Median \t= {median}')
    return median

def modusTunggal(data):
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1

    nilaiMaks = max(freq.values())

    modus = [k for k, v in freq.items() if v == nilaiMaks]
    print(f'Modus \t= {modus}')
    return modus

print('\nDATA TUNGGAL:')
meanTunggal(lst)
medianTunggal(lst)
modusTunggal(lst)
print(divider)

def jumlahKelas(data):
    penentuanClass = str(input('banyak kelas ditentukan sendiri?\ty/n: '))
    banyakKelas = 0
    if penentuanClass == 'y':
        banyakKelas += int(input('Class\t: '))
    elif penentuanClass == 'n':
        logaritma = math.log(len(data))
        hasilLog = 1 + 3.3 * logaritma
        if hasilLog % 1 >= 0.5:
            banyakKelas += int(hasilLog) + 1
        else:
            banyakKelas += int(hasilLog) 
    print(f'\njumlah kelas \t= {banyakKelas}')
    return banyakKelas

def lebarKelas(data, n):
    terbesar = max(data)
    terkecil = min(data)
    classWidth = (max(data) - min(data)) / n
    lebKelas = round(classWidth, 2)
    print(f'''Terbesar \t= {terbesar}
Terkecil \t= {terkecil}
lebarKelas \t= {lebKelas}''')
    return lebKelas
    

def tabelDistribusi(data, n):
    tepiBawah = data[0]
    print('''|| Class Limit\t\t| Freq\t\t| MidPoint\t| FreqRel\t| CummuFreq\t\t||
==========================================================================''')
    for data in range(int(n)):
        tepiAtas = tepiBawah + lebKelas
        rentang = f'{tepiBawah} - {tepiAtas}'
        frekuensi = 0
        midPoint = 0
        frekRel = 0
        cummuFreq = 0
        tepiBawah += lebKelas
        round(tepiBawah, 2)
        print(f'|| {rentang}\t\t| {frekuensi}\t\t| {midPoint}\t\t| {frekRel}\t\t| {cummuFreq}\t\t||')

print('DATA KELOMPOK:\n')
banyakKelas = jumlahKelas(lst)
lebKelas = lebarKelas(lst, banyakKelas)
print('\nTabel Distribusi')
tabelDistribusi(lst, banyakKelas)
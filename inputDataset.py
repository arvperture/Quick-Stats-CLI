print('''
====================
 STATISTIKA SEMES 1
====================''')

inputDataset = []
namaDataset = str(input('\nNama Dataset?\t: '))
opreasi = 1

print('\n"Enter" lagi untuk stop')
urutanData = 0
while opreasi == 1:
    himpData = (input(f'Input data ke - {urutanData + 1}\t: '))
    inputDataset.append(himpData)
    if himpData == '':
        inputDataset.remove('')
        doneQuest = input('selesai?\ty/n: ')
        if doneQuest == 'n':
            continue
        elif doneQuest == 'y':
            break
    urutanData += 1

RAWdataset = []
for x in inputDataset:
    RAWdataset.append(float(x))

dataset = sorted(RAWdataset)
divider = '======================================================='
print(f'''
{divider}
Nama Dataset: {namaDataset.upper()}
Dataset Input:
{dataset}
{divider}''')
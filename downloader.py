# cara menulis file di dalam python secara otomatis
# with open('test.txt', 'w') as file:
#     file.write('kuntul.com')

# https://megapolitan.kompas.com/read/2023/10/06/15163351/sindir-anak-buah-yang-incar-jabatan-heru-budi-promosi-untuk-asn-yang
import requests

html = requests.get('https://megapolitan.kompas.com/read/2023/10/06/15163351/sindir-anak-buah-yang-incar-jabatan-heru-budi-promosi-untuk-asn-yang').content 
with open('oke.html', 'w') as file:
    file.write('<html><head></head>' + html.decode().split('</head>')[1])
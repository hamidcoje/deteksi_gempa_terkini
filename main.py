"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 11 April 2022
    Waktu: 10:06:57 WIB
    Magnitudo: 3.9
    Kedalaman: 55 km
    Lokasi: LS=5.26 - BT=103.86
    Pusat Gempa: Pusat gempa berada di laut 11 km Barat daya Pesisir Barat
    Dirasakan: Dirasakan (Skala MMI): II Pesisir Barat
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '11 April 2022'
    hasil['waktu'] = '10:06:57 WIB'
    hasil['magnitudo'] = 3.9
    hasil['lokasi'] = {'ls': 5.26, 'bt': 103.86}
    hasil['pusat'] = 'Pusat gempa berada di laut 11 km Barat daya Pesisir Barat'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II Pesisir Barat'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")




if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)
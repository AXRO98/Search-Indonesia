"""
[=================================================]
 Copyright (C) 2023 axroc98. All rights reserved.
[=================================================]
 This message is intended to protect the copyright of the works contained in this document.
 All material within this document, including but not limited to text, images, graphics, audio, video, and other materials, are the exclusive property of axroc98 unless otherwise stated.
 Duplication or distribution of the whole or partial content of this document is not permitted without permission from axroc98.
 Any modification, reproduction, or republication of this content without written permission from the copyright owner is strictly prohibited. 
 Violation of these terms constitutes an infringement of exclusive rights and may result in legal action as per the applicable regulations.
 axroc98 reserves the right to take necessary measures to protect its copyright and intellectual property.
 The use of trademarks or service marks visible in this document does not imply any endorsement or affiliation between axroc98 and the owners of such trademarks.
 For inquiries or requests regarding copyright, please contact us via the email address listed in this document.
 Thank you for your understanding and compliance with this copyright notice. We hope this document provides valuable benefits and information, and remains a well-protected asset.
 © 2023 axroc98. All rights reserved under the law.

[==========================]
 Contact Me:
 Email: axroc98@proton.me
[==========================]
"""

logo = """
   _____                                _     
  / ____|                              | |    
 | (___     ___    __ _   _ __    ___  | |__  
  \___ \   / _ \  / _` | | '__|  / __| | '_ \ 
  ____) | |  __/ | (_| | | |    | (__  | | | |
 |_____/   \___|  \__,_| |_|     \___| |_| |_|
        Indonesia\n\n"""

import json

def search(data, keyword):
    found_no = 0
    found = False  # Variabel penanda untuk menandakan apakah hasil ditemukan
    
    print("\n[===========================================]")
    print(f"              Result {keyword}")
    print("[===========================================]")
    for provinsi in data['provinsi']:
        if keyword.lower() in provinsi['nama'].lower():
            print("\n[===============[ PROVINSI ]================]")
            print(f" ID Provinsi: {provinsi['id']}")
            print(f" Nama Provinsi: {provinsi['nama']}")
            print("[===========================================]\n")
            found = True
            found_no += 1
        
        for kabupaten in provinsi['kabupaten']:
            if keyword.lower() in kabupaten['nama'].lower():
                print("\n[===============[ KABUPATEN ]===============]")
                print(f" Nama Provinsi: {provinsi['nama']}")
                print(f" ID Provinsi: {provinsi['id']}")
                print(f" Nama Kabupaten/Kota: {kabupaten['nama']}")
                print(f" ID Kabupaten/Kota: {kabupaten['id'][2:]}")
                print("[===========================================]\n")
                found = True
                found_no += 1
                
            for kecamatan in kabupaten['kecamatan']:
                if keyword.lower() in kecamatan['nama'].lower():
                    print("\n[===============[ KECAMATAN ]===============]")
                    print(f" Nama Provinsi: {provinsi['nama']}")
                    print(f" ID Provinsi: {provinsi['id']}")
                    print(f" Nama Kabupaten/Kota: {kabupaten['nama']}")
                    print(f" ID Kabupaten/Kota: {kabupaten['id'][2:]}")
                    print(f" Kecamatan: {kecamatan['nama']}")
                    print(f" ID Kecamatan: {kecamatan['id'][4:]}")
                    print("[=============================================]\n")
                    found = True
                    found_no += 1
                    
                for kelurahan in kecamatan['kelurahan']:
                    if isinstance(kelurahan, dict) and keyword.lower() in kelurahan.get('nama', '').lower():
                        print("\n[===============[ KELURAHAN ]===============]")
                        print(f" Nama Provinsi: {provinsi['nama']}")
                        print(f" ID Provinsi: {provinsi['id']}")
                        print(f" Nama Kabupaten/Kota: {kabupaten['nama']}")
                        print(f" ID Kabupaten/Kota: {kabupaten['id'][2:]}")
                        print(f" Kecamatan: {kecamatan['nama']}")
                        print(f" ID Kecamatan: {kecamatan['id'][4:]}")
                        print(f" Kelurahan/Desa: {kelurahan['nama']}")
                        print(f" ID Kelurahan/Desa: {kelurahan['id'][6:]}")
                        print("[===========================================]\n")
                        found = True
                        found_no += 1
                        
    if found:
        print(f"Found {found_no} name(s)")
    else:
        print("Nama tempat tidak ditemukan.")

# Menggunakan data.json yang telah diberikan
with open('code_wilayah_indonesia_38_provinsi.json') as file:
    data = json.load(file)

# Contoh penggunaan fungsi search
print(logo)
search(data, input("Search: "))

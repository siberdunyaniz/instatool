#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import requests
import webbrowser
import base64 as b64
import binascii as ba
from colorama import Fore, Style, init
from getpass import getpass

# Colorama'yı başlat
init(autoreset=True)

# 3D ARIVA giriş ekranı için ASCII Art
def print_login_banner():
    banner = r"""
                                     
 ▄▀▀█▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀█▄  
▐ ▄▀ ▀▄ █   █   █ █   █  █ █   █    █ ▐ ▄▀ ▀▄ 
  █▄▄▄█ ▐  █▀▀█▀  ▐   █  ▐ ▐  █    █    █▄▄▄█ 
 ▄▀   █  ▄▀    █      █       █   ▄▀   ▄▀   █ 
█   ▄▀  █     █    ▄▀▀▀▀▀▄     ▀▄▀    █   ▄▀  
▐   ▐   ▐     ▐   █       █           ▐   ▐   
                  ▐       ▐                   

By Telegram @Alparsl4n & @AtahanArslan 
"""
    print(Fore.CYAN + Style.BRIGHT + banner)
    print(Fore.RED + Style.BRIGHT + "Lütfen telegramda verdiğimiz giriş kodunu girin")
    print()

# Banner'ı yazdır
print_login_banner()
# Giriş kontrolü: Giriş kodu 'ariva' olmalıdır. Doğru kod girilince önce Telegram kanalına yönlendirilir.
def login():
    print_login_banner()
    user_code = getpass(Fore.YELLOW + "Giriş Kodunu Giriniz: " + Fore.RESET)
    if user_code.strip().lower() != "ariva":
        print(Fore.RED + "Hatalı giriş kodu! Erişim reddedildi.")
        sys.exit(1)
    else:
        print(Fore.GREEN + "Giriş başarılı. Hoşgeldiniz!")
        # Telegram kanalına yönlendir (kanal linkini aşağıdaki URL ile değiştirin)
        telegram_channel = "https://t.me/siberdunyanizz"
        print(Fore.LIGHTMAGENTA_EX + f"Telegram kanalına yönlendiriliyorsunuz: {telegram_channel}")
        webbrowser.open(telegram_channel)
        # Kullanıcının devam etmesi için kısa bir bekleme
        os.system('pause' if os.name == 'nt' else 'read -n1 -s -r -p "Devam etmek için enter tuşuna basınn..."')
        os.system('cls' if os.name == 'nt' else 'clear')

# Orijinal ASCII art başlıkları (Bajrangi & Aditya)
def print_title():
    bajrangi_ascii = """
 ██╗███╗   ██╗███████╗████████╗ █████╗ 
 ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗
 ██║██╔██╗ ██║███████╗   ██║   ███████║
 ██║██║╚██╗██║╚════██║   ██║   ██╔══██║
 ██║██║ ╚████║███████║   ██║   ██║  ██║
 ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
                                             """
    
    aditya_ascii = """
 ________  ______    ______   __         ______  
/        |/      \  /      \ /  |       /      \ 
$$$$$$$$//$$$$$$  |/$$$$$$  |$$ |      /$$$$$$  |
   $$ |  $$ |  $$ |$$ |  $$ |$$ |      $$ \__$$/ 
   $$ |  $$ |  $$ |$$ |  $$ |$$ |      $$      \ 
   $$ |  $$ |  $$ |$$ |  $$ |$$ |       $$$$$$  |
   $$ |  $$ \__$$ |$$ \__$$ |$$ |_____ /  \__$$ |
   $$ |  $$    $$/ $$    $$/ $$       |$$    $$/ 
   $$/    $$$$$$/   $$$$$$/  $$$$$$$$/  $$$$$$/
                                                         
"""
    print(Fore.RED + Style.BRIGHT + bajrangi_ascii)  # Bajrangi in bright red
    print(Fore.GREEN + aditya_ascii)  # Aditya in bold green

# Function to handle the original script functionality and display response in colored format
def run_script():
    os.system('cls||clear')
    
    # Print Bajrangi and Aditya titles
    print_title()

    h = ['61', '48', '52', '30', '63', '48', '4D', '36', '4C', '79', '39', '70', '4C', '6D', '6C', '75', '63', '33', '52', 
         '68', '5A', '33', '4A', '68', '62', '53', '35', '6A', '62', '32', '30', '76', '59', '58', '42', '70', '4C', '33', 
         '59', '78', '4C', '33', '56', '7A', '5A', '58', '4A', '7A', '4C', '32', '78', '76', '62', '32', '74', '31', '63', 
         '43', '38', '3D']
    hxafsnewas = ''.join(h)
    def indaknwcq(x):
        return x
    def skdnvwvds(s):
        return ''.join([indaknwcq(char) for char in s if char != ' '])
    hxafsnewas_no_spaces = skdnvwvds(hxafsnewas)
    knunqwsi = 2
    cuyewhw = [hxafsnewas_no_spaces[i:i + knunqwsi] for i in range(0, len(hxafsnewas_no_spaces), knunqwsi)]
    reversed_cuyewhw = [chunk[::-1][::-1] for chunk in cuyewhw]
    hxafsnewas_reassembled = ''.join(reversed_cuyewhw)
    ivmkrewom = ''.join([char if i % 2 == 0 else char for i, char in enumerate(hxafsnewas_reassembled)])
    def uwnrevj(uhevwcnje):
        return ba.unhexlify(indaknwcq(uhevwcnje))
    bytwbsdwd = uwnrevj(ivmkrewom)
    def uenfwjdsw(bytwbsdwd):
        def verwvwvfdq(data):
            return indaknwcq(data.decode('utf-8'))
        return verwvwvfdq(bytwbsdwd)
    uwevnewoiikw = uenfwjdsw(bytwbsdwd)
    def ubkfhjb(x):
        return x
    def uvwervnjwds(s):
        def step1(data):
            return indaknwcq(data)
        def step2(data):
            return ubkfhjb(data)
        def step3(data):
            return step2(step1(data))
        return b64.b64decode(step3(s)).decode('utf-8')
    uwnrkwnvsdfin = uvwervnjwds(uwevnewoiikw)

    # Getting username input
    username = input(Fore.RED + "Hedefİnsta: " + Fore.WHITE + "@")
    
    # Making the API request
    headers = {
        'accept-language': 'en-US;q=1.0',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'user-agent': 'Instagram 337.0.3.23.54 (iPhone12,1; iOS 16_6; en_US; en; scale=2.00; 828x1792; 577210397) AppleWebKit/420+',
    }

    data = {
        "q": username,
    }

    try:
        response = requests.post(uwnrkwnvsdfin, headers=headers, data=data)
        response.raise_for_status()
        os.system('cls||clear')

        response_json = response.json()

        # Displaying response with colored output
        print(Fore.MAGENTA + Style.BRIGHT + "Yanıt Detayları:")
        print(Fore.CYAN + "Çoklu Kullanıcı Bulundu: " + Fore.YELLOW + str(response_json.get('multiple_users_found', 'N/A')))
        print(Fore.CYAN + "E-Posta Gönderildi: " + Fore.YELLOW + str(response_json.get('email_sent', 'N/A')))
        print(Fore.CYAN + "SMS Gönderildi: " + Fore.YELLOW + str(response_json.get('sms_sent', 'N/A')))
        print(Fore.CYAN + "WA Gönderildi: " + Fore.YELLOW + str(response_json.get('wa_sent', 'N/A')))
        print(Fore.CYAN + "Arama Kaynağı: " + Fore.YELLOW + response_json.get('lookup_source', 'N/A'))
        print(Fore.CYAN + "Düzeltilmiş Giriş: " + Fore.YELLOW + response_json.get('corrected_input', 'N/A'))
        print(Fore.CYAN + "Doğrulama Adımlarında UHL Girişi Göster: " + Fore.YELLOW + str(response_json.get('show_uhl_entry_in_verification_steps', 'N/A')))
        print(Fore.CYAN + "UHL Girişi Uygun CPS: " + Fore.YELLOW + str(response_json.get('uhl_entry_eligible_cps', 'N/A')))
        print(Fore.CYAN + "Gizlenmiş Telefon: " + Fore.YELLOW + response_json.get('obfuscated_phone', 'N/A'))

        user = response_json.get('user', {})
        print(Fore.GREEN + "Kullanıcı Bilgileri:")
        print(Fore.GREEN + "  Tam Adı: " + Fore.LIGHTBLUE_EX + user.get('full_name', 'N/A'))
        print(Fore.GREEN + "  Kullanıcı Adı: " + Fore.LIGHTBLUE_EX + user.get('username', 'N/A'))
        print(Fore.GREEN + "  Profil Resmi URL: " + Fore.LIGHTBLUE_EX + user.get('profile_pic_url', 'N/A'))
        print(Fore.GREEN + "  Doğrulanmış: " + Fore.LIGHTBLUE_EX + str(user.get('is_verified', 'N/A')))

        print(Fore.LIGHTCYAN_EX + "Geçerli Telefon Var: " + Fore.LIGHTYELLOW_EX + str(response_json.get('has_valid_phone', 'N/A')))
        print(Fore.LIGHTCYAN_EX + "E-Posta ile Sıfırlama Yapılabilir: " + Fore.LIGHTYELLOW_EX + str(response_json.get('can_email_reset', 'N/A')))
        print(Fore.LIGHTCYAN_EX + "SMS ile Sıfırlama Yapılabilir: " + Fore.LIGHTYELLOW_EX + str(response_json.get('can_sms_reset', 'N/A')))
        print(Fore.LIGHTCYAN_EX + "WA ile Sıfırlama Yapılabilir: " + Fore.LIGHTYELLOW_EX + str(response_json.get('can_wa_reset', 'N/A')))
        print(Fore.LIGHTCYAN_EX + "WA Zamanlama Sinyali: " + Fore.LIGHTYELLOW_EX + str(response_json.get('is_wa_timing_signal', 'N/A')))
        print(Fore.LIGHTCYAN_EX + "WA Hesap Kurtarma Türü: " + Fore.LIGHTYELLOW_EX + response_json.get('wa_account_recovery_type', 'N/A'))
        print(Fore.LIGHTCYAN_EX + "Telefon Numarası: " + Fore.LIGHTYELLOW_EX + response_json.get('phone_number', 'N/A'))
        print(Fore.LIGHTCYAN_EX + "E-Posta: " + Fore.LIGHTYELLOW_EX + str(response_json.get('email', 'N/A')))

    except requests.RequestException as e:
        print(Fore.RED + f"Bir hata oluştu: {e}")

def main():
    # Giriş ekranı ve doğrulama
    login()
    # Asıl script çalışması
    run_script()

if __name__ == "__main__":
    main()

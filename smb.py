from configparser import ConfigParser

if __name__ == "__main__":
    smb = ConfigParser(interpolation=None)
    smb.read("/etc/samba/smb.conf")

    for section in smb.sections():
        print('[' + section + ']')
        print(smb.items(section))
        print("\n")


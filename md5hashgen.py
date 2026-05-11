#!/usr/bin/env python3

import hashlib

def main():
    print("\n🔐 Uteast MD5 Hash Encrypter\n")

    try:
        password = input(">> Enter your password (eg: Kpp): ").strip()

        if not password:
            print("\n❌ Password cannot be empty\n")
            return

        md5_hash = hashlib.md5(password.encode()).hexdigest()

        print("\n==============================")
        print(f"Password: {password}")
        print(f"MD5 Hash: {md5_hash}")
        print("==============================\n")

    except KeyboardInterrupt:
        print("\n\n👋 Exiting...\n")

if __name__ == "__main__":
    main()
import os

class Datalog:
    def write(line):
        file = open('backup.log','a')
        text = f"{line}"
        file.write(text +"\n")
        file.close()

    def read():
        try:
            file = open('backup.log','r')
            file.read().rstrip()
            file.close()
            return file
        
        except FileNotFoundError as e: 
            print(f"File not found! {e}")

    def delete():
        try:
            os.remove('backup.log')
            return True

        except FileNotFoundError as e:
            print(f"File not found! {e}")
            return False

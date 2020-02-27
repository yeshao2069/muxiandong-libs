import ftplib
import json
import os
import time


global config

def load_json(file_name):
    with open(file_name,"r") as f:
        data = json.load(f)
    return data

def build_android_package():
    global config
    c = config["work"]

    print(" clean cmd\n");
    os.system("clear")
    print("===================================================")
    print(" update git...")
    os.chdir(c["path"])
    os.system("git pull")
    print("===================================================")
    print(" modify egretproperties-json file begin...\n")
    cpd1 = config["android-egret-json"]
    cptarget1 = cpd1["target-path"]
    cptemp1 = cpd1["bak-path"]
    os.system("\cp "+cptemp1+" "+cptarget1)
    print(" modify egretproperties-json file done.\n")
    print("===================================================")
    print(" rebuild android projct, generate js code and resources\n")
    print(" wait a few seconds...")
    os.system("egret publish " + c["path"])
    print(" rebuild done.")
    print("===================================================")
    print(" build android package...\n")
    print(" modify default-thm-json file begin...\n")
    cpd2 = config["android-json"]
    cptarget2 = cpd2["target-path"]
    cptemp2 = cpd2["bak-path"]
    os.system("\cp "+cptemp2+" "+cptarget2)
    print(" modify default-thm-json file done.\n")

    andr = config["android"]
    os.chdir(andr["path"])
    print(" gradle clean...\n")
    os.system("gradle clean")
    print(" gradle build...\n")
    os.system("gradle build")
    print(" gradle generate release apk...\n")
    os.system("gradle assembleRelease")
    return andr["path"] + "/app/build/outputs/apk/app-release.apk"

def upload_file_to_ftp(local_file_path,remote_path,remote_file_name):
    print("===================================================")
    global config
    c = config["ftp"]
    ftp = ftplib.FTP(c["url"])
    ftp.login(c["account"], c["password"])
    ftp.cwd(remote_path)
    with open(local_file_path,"rb") as fd:
    	ftp.storbinary("STOR "+remote_file_name,fd)
    ftp.close()

def init_evn():
    global config
    c = config["tools"]
    os.chdir(c["path"])
    print("initalize env profile")
    os.system("source env.profile")
    print("add gradle operator permission...\n")
    os.system("chmod +x /Applications/Android\ Studio.app/Contents/gradle/gradle-4.6/bin/gradle")

if __name__ == "__main__":
    global config
    os.chdir("/Users/xindonghai/workspace/damai/tools")
    config = load_json("config.json")

    init_evn()

    file_name = time.strftime("damai-%Y-%m-%d-%H-%M-%S-android.apk",time.localtime(time.time()))
    remote_path = "client-package/damai"
    apk_full_path = build_android_package()
    print("===================================================")
    print(" new generate apk route is:" + apk_full_path)
    upload_file_to_ftp(apk_full_path,remote_path,file_name)
    print("done!!!!!!")
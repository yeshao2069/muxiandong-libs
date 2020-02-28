import ftplib
import json
import os
import time


global config

def load_json(file_name):
    with open(file_name,"r") as f:
        data = json.load(f)
    return data

def build_ios_package():
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
    cpd1 = config["ios-egret-json"]
    cptarget1 = cpd1["target-path"]
    cptemp1 = cpd1["bak-path"]
    os.system("\cp "+cptemp1+" "+cptarget1)
    print(" modify egretproperties-json file done.\n")
    print("===================================================")
    print(" rebuild ios projct, generate js code and resources\n")
    print(" wait a few seconds...")
    os.system("egret publish " + c["path"])
    print(" rebuild done.")
    print("===================================================")
    print(" build ios package...\n")
    print(" modify default-thm-json file begin...\n")
    cpd2 = config["ios-json"]
    cptarget2 = cpd2["target-path"]
    cptemp2 = cpd2["bak-path"]
    os.system("\cp "+cptemp2+" "+cptarget2)
    print(" modify default-thm-json file done.\n")

    c = config["ios"]
    os.chdir(c["path"])
    print(" clean project...\n")

    comm_pram =  " -project " + c["path"] + "/damai.xcodeproj" +  " -configuration Release " #" -target carrots-mobile" +

    cmd = "xcodebuild clean " + comm_pram + " -target damai-mobile"
    print(cmd)
    os.system(cmd)

    os.system("rm -rf ./archive.xcarchive")
    cmd = "xcodebuild archive " + comm_pram + " -scheme damai-mobile " + " -archivePath ./archive.xcarchive"
    print(cmd)
    os.system(cmd)

    os.system("rm -rf ./ipa/*")
    cmd = "xcodebuild -exportArchive -archivePath ./archive.xcarchive -exportOptionsPlist ./ExportOptions.plist -exportPath ./ipa"
    print(cmd)
    os.system(cmd)

    print("===================================================")
    print(" rename ios package...")
    file_name = time.strftime("damai-%Y-%m-%d-%H-%M-%S-ios.ipa",time.localtime(time.time()))
    os.rename(c["path"]+"/ipa/damai-mobile.ipa" , c["path"]+"/ipa/"+file_name)

    print(" rename ios done.")

    return file_name

def send_message_to_zen(title,desc):
    print("===================================================")
    print(" send meaasge to chan dao ")
    global config
    c = config["zen"]
    cli = zen.zentao_client(c["url"], c["account"], c["password"])
    cli.login()
    cli.add_todo(title,desc)

def upload_file_to_ftp(local_file_path,remote_path,remote_file_name):
    print("===================================================")
    print(" upload to ftp")
    global config
    c = config["ftp"]
    ftp = ftplib.FTP(c["url"])
    ftp.login(c["account"], c["password"])
    ftp.cwd(remote_path)
    with open(local_file_path,"rb") as fd:
    	ftp.storbinary("STOR "+remote_file_name,fd)
    ftp.close()

if __name__ == "__main__":
    global config

    # change current dir work route to tools
    os.chdir("/Users/xindonghai/workspace/damai/tools")

    config = load_json("config.json")
    # file_name = time.strftime("%Y-%m-%d-%H-%M-%S-ios.ipa",time.localtime(time.time()))
    remote_path = "client-package/damai"
    #process_js()
    file_name = build_ios_package()
    ipa_full_path = config["ios"]["path"] + "/ipa/" + file_name
    print("===================================================")
    print(" new generate ipa route is:" + ipa_full_path)

    upload_file_to_ftp(ipa_full_path,remote_path,file_name)
    print("\nbuild ios package done.")  
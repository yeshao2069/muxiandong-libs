import ftplib
import json
import os
import time
import sys
import hashlib 
import zipfile

global config
global version

excludes = [".DS_Store"]
def isFileFilter(filename):
    for name in excludes:
        if filename.endswith(name) or filename == name :
            return True
    return False

def getmd5(filename):  
    m = hashlib.md5()  
    mfile = open(filename, 'rb')
    m.update(mfile.read())
    mfile.close()
    md5value = m.hexdigest()  
    return md5value   

def load_json(file_name):
    with open(file_name,"r") as f:
        data = json.load(f)
    return data

def save_json(file_name,data):
    with open(file_name,"w") as f:
        json.dump(data,f,sort_keys = True)


def build_ios_update_package(path,os_path,desc_path,version_str,download_url,zip_name,os_type):
    print(path)
    print(desc_path)
    os.chdir(path)
    print("===================================================")
    print(" update git...\n")
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
    os.system("egret publish " + path)
    print(" rebuild done.")
    print("===================================================")
    print(" modify default-thm-json file begin...\n")
    cpd2 = config["ios-json"]
    cptarget2 = cpd2["target-path"]
    cptemp2 = cpd2["bak-path"]
    os.system("\cp "+cptemp2+" "+cptarget2)
    print(" modify default-thm-json file done.\n")
    print("===================================================")
    print(" change work directory to update folder...\n")
    isExitFolder = os.path.exists(desc_path)
    if not isExitFolder:
        os.system("mkdir -p "+desc_path)
    os.chdir(desc_path)
    os.system("rm -rf ./*")
    print(" copy resource from js and resource...\n")
    os.system("cp -r " + os_path + "/assets/game" + "/js ./")
    os.system("cp -r " + os_path + "/assets/game" + "/resource ./")
    print("===================================================")
    print(" create new filelist.json file...\n")
    create_filelist_json(download_url,version_str,os_type)
    print(" new filelist.json file create done.\n")
    print(" create new version.json file...\n")
    create_version_json(download_url,version_str,os_type)
    print(" new version.json file create done.\n")
    os.system("rm -rf ../" + zip_name)
    zip_file_path("./","../",zip_name)
    return desc_path + "/../" + zip_name

def build_android_update_package(path,os_path,desc_path,version_str,download_url,zip_name,os_type):
    print(path)
    print(desc_path)
    os.chdir(path)
    print("===================================================")
    print(" update git...\n")
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
    os.system("egret publish " + path)
    print(" rebuild done.")
    print("===================================================")
    print(" modify android-thm-json file begin...\n")
    cpd2 = config["android-json"]
    cptarget2 = cpd2["target-path"]
    cptemp2 = cpd2["bak-path"]
    os.system("\cp "+cptemp2+" "+cptarget2)
    print(" modify default-thm-json file done.\n")
    print("===================================================")
    print(" change work directory to update folder...\n")
    isExitFolder = os.path.exists(desc_path)
    if not isExitFolder:
        os.system("mkdir -p "+desc_path)
    os.chdir(desc_path)
    os.system("rm -rf ./*")
    print(" copy resource from js and resource...\n")
    os.system("cp -r " + os_path + "/assets/game" + "/js ./")
    os.system("cp -r " + os_path + "/assets/game" + "/resource ./")
    print("===================================================")
    print(" create new filelist.json file...\n")
    create_filelist_json(download_url,version_str,os_type)
    print(" new filelist.json file create done.\n")
    print(" create new version.json file...\n")
    create_version_json(download_url,version_str,os_type)
    print(" new version.json file create done.\n")
    os.system("rm -rf ../" + zip_name)
    zip_file_path("./","../",zip_name)
    return desc_path + "/../" + zip_name
    
def create_filelist_json(download_url,version_str,os_type):
    newList = {}
    newList["stage"] = []

    walk_dir("resource/",newList)
    walk_dir("js/",newList)
    fileinfo = open('filelist.json','w')
    buf ="{\n"
    buf +="\t\"version\" : \"" + version_str + "\",\n"
    buf +="\t\"engineVersion\" : \"5.2.15\",\n"
    buf +="\t\"type\" : \""+os_type+"\",\n"
    buf +="\t\"filelist\" : ["
    for i in range(0,len(newList["stage"])):
        file = newList["stage"][i]
        buf += "\n\t\t{\n\t\t\t\"name\":\""+file["name"]+"\",\n"
        buf += "\t\t\t\"md5\":\""+file["code"]+"\",\n"
        buf += "\t\t\t\"size\":\""+str(file["size"])+"\"\n"
        if i<len(newList["stage"])-1:
            buf += "\t\t},"
        else:
            buf += "\t\t}"
    buf += "\n\t],\n"
    buf +="\n\t\"searchPaths\" : [\n"
    buf +="\t]\n"
    buf = buf + "}"

    fileinfo.write(buf)
    fileinfo.close()

def create_version_json(download_url,version_str,os_type):
    fileinfo = open('version.json','w')
    buf ="{\n"
    buf += "\t\"filelist_url\" : \"http://"+download_url+"/"+os_type+"/filelist.json\",\n"
    buf += "\t\"base_url\" : \"http://"+download_url+"/"+os_type+"/\",\n"
    buf +="\t\"version\" : \""+version_str+"\",\n"
    buf +="\t\"type\" : \""+os_type+"\",\n"
    buf +="\t\"engineVersion\" : \"5.2.15\"\n"
    buf = buf + "}"

    fileinfo.write(buf)
    fileinfo.close()

def walk_dir(dir,newList):
    for root, dirs, files in os.walk(dir):
        for name in files:
            path = os.path.join(root,name)
            newPath = path#path.replace(gamePath,"")
            if not isFileFilter(newPath):
                detail = {}
                detail["name"] = newPath
                detail["code"] = getmd5(path)
                detail["size"] = os.path.getsize(path)
                newList["stage"].append(detail)
    return newList

def zip_file_path(input_path, output_path, output_name):
    f = zipfile.ZipFile(output_path + '/' + output_name, 'w', zipfile.ZIP_DEFLATED)
    filelists = []
    get_zip_file(input_path, filelists)
    for file in filelists:
        f.write(file)
    f.close()
    return output_path + r"/" + output_name

def get_zip_file(input_path, result):
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path + "/" + file):
            get_zip_file(input_path + "/" + file, result)
        else:
            result.append(input_path + "/" + file)

def upload_file_to_ftp(local_file_path,remote_path,remote_file_name):
    print("===================================================")
    print(" update to ftp"+local_file_path+"...\n")
    global config
    c = config["ftp"]
    ftp = ftplib.FTP(c["url"])
    ftp.login(c["account"], c["password"])
    ftp.cwd(remote_path)
    with open(local_file_path,"rb") as fd:
    	ftp.storbinary("STOR "+remote_file_name,fd)
    ftp.close()

if __name__ == "__main__":
    global config,version

    os.chdir("/Users/xindonghai/workspace/damai/tools")

    config = load_json("config.json")
    version = load_json("update_version.json")

    version_str = str(version["v1"]) + "." + str(version["v2"]) + "." + str(version["v3"])
    download_url = config["update"]["download_url"]
    print("version: " + version_str + " download_url: " + download_url)

    ios_path = config["ios"]["path"]
    android_path = config["android"]["path"]
    update_path = config["update"]["path"]
    work_path = config["work"]["path"]
    print("===================================================")
    print(" build update package...\n")
    ios_zip = build_ios_update_package(work_path,ios_path,update_path+"/ios",version_str,download_url,"ios.zip","ios")
    android_zip = build_android_update_package(work_path,android_path,update_path+"/android",version_str,download_url,"android.zip","android")
    print(ios_zip)
    print(android_zip)
    ios_file_name = time.strftime("damai-ios-%Y-%m-%d-%H-%M-%S-HotUpdate.zip",time.localtime(time.time()))
    android_file_name = time.strftime("damai-android-%Y-%m-%d-%H-%M-%S-HotUpdate.zip",time.localtime(time.time()))
    remote_path = "client-package/damai/update"

    upload_file_to_ftp(ios_zip,remote_path,ios_file_name)
    upload_file_to_ftp(android_zip,remote_path,android_file_name)
    os.chdir(config["tools"]["path"])
    version["v3"] = version["v3"] + 1
    save_json("update_version.json",version)
    print("===================================================")
    print("done!!!!!!")
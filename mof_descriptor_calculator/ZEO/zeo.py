import os
import pandas as pd

def run_zeo(cif_file, zeo_path):
    
    cif_name = cif_file.split("/")[-1][:-4]
    cwd = os.getcwd()
    cif_specific_path = cwd + "/data/" + cif_name +"/geo_pro"
    cif_file_location = cwd + "/cifs/" + cif_file
    os.makedirs(cif_specific_path, exist_ok= True)
    
    commands = [
        f"{zeo_path} -ha -sa 1.86 1.86 2000 {cif_specific_path}/ASA.txt {cif_file_location}",
        f"{zeo_path} -ha -vol 1.86 1.86 50000 {cif_specific_path}/AVA.txt {cif_file_location}",
        f"{zeo_path} -ha -res {cif_specific_path}/PD.txt {cif_file_location}",
        f"{zeo_path} -ha -volpo 1.86 1.86 2000 {cif_specific_path}/POV.txt {cif_file_location}"]

    for command in commands:
        os.system(command)
        
    data = {}
    with open(f"{cif_specific_path}/ASA.txt", "r") as f:
        lines = f.readlines()
        data["UC_volume"] = float(lines[0].strip().split("Unitcell_volume: ")[1].split()[0])
        data["Density"] = float(lines[0].strip().split("Density: ")[1].split()[0])
        data["ASA"] = float(lines[0].strip().split("ASA_A^2: ")[1].split()[0])
        data["vASA"] = float(lines[0].strip().split("ASA_m^2/cm^3: ")[1].split()[0])
        data["gASA"] = float(lines[0].strip().split("ASA_m^2/g: ")[1].split()[0])
        data["NASA"] = float(lines[0].strip().split("NASA_A^2: ")[1].split()[0])
        data["vNASA"] = float(lines[0].strip().split("NASA_m^2/cm^3: ")[1].split()[0])
        data["gNASA"] = float(lines[0].strip().split("NASA_m^2/g: ")[1].split()[0])
        print(lines[0])
        
    with open(f"{cif_specific_path}/AVA.txt", "r") as f:
        lines = f.readlines()
        data["AVA"] = float(lines[0].strip().split("AV_A^3: ")[1].split()[0])
        data["AVAf"] = float(lines[0].strip().split("AV_Volume_fraction: ")[1].split()[0])
        data["AVAg"] = float(lines[0].strip().split("AV_cm^3/g: ")[1].split()[0])
        data["NAVA"] = float(lines[0].strip().split("NAV_A^3: ")[1].split()[0])
        data["NAVAf"] = float(lines[0].strip().split("NAV_Volume_fraction: ")[1].split()[0])
        data["NAVAg"] = float(lines[0].strip().split("NAV_cm^3/g: ")[1].split()[0])
        print(lines[0])
    
    with open(f"{cif_specific_path}/PD.txt", "r") as f:
        lines = f.readlines()
        data["Di"] = float(lines[0].strip().split()[1])
        data["Df"] = float(lines[0].strip().split()[2])
        data["Dif"] = float(lines[0].strip().split()[3])
    
    with open(f"{cif_specific_path}/POV.txt", "r") as f:
        lines = f.readlines()
        print(lines[0])
        data["POAVA"] = float(lines[0].strip().split("POAV_A^3: ")[1].split()[0])
        data["POAVAf"] = float(lines[0].strip().split("POAV_Volume_fraction: ")[1].split()[0])
        data["POAVAg"] = float(lines[0].strip().split("POAV_cm^3/g: ")[1].split()[0])
        data["NPOAVA"] = float(lines[0].strip().split("PONAV_A^3: ")[1].split()[0])
        data["NPOAVAf"] = float(lines[0].strip().split("PONAV_Volume_fraction: ")[1].split()[0])
        data["NPOAVAg"] = float(lines[0].strip().split("PONAV_cm^3/g: ")[1].split()[0])

    data = pd.DataFrame(data, index = [0])
    data.to_csv(f"{cif_specific_path}/data.csv")
    
    return f"{cif_specific_path}/data.csv"


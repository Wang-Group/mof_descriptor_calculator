import os
from os import listdir
from os.path import isfile, join
import pandas as pd
from pymatgen.io.cif import CifParser
from molSimplify.Informatics.MOF.MOF_descriptors import get_MOF_descriptors
import argparse
import subprocess

def get_primitive(datapath, writepath):
    s = CifParser(datapath, occupancy_tolerance=1).get_structures()[0]
    sprim = s.get_primitive_structure()
    sprim.to(writepath,"cif")

def calculate_RAC(cif_file):

    cif_name = cif_file.split("/")[-1][:-4]
    cif_specific_path = "./data/" + cif_name
    
    os.makedirs(cif_specific_path, exist_ok= True)

    featurization_list = []
    
    get_primitive(datapath=f"./cifs/{cif_file}",
                  writepath= cif_specific_path + "/" + cif_file)
    
    full_names, full_descriptors = get_MOF_descriptors(data= cif_specific_path+ "/" + cif_file,
                                                       depth=3, 
                                                       path=cif_specific_path,
                                                       xyzpath=cif_specific_path + "/xyz/" + cif_file.replace('.cif','.xyz')
                                                       )
    
    full_names.append('filename')
    full_descriptors.append(cif_file)
    featurization = dict(zip(full_names, full_descriptors))
    featurization_list.append(featurization)

    df = pd.DataFrame(featurization_list)
    df.to_csv(cif_specific_path + "/" + cif_file.replace('.cif','.csv'))
    return df
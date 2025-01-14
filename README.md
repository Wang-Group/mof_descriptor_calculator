# mof_descriptor_calculator

### Requirements
Ensure you have the following dependencies installed before running the code:
```code
Python 3.8+
pandas
numpy
scikit-learn
matplotlib
seaborn
```
Install the dependencies using pip.

[Zeo++-0.3](https://www.zeoplusplus.org/download.html)

## Installation
To use the code in this repository, clone the repository and install the necessary dependencies listed in the [Requirements](#requirements) section.
Then install the package offered by this repo:

```code
git clone <repository-url>
cd mof_descriptor_calculator
pip install -e . 
```

## Usage
One example is at [example.ipynb](./example.ipynb).

```code
# import all the necessary packages
import mof_descriptor_calculator as mof_d
import pandas as pd
import os

# find the paths of the cifs 
cifs = [i for i in os.listdir("./cifs_14MOFs/") if i.endswith("cif")]

# the working path for zeo
zeo_path = "../zeo++-0.3/network" # path to the zeo++-0.3 package

# test the 
failed = []
for cif_file in cifs:
    try:
        mof_d.RAC.calculate_RAC(cif_file = cif_file)
        test = mof_d.ZEO.run_zeo(cif_file = cif_file, zeo_path= zeo_path)
    except:
        failed.append(cif_file)
        continue

```

## Contributions and Support
Feel free to contribute by opening issues or submitting pull requests.

## License
This project is licensed under the MIT License.
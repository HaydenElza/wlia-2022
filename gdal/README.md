# README

## Set up environment

After cloning the repository you will need to set up your python environment. You need to first install [miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/individual).

Open Anaconda Prompt and change to the abi_xml_munging directory within the cloned repository and create the environment from file:
```bash
cd gdal
conda env create --file environment.yml
```

Activate the environment using:
```bash
conda activate wlia2022_env
```
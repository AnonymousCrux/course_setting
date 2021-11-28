# course_setting

## Setup jupyter-lab with miniconda

Install miniconda from https://docs.conda.io/en/latest/miniconda.html.

Then execute

```shell
conda env create -f environment.yml
conda activate sh2021-python
```

Start jupyter lab:

```shell
jupyter-lab
```

## Dashboard

Start the dasboard with:

```shell
streamlit run dashboard/dashboard.py
```

## Data

### Folder `Data`

Cleaned up dataset.

### Folder `Runs Computed`

`<date>_<athlete>_<run>.csv`


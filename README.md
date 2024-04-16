# README

## Description of CSV Files

This repository contains three CSV files that are used as parameters for the `main.py` program. Below is a detailed description of each file:

### matrix_d.csv

Each line of this file represents an option. Each column represents the parameters of this option in relation to the criteria. The values are separated by commas.

### weights.csv

Each line of this file contains the importance of each parameter to the user, expressed in percentage, and whether this parameter is of the type "the more, the better" (1) or "the less, the better" (0). The values are separated by commas.

### options.csv

This file contains the name of each of the options. These names will be used to plot the options on the final chart.

## How to Use

1. Make sure the CSV files are in the same directory as the `main.py` file.
2. Run the `main.py` file.
3. The program will use the data from the CSV files to calculate and plot a chart with the options.

## Example of Use

```bash
python main.py
```
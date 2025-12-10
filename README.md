# **pnct-api-scraper**

This repository was developed as part of the Integrative Project I of the Civil Engineering course at the Federal University of Santa Catarina (UFSC). This repository contains two Python scripts for collecting traffic volume data from highways using the National Traffic Counting Program (PNCT) API from DNIT. The collected data corresponds to hourly and quarter-hourly traffic volume for specified counting stations.

## Script Structure

The scripts are organized as follows:

- **api_volumeHora.py**: Retrieves hourly traffic volume data.
- **api_volumeQuartoHora.py**: Retrieves quarter-hourly traffic volume data.

Each script makes requests to the PNCT API, storing the retrieved data in CSV files organized by counting stations and date.

## Requirements

Before running the scripts, ensure that Python is installed along with the following packages:

```bash
pip install requests pandas
```

## Usage

1. **Configure the storage path**
   - In `api_volumeHora.py`, adjust the `caminho` (path) variable to the directory where you want to save the collected data.
   - In `api_volumeQuartoHora.py`, make the same adjustment in the `caminho` (path) variable.

2. **Run the desired script**

   To collect hourly traffic volume data:
   
   ```bash
   python api_volumeHora.py
   ```

   To collect quarter-hourly traffic volume data:
   
   ```bash
   python api_volumeQuartoHora.py
   ```

The data will be saved in CSV files organized into folders named according to the counting stations.

## CSV File Structure

The CSV files contain the following columns:

- **idEquipamento** (equipment ID): Identifier of the counting equipment.
- **sentido** (direction): Traffic flow direction.
- **ano** (year), **mes** (month), **dia** (day), **hora** (hour): Date and time of the count.
- **valorVH** (hourly volume) (only in `api_volumeHora.py`): Hourly traffic volume.

## Notes

- The script automatically handles the existence of folders and files.
- If no data is available for a given day, a message will be displayed in the console.
- The current timestamp is added to the API URL to prevent request caching.

## Author

João Vitor Ferreira Pedro
[Civil Engineer - UFSC]
[https://github.com/jvfpedro] [jvfpedro@gmail.com]

Daniel Tavares dos Anjos
[collaborator]
[https://github.com/danieltanjos]



# CriminalIP_FindDorks

This project provides a set of Python scripts to query asset information related to DICOM, Elasticsearch, ADB, and FTP using the Criminal IP Banner Search API.

## Description

The program uses the Criminal IP Banner Search API to search for assets with specific attributes such as IP, Port, Product, and Title related to DICOM, Elasticsearch, ADB, and FTP.

Relevant API documentation: [Criminal IP Banner Search API](https://www.criminalip.io/en/developer/api/get-banner-search)

## Prerequisites

- **Criminal IP API Key**: You need to sign up at [criminalip.io](https://criminalip.io) and obtain an API key.

## Installation and Setup

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/criminalIP_FindDorks.git
    ```

2. Navigate to the project directory:
    ```bash
    cd criminalIP_FindDorks
    ```

3. Open each script file (`criminalip_Dimco.py`, `criminalip_Elasticserach.py`, `criminalip_ADB.py`, `criminalip_FTP.py`) and insert your Criminal IP API Key into the `x-api-key` variable.

4. If you wish to add additional Criminal IP search queries, modify the `base_url` and query parameters within the script files accordingly.

## Usage

To start the scripts, execute them individually as follows:
```bash
python criminalip_Dimco.py
python criminalip_Elasticserach.py
python criminalip_ADB.py
python criminalip_FTP.py
```

## Screenshots
When the scripts are executed, you will receive output similar to the following: 
[DIMCO](DIMCO.png)
[Elasticsearch](Elasticsearch.png)
[ADB](ADB.png)
[FTP](FTP.png)
   
## Additional Information 
For detailed information on how to use the Criminal IP Open API, please refer to the [Criminal IP Open API Documentation](https://www.criminalip.io/en/developer/api/get-banner-search).

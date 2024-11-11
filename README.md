# Script for Downloading 2021 TIGER/Line® Shapefiles: Roads
This Python script uses Selenium to automate the process of downloading shapefiles from the U.S. Census Bureau website for specific counties in the given state. It selects a state, iterates over its counties, and downloads the relevant shapefile for each county.

<br>

## Requirements
To run this script, you need the following installed on your machine:
- Python 3.x
- Google Chrome
- ChromeDriver (compatible with your Chrome version)
- Selenium (python library)

<br>

## Setup Instructions
### 1. Install Python and Pip:
Ensure `Python 3.x` is installed on your system. You can download it from [python.org](https://www.python.org/).

### 2. Install Selenium:
Open your command line interface (CLI) and run the following command:
```shell
PS C:\Users\userxxx> pip install selenium
```
Refer [documentation](https://selenium-python.readthedocs.io/installation.html) in case of issues during installation. 

### 3. Download and Install ChromeDriver:
- Download ChromeDriver from [here](https://developer.chrome.com/docs/chromedriver/downloads). Make sure it matches the version of your installed Google Chrome browser.
- Extract the downloaded file and place the `chromedriver.exe` file in a directory.

### 4. Update the Script with Your Paths:
- Modify `driver_path` in the script to point to your chromedriver.exe location.
- Modify `downloadFilepath` to the desired download directory on your machine.

<br>

## How to Run

### 1. Open the Script:
Copy the provided script into a Python file, i.e, `scraping_tiger_shapefile.py`.

### 2. Run the Script:
- Open a terminal or command prompt.
- Navigate to the directory containing the script.
- Execute the script using:
```shell 
PS C:\Users\userxxx\directory-of-script> python scraping_tiger_shapefile.py
```

### 3. Monitor the Execution:
The script will open a Chrome browser window, navigate to the Census Bureau website, and start downloading shapefiles for counties in the specified state. It will iterate through each county and print the currently selected county on the console.

### 4. Completion:
After downloading files for all counties, the browser will close automatically, and the script will print the total number of downloads. <br> 

$${\color{red}Please \space verify \space the \space total \space number \space of \space counties \space downloaded \space to \space the \space actual \space number. \space Site \space response \space time \space may \space affect \space the \space downloads.}$$

<br>


## Note
* You may need to adjust the sleep times in the script based on your internet speed and the site’s response time to ensure all files download correctly.
* Ensure that Pop-ups are enabled in Chrome for the website used in the script.


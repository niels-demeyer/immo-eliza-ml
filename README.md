# Belgium Real Estate Dataset 🏡

## Description 📝

This project aims to make a price prediction model using machine learning.

## Table of Contents

- [Installation ⚙️](#installation-⚙️)
- [Usage 🚀](#usage-🚀)
- [Sources 📚](#sources-📚)

## Installation ⚙️

**Prerequisites**

Ensure you have Git and Python installed on your system. Some commands in the manual may differ depending on the operating system and terminal used.

**Clone the repository using `git` command:**

    git clone git@github.com:niels-demeyer/immo-eliza-ml.git

**Navigate to the root of the repository using `cd` command**:

    cd immo-eliza-ml

**Install the required packages using `pip` command:**

    pip3 install -r requirements.txt

## Usage 🚀

**Update URLs to fetch the newest information:**

    cd scrapy/immoweb/immoweb
    scrapy crawl most_expensive -o output.json

It can take some time.

**Navigate back to the root of repository:**

    cd ../../..

**Navigate to the hrequests folder\*\***

    cd hrequests

**Open the [main.py](hrequests/main.py) using code editor and change these values:**

![How to setup hrequests](img/how_to_setup_hrequests.png)

by default it scrapes 500 urls, you can change it by changing the value of the `end` variable.

by default it saves the result to the my_database.sqlite file in the first_500 table, you can change it by changing the value of the `table_name` variable.

**After changing the values, run the main.py file using the following command:**

    python3 main.py

It will start scraping the data from the urls and save it to the database. It can take some time, so be patient.

Your data will be saved in the `my_database.sqlite` file.

## Sources 📚

Data for this project was sourced from:

- [Immoweb](https://www.immoweb.be/): The primary source of data used in this project. Immoweb is Belgium's leading real estate website, providing listings for properties for sale and rent.

# GBIF-Geographical-Coordinates-Scraper

A simple program I made to scrape the coordinates of particular species from the [Global Biodiversity Information Facility(abbreviated gbif)](https://www.gbif.org/). The species could be found in the `sources.xlsx` Excel file.
When this program is executed, an Excel file called `scraped-results.xlsx` is created, which contains the species in the extracted from the `source.xlsx` plus their Geographical coordinates (latitude and longitude) in Cameroon.

I made use of [pygbif](https://pygbif.readthedocs.io/en/latest/index.html) python library to easily fetch the needed data from gbif.
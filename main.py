import pygbif as gbif
import pandas as pd
from openpyxl import Workbook

wb = Workbook()
worksheet = wb.active
worksheet.title = "Results Sheet"

# open the source Excel file and retrieve the content of the species column
df = pd.read_excel("source.xlsx")
species_col = df["Species"]

for index, i in enumerate(species_col):
    # the first and third items of the species column have some strange Unicode issues -
    # the line below is kind of a hack
    i = 'Acridocarpus staudtii (Engl.) Engl. ex Hutch. & Dalziel' if index == 0 else 'Adenocarpus mannii (Hook.f.) Hook.f.' if index == 2 else i
    specie = gbif.species.name_backbone(name=i)

    specie_coordinates = []
    if specie:
        try:
            # search for occurrences (with coordinates, and in Cameroon)
            o = gbif.occurrences.search(scientificName=specie["scientificName"], hasCoordinate=True, country="CM")
        except KeyError:
            print(f"Error: {i} -------------- {specie}")
        else:
            # grab the search results (a dictionary of all matching occurrences)
            search_results = o["results"]
            for j in search_results:
                scientific_name = j['scientificName']
                if i in scientific_name:
                    # get the latitude and longitude of this particular occurrence
                    lon, lat = j['decimalLongitude'], j['decimalLatitude']
                    if (lat, lon) in specie_coordinates or (round(lat, 1), round(lon, 1)) in specie_coordinates:
                        continue
                    else:
                        # round to two decimal places and store it
                        lat, lon = round(lat, 1), round(lon, 1)
                        specie_coordinates.append((lat, lon))

    # add a row to the worksheet with well formatted coordinates
    worksheet.append([i, *[f"{x[0]}N, {x[1]}E" for x in specie_coordinates]])

# save the workbook
wb.save("scraped-results.xlsx")

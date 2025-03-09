import pandas as pd

class XJ_97_99:
    country_origin = {"1": "United States"}
    make = {"J": "Jeep"}
    vehicle_type = {"4": "MPV"}
    gross_weight_rating = {"F": "4000-5000 lbs"}
    vehicle_line = {
        "F": "4x4 - Left Hand Drive",
        "J": "4x4 - Right Hand Drive",
        "N": "4x4 - Right Hand Drive",
        "B": "2WD - Left Hand Drive",
        "T": "2WD - Right Hand Drive",
        }
    series = {
        "2": "SE",
        "6": "Sport",
        "7": "Country",
    }
    body_style = {
        "7": "2-Door",
        "8": "4-Door"
    }
    engine = {
        "P": "2.5L 4 Cyl",
        "S": "4.0L 6 Cyl"
    }
    check_digit = "skip"
    model_year = {
        "V": "1997",
        "W": "1998",
        "X": "1999",
    }
    assembly_plant = "skip"
class XJ_00_01:
    country_origin = {"1": "United States"}
    make = {"J": "Jeep"}
    vehicle_type = {"4": "MPV"}
    gross_weight_rating = {"F": "4000-5000 lbs"}
    vehicle_line = {
        "F": "4x4 - Left Hand Drive",
        "J": "4x4 - Right Hand Drive",
        "N": "4x4 - Right Hand Drive",
        "B": "2WD - Left Hand Drive",
        "T": "2WD - Right Hand Drive",
        }
    series = {
        "N": "5 speed manual",
        "A": "3 speed auto",
        "B": "4 speed auto",
        "4": "Sport",
        "6": "Country/Limited",
        "5": "Classic",
    }
    body_style = {
        "7": "2-Door",
        "8": "4-Door"
    }
    engine = {
        "M": "2.5L 4 Cyl [Diesel]",
        "P": "2.5L 4 Cyl [Gas]",
        "S": "4.0L 6 Cyl",
    }
    check_digit = "skip"
    model_year = {
        "Y": "2000",
        "Z": "2001",
        "1": "2001",
    }
    assembly_plant = "skip"
xj97_99 = {
    1: XJ_97_99.country_origin,
    2: XJ_97_99.make,
    3: XJ_97_99.vehicle_type,
    4: XJ_97_99.gross_weight_rating,
    5: XJ_97_99.vehicle_line,
    6: XJ_97_99.series,
    7: XJ_97_99.body_style,
    8: XJ_97_99.engine,
    9: XJ_97_99.check_digit,
    10: XJ_97_99.model_year,
    11: XJ_97_99.assembly_plant
    }
xj00_01 = {
    1: XJ_00_01.country_origin,
    2: XJ_00_01.make,
    3: XJ_00_01.vehicle_type,
    4: XJ_00_01.gross_weight_rating,
    5: XJ_00_01.vehicle_line,
    6: XJ_00_01.series,
    7: XJ_00_01.body_style,
    8: XJ_00_01.engine,
    9: XJ_00_01.check_digit,
    10: XJ_00_01.model_year,
    11: XJ_00_01.assembly_plant
    }

def XJ_Decoder(identifier: str) -> dict:
    global xj00_01
    global xj97_99
    
    if identifier in ["V", "W", "X"]:
        return xj97_99
    elif identifier in ["Y", "Z", "1"]:
        return xj00_01

def DisplaySpecs(vehicle_specs: list, vin: str) -> None:
    print(vin)
    for spec in vehicle_specs:
        print(spec)
    print("-"*30, end="\n\n")

vin_list = pd.read_csv("vin_list.csv", header=None)

for index, row in vin_list.iterrows():
    vehicle_info = []
    vin = row.to_string(header=False, index=False)
    vin_decoder = XJ_Decoder(str(vin[9]))
    for index, position in enumerate(vin):
        index += 1
        if index > 11:
            break
        elif index < 4:
            continue
        elif isinstance(vin_decoder[index], str):
            continue
        vehicle_info.insert(0, vin_decoder[index][position])
        
    DisplaySpecs(vehicle_info, vin)
        
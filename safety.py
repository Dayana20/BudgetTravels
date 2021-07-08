def start(country_name):
    fileName = "safety.csv"
    country_info = {}
    with open(fileName,"r") as file:
        # "country","lifeQualityRank","lifeQualityIndex","safetyIndex","healthcareIndex","pollutionIndex","climateIndex"
    #     for country, qRank, qIndex, safetyIndex, healthcareIndex, pollutionIndex, climateIndex in file:
    #         print("country", country)
        for line in file: 
            line = line.replace('"','')
            line = line.replace('\n','').split(',')
            country_info[line[0]] = line[1:]

    print(country_info[country_name])

def main():
    country_name = input("What country? (Full Name Please) ")
    start(country_name)
    
main()


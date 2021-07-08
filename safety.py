def start(country_name):
    fileName = "safety2.csv"
    country_info = {}
    with open(fileName,"r") as file:
        for line in file: 
            line = line.split()
            country_info[line[1]] = {"Safety Rank": line[0],"Safety Index Score":line[2]}

    for key, value in country_info[country_name].items():
        print(key, " : ", value)

def main():
    country_name = input("What country? (Full Name Please) ")
    start(country_name)
    
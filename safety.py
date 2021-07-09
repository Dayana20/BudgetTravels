def start(country_name):
    fileName = "safety2.csv"
    country_info = {}
    with open(fileName,"r") as file:
        for line in file: 
            line = line.split()
            length = len(line)
            name = ' '.join(line[1:length-1])
            country_info[name] = {"Safety Rank": line[0],"Safety Index Score":line[-1]}

    for key, value in country_info[country_name].items():
        print(key, " : ", value)
    

def main():
    country_name = input("What country? (Full Name Please) ")
    start(country_name)
    

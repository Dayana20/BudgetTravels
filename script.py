from weather import *
from holidays import *
from safety import *
from translate import Translator #sudo pip3 install translate

def print_header(title):
    print(f'\n{title}')
    print('-' * len(title))
    
def menu():
    print_header('Menu')
    toPrint= """
    1) Weather
    2) Holidays
    3) Safety
    0) Exit/Try Another Option
    """
    print(toPrint)


def handle_option(option):
    try:
        return int(option)
    except:
        return -1

def weather(lat, lon, location, city_name):
    API_key = 'ea395ebe708b1af005b17243cbc20ac9'
    dic = set_up_w(lat,lon,API_key)
    info = create_dataframe_w(dic)
    dbName = 'weather'
    fileName = 'weather_file'
    tableName = 'weather_table'
    df, engine = update_w(dbName, fileName, tableName, info)
    write_table_w(dbName,engine, info)
    save_data_w(dbName, fileName, engine,info)
    # visualiation (NEEDS IMPROVEMENT)
    df.plot.bar(x='date', y='temp')
    plt.title(location.address)
    plt.savefig('weather_bar.png')
    
    
def holidays(country_name):
    # holiday main
    database = 'holidays'
    file = 'holiday_file'
    table = 'holiday_table'
    engine_h = create_engine('mysql://root:codio@localhost/' + database)
    api_key = get_api()
    url = build_url(country_name, api_key) # moved this up here
    dic = build_dict(url) # added this
    holiday_df = build_dataframe(dic) #added this
    df = update_database(database, table, file, engine_h)    
    write_table_h(df, database, table, engine_h)
    save_data_to_file(df, database, table, file, engine_h)
    
def safety(translator, destination_name):
    translation = translator.translate(destination_name)
    start(translation)
    
    
def main():
    language = input("Input Language format for city and country name: ")
    translator= Translator(from_lang=language,to_lang="english")
    # weather main
    destination_name = input("City and/or State/Country of Destination: ")
    lat, lon, location = get_data_w(destination_name)
    #holiday
    country_name = location.address.split(', ')[-1]
    # print(country_name)
    menu()
    option = handle_option(input('Enter your option: '))
    
    ##menu
    while(option!=0):
        if(option==1): #weather
            print_header("Weather for "+ location.address)
            weather(lat, lon, location, destination_name)
        elif(option==2):
            print_header("Holidays for "+ location.address)
            holidays(country_name)
        elif(option==3):
            print_header("Safety for "+ location.address)
            safety(translator, country_name)
        else:
            print('\nInvalid choice, select another option')
            
        menu()
        option = handle_option(input('Enter your option: '))
        
    print("Bye")
    
    
main()
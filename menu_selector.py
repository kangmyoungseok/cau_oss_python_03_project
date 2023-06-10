import file_manager
from parking_spot_manager import str_list_to_class_list, print_spots
from parking_spot_manager import filter_by_name, filter_by_district, filter_by_city, filter_by_location, filter_by_ptype
from parking_spot_manager import sort_by_keyword

def start_process(path):
    str_list = file_manager.read_file(path)
    spots = str_list_to_class_list(str_list)

    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            print_spots(spots)
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                spots = filter_by_name(spots,keyword)
                print_spots(spots)
            elif select == 2:
                keyword = input('type city:')
                spots = filter_by_city(spots,keyword)
                print_spots(spots)
            elif select == 3:
                keyword = input('type district:')
                spots = filter_by_district(spots,keyword)
                print_spots(spots)
            elif select == 4:
                keyword = input('type ptype:')
                spots = filter_by_ptype(spots,keyword)
                print_spots(spots)
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                spots = filter_by_location(spots,(min_lat,max_lat,min_lon,max_lon))
                print_spots(spots)
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                spots = sort_by_keyword(spots,keyword)               
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            break
        else:
            print("invalid input")
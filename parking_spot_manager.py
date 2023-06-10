class parking_spot:
    """
    하나의 주차장 정보를 저장하는 클래스

    Attributes:
        name (str): 주차장 이름
        city (str): 주차장이 위치한 시
        district (str): 주차장이 위치한 구
        ptype (str): 주차장 유형
        longitude (float): 경도
        latitude (float): 위도

    methods:
        get(keyword): keyword에 해당하는 정보를 반환
    """

    # 생성자
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = {}
        self.__item['name'] = name
        self.__item['city'] = city
        self.__item['district'] = district
        self.__item['ptype'] = ptype
        self.__item['longitude'] = float(longitude)
        self.__item['latitude'] = float(latitude)

    def get(self, keyword='name') -> dict:
        return self.__item[keyword]


    def __str__(self) -> str:
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
def str_list_to_class_list(str_list: list) -> list:
    """
    문자열 리스트로 저장된 주차장 정보를 클래스 리스트로 변환

    Args:
        str_list (list): 문자열 리스트

    Returns:
        list: 클래스 리스트
    """
    class_list = []
    for item in str_list:
        # 1. 아이템 파싱(delimiter : ',')
        seq,name,city,district,ptype,longitude,latitude = item.split(',')
        # 2. 파싱 정보로 클래스 생성
        new_item = parking_spot(name,city,district,ptype,longitude,latitude)
        # 3. class_list에 추가
        class_list.append(new_item)

    return class_list

def print_spots(spots: list) -> None:
    """
    주차장 정보를 출력

    Args:
        spots (list): 주차장 정보가 저장된 클래스 리스트
    """
    print(f"---print elements({len(spots)})---")
    for item in spots:
        print(item)


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)
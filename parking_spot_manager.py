"""
    parking_spot 클래스와 관련된 함수들을 정의한 모듈

    parking_spot 클래스는 주차장 정보를 저장하는 클래스

    parking_spot 클래스의 인스턴스에 저장되는 정보
        name (str): 주차장 이름
        city (str): 주차장 위치(시도)
        district (str): 주차장 위치(시군구)
        ptype (str): 주차장 유형
        longitude (float): 경도
        latitude (float): 위도

    그 외에 parking_spot 클래스와 관련된 함수들을 정의    
"""

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


def filter_by_name(spots: list, name: str) -> list:
    """
    주차장 정보중 해당하는 이름(name)을 가진 추자장들만 새로운 리스트로 반환

    Args:
        spots (list): 주차장 정보가 저장된 클래스 리스트
        name (str): 이름
    
    Returns:
        list: 클래스 리스트
    """
    filtered_list = [item for item in spots if name in item.get('name')]
    return filtered_list

def filter_by_city(spots: list, city: str) -> list:
    """
    주차장 정보중 해당 도시(시도)에 해당하는 추자장들만 새로운 리스트로 반환

    Args:
        spots (list): 주차장 정보가 저장된 클래스 리스트
        city (str): 시도
    
    Returns:
        list: 클래스 리스트
    """
    filtered_list = [item for item in spots if city in item.get('city')]
    return filtered_list

def filter_by_district(spots: list, district: str) -> list:
    """
    주차장 정보중 해당 도시(시군구)에 해당하는 추자장들만 새로운 리스트로 반환

    Args:
        spots (list): 주차장 정보가 저장된 클래스 리스트
        district (str): 시군구
    
    Returns:
        list: 클래스 리스트
    """
    filtered_list = [item for item in spots if district in item.get('district')]
    return filtered_list

def filter_by_ptype(spots: list, ptype: str) -> list:
    """
    주차장 정보중 해당하는 주차장 유형 가진 추자장들만 새로운 리스트로 반환

    Args:
        spots (list): 주차장 정보가 저장된 클래스 리스트
        ptype (str): 주차장 유형
    
    Returns:
        list: 클래스 리스트
    """
    filtered_list = [item for item in spots if ptype in item.get('ptype')]
    return filtered_list

def filter_by_location(spots: list, locations: tuple) -> list:
    """
    주차장 정보중 주어진 위도,경도 범위 내의 추자장들만 새로운 리스트로 반환

    Args:
        spots (list): 주차장 정보가 저장된 클래스 리스트
        locations (tuple): (min_lat, max_lat, min_long, max_long)
    
    Returns:
        list: 클래스 리스트
    """
    filtered_list = [item for item in spots if \
                      locations[0] < item.get('latitude') < locations[1] and \
                      locations[2] < item.get('longitude') < locations[3]] 
    return filtered_list

def sort_by_keyword(spots: list, keyword: str) -> list:
    """
    주차장 정보를 해당하는 키워드로 정렬하여 새로운 리스트로 반환

    Args:
        spots (list): 주차장 정보가 저장된 클래스 리스트
        keyword (str): 정렬할 기준 컬럼
    
    Returns:
        list: 클래스 리스트
    """
    sorted_list = sorted(spots, key=lambda x: x.get(keyword))
    return sorted_list


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # str_list = file_manager.read_file("./input/free_parking_spot.csv")
    # spots = str_list_to_class_list(str_list)
    # spots = filter_by_district(spots, '동작')
    # spots = filter_by_name(spots,'대학교')
    # spots = filter_by_city(spots, '인천')
    #spots = filter_by_location(spots, (35.5,36.5,127.5,128.5))
    #print_spots(spots)
    
    # version#4
    spots = sort_by_keyword(spots, 'latitude')
    print_spots(spots)
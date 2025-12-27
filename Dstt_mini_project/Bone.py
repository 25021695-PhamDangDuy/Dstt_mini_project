import math
temp_arr = {
    "1" : {
        "Name" : "Phạm Đăng Duy",
        "Điểm CC" : 10,
        "Điểm GK" : 9,
        "Điểm CK" : 8,
        "Điểm TB" : 8.5
    },
    "2" :{
        "Name" : "Trần Lê Trung Dũng",
        "Điểm CC" : 9,
        "Điểm GK" : 10,
        "Điểm CK" : 7.6,
        "Điểm TB" : 8
    },
    "3" :{
        "Name" : "Ngô Đình Dũng",
        "Điểm CC" : 8,
        "Điểm GK" : 10,
        "Điểm CK" : 9,
        "Điểm TB" : 9
    }
}

def get_info_student(arr : dict, key : str) -> list:
    """
    Hàm này giúp lấy thông tin từ kho dữ liệu(data base) và trích xuất ra một list mới
    Ví dụ: get_info_student(data_base, key = "Name") là lấy tất cả các Name từ data_base ra
    """
    #ValuesList
    Studentlist = list(arr.values())
    #GenerList
    ID = list(arr.keys())
    Name_list = []
    CC = []
    GK = []
    CK = []
    TB = []

    #Add items into GenerList
    for dct in Studentlist:
        Name_list.append(dct["Name"])
        CC.append(dct["Điểm CC"])
        GK.append(dct["Điểm GK"])
        CK.append(dct["Điểm CK"])
        TB.append(dct["Điểm TB"])
    
    #Process KeyValue
    if key == "ID":
        return ID
    elif key == "Name":
        return Name_list
    elif key == "CC":
        return CC
    elif key == "GK":
        return GK
    elif key == "CK":
        return CK
    elif key == "TB":
        return TB
    elif key == "All":
        return ID,Name_list, CC, GK, CK, TB
    else:
        print("KeyValue Error!")
    


def show_diem(a):
    pass

print(get_info_student(temp_arr, key = "All"))


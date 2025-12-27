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



def show_grade(arr : dict, key):
    if key == "All":
        print("=================================================================")
        print(f"{"Mã sv":<8}{"Họ và Tên":<30}{"Điểm CC":<10}{"Điểm GK":<10}{"Điểm CK":<10}{"Điểm TB":<10}")
        print("-----------------------------------------------------------------")
        for key, value in arr.items():
            print(f"{key:<8}{value["Name"]:<30}{value["Điểm CC"]:<10}{value["Điểm GK"]:<10}{value["Điểm CK"]:<10}{value["Điểm TB"]:<10}")
    else:
        is_CC = False
        is_GK = False
        is_CK = False
        is_TB = False
        for x in key:
            is_CC = True if ( x == "1") else is_CC
            is_GK = True if ( x == "2") else is_GK
            is_CK = True if ( x == "3") else is_CK
            is_TB = True if ( x == "4") else is_TB
        print(f"{"Mã sv":<8}{"Họ và Tên":<30}" + (f"{"Điểm CC":<10}" if is_CC else "") + (f"{"Điểm GK":<10}" if is_GK else "") + (f"{"Điểm CK":<10}" if is_CK else "") + (f"{"Điểm TB":<10}" if is_TB else ""))
        for key, value in arr.items():
            print(f"{key:<8}{value["Name"]:<30}" + (f"{value["Điểm CC"]:<10}" if is_CC else "") + (f"{value["Điểm GK"]:<10}" if is_GK else "") + (f"{value["Điểm CK"]:<10}" if is_CK else "") + (f"{value["Điểm TB"]:<10}" if is_TB else ""))
show_grade(temp_arr, "24")









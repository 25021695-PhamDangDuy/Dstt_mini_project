import math
import os

#StorageSetting
ID_stg = {}
"""
Info_student_stg(temp) = {"name" : XYZ, "Điểm CC" : 00, "Điểm GK" : 00, "Điểm CK" : 00, "Điểm TK" : average()}
"""
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
#Def Function Settings
#Backing track
def back_tracking(arr : dict, funcDef ,startValue : int, endValue = 4):
    running = True
    while running:
        n = 0
        if n == 0:
            funcDef(arr)
            print("1. Quay lại                  2.Dừng chương trình")
            n = int(input("Bạn muốn: "))
        if n == 1:
           n = 0
        elif n == 2:
            print("Xác nhận dừng chương trình(y/n):")
            xac_nhan = input("Xác nhận: ")
            if xac_nhan == "y" :
                startValue = endValue
                running = False
            elif xac_nhan == "n":
                print("Hủy!")
                n = 0
        else:
            print("Lỗi tham số!")
        return startValue
        
        

#Show infor def
def Show_infor(arr ):
    """
    Hàm này xử lí input nhập vào là những gì user mong muốn + database -> Hiển thị lên terminal những gì user cần 
    """
    #GUIsettings

    GUI = """
    ==============[Danh Sách Sinh Viên]=============
        1.Xem từng phần                     2.Xem tất cả
        3.Quay lại
    ================================================
    """


    GUI_1 = f"""
    ===============[Chi tiết các phần có thể xem]===============
    1. Mã sinh viên                             2. Họ và tên
    3. Điểm thành phần                          4. Quay lại
    """
    GUI_1_3 = f"""
    =====================[Thành phần các điểm]======================
    1. Điểm chuyên cần                            2. Điểm giữa kì
    3. Điểm cuối kì                               4. Điểm trung bình
    5. Quay lại
    """


    GUI_2 = f"""
    ==============[Thông tin sinh viên]=============
    """

    #Main
    # User Inpurt
    print(GUI)
    n = int(input("Hãy chọn chế độ xem: "))
    #Process
    if n == 1:
        print(GUI_1)
        print("Nhập các số bạn muốn xem vào(ví dụ: 12 hoặc 123)")
        print(GUI_1_3)
        print("Nhập các số bạn muốn xem vào(ví dụ: 12 hoặc 1234)")


    elif n == 2:
        print(GUI_2)
    elif n == 3:
        print("Đang quay về!")
        main()
        


#Modify infor student
def modify_infor(arr):
    """
    Hàm này xử lí input là mảng nhập vào và cho output là thay đổi items trong mảng đó theo mong muốn của user
    """
    #GUIsettings
    GUI = """
    ===================[Chỉnh sửa thông tin]==================
        1.  Thêm sinh viên                 2. Xóa thông tin sv
        3.  Sửa thông tin sv
    ==========================================================
    """
    GUI_1 = """
    ===================[Thêm sinh viên]==================
        
    =====================================================
    """
    GUI_2 = """
    ===================[Xóa thông tin sv]====================
        
    ==========================================================
    """
    GUI_3 = """
    ===================[Chỉnh sửa thông tin sv]==================
        
    =============================================================
    """

    #Process
    print(GUI)
    n = int(input("Chọn phần chỉnh sửa bạn muốn: "))

    
#Searching infor
def searching(arr):
    """
    Hàm này giúp tìm kiếm thông tin sinh viên cần thiết
    """



def main():
    #GUI settings
    basemain = f"""
        |=================================={"{Quản Lí Sinh Viên}"}==================================|
            1. Xem danh sách                                  3. Chỉnh sửa thông tin sinh viên
            2. Tìm kiếm sinh viên                             4. Dừng
        |=======================================================================================|
        """
    #Process
    running = True
    n = 0
    while running:
        if n == 0:
            print(basemain)
            n = int(input("Nhập số tương ứng với yêu cầu mà bạn muốn: "))

        if n == 1:
            n = back_tracking(temp_arr,Show_infor,n, endValue = 4)
        elif n == 2:
            n = back_tracking(temp_arr,searching,n,endValue= 4)
        elif n == 3:
            n = back_tracking(temp_arr,modify_infor,n,endValue= 4)
        elif n == 4:
            print("Thoát chương trình!")
            running = False



main()
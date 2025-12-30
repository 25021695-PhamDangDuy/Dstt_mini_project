
temp_arr = {
    "1" : {
        "Họ và Tên" : "Phạm Đăng Duy",
        "Điểm CC" : 10,
        "Điểm GK" : 9,
        "Điểm CK" : 8,
        "Điểm TB" : 8.5
    },
    "2" :{
        "Họ và Tên" : "Trần Lê Trung Dũng",
        "Điểm CC" : 9,
        "Điểm GK" : 10,
        "Điểm CK" : 7.6,
        "Điểm TB" : 8
    },
    "3" :{
        "Họ và Tên" : "Ngô Đình Dũng",
        "Điểm CC" : 8,
        "Điểm GK" : 10,
        "Điểm CK" : 9,
        "Điểm TB" : 9
    }
} 
def show_grade(arr : dict, key):
    if key == "All":
        print("=================================================================")
        print(f"{"Mã sv":<8}{"Họ và Tên":<30}{"Điểm CC":<10}{"Điểm GK":<10}{"Điểm CK":<10}{"Điểm TB":<10}")
        print("-----------------------------------------------------------------")
        for key, value in arr.items():
            print(f"{key:<8}{value["Họ và Tên"]:<30}{value["Điểm CC"]:<10}{value["Điểm GK"]:<10}{value["Điểm CK"]:<10}{value["Điểm TB"]:<10}")
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
            print(f"{key:<8}{value["Họ và Tên"]:<30}" + (f"{value["Điểm CC"]:<10}" if is_CC else "") + (f"{value["Điểm GK"]:<10}" if is_GK else "") + (f"{value["Điểm CK"]:<10}" if is_CK else "") + (f"{value["Điểm TB"]:<10}" if is_TB else ""))

def tinh_diem_tong_ket(CC, GK, CK):
    return CC * 0.1 + GK * 0.3 + CK * 0.6

def Add_infor():
    temp_sv = {'ID': '', 'NAME': '', 'CC': 0, 'GK': 0, 'CK': 0}
    buoc = 0

    print("\n--- Nhập thông tin (Gõ 'back' hoặc '<' để quay lại) ---")

    while buoc < 5:
        try:
            # ==== ID =====
            if buoc == 0:
                raw = input(">> Nhập ID (hoặc 'exit'): ").strip()
                if raw.lower() == 'exit':
                    return False
                if raw.lower() in ['back', '<']:
                    return False

                if raw in temp_arr:
                    print(f"   [!] ID '{raw}' đã tồn tại. Chế độ: CẬP NHẬT.")

                temp_sv['ID'] = raw
                buoc += 1

            # ===== TÊN =====
            elif buoc == 1:
                print(f"   --- Nhập liệu cho ID: {temp_sv['ID']} ---")
                raw = input("   >> Tên SV: ")
                if raw.lower() in ['back', '<']:
                    buoc -= 1
                    continue
                temp_sv['NAME'] = raw
                buoc += 1

            # ===== ĐIỂM CHUYÊN CẦN =====
            elif buoc == 2:
                raw = input("   >> Điểm Chuyên cần: ")
                if raw.lower() in ['back', '<']:
                    buoc -= 1
                    continue
                val = float(raw)
                if 0 <= val <= 10:
                    temp_sv['CC'] = val
                    buoc += 1
                else:
                    print("   [!] Điểm từ 0-10.")

            # ===== ĐIỂM GIỮA KỲ =====
            elif buoc == 3:
                raw = input("   >> Điểm Giữa kỳ: ")
                if raw.lower() in ['back', '<']:
                    buoc -= 1
                    continue
                val = float(raw)
                if 0 <= val <= 10:
                    temp_sv['GK'] = val
                    buoc += 1
                else:
                    print("   [!] Điểm từ 0-10.")

            # ===== ĐIỂM CUỐI KỲ =====
            elif buoc == 4:
                raw = input("   >> Điểm Cuối kỳ: ")
                if raw.lower() in ['back', '<']:
                    buoc -= 1
                    continue
                val = float(raw)
                if 0 <= val <= 10:
                    temp_sv['CK'] = val
                    buoc += 1
                else:
                    print("   [!] Điểm từ 0-10.")

        except ValueError:
            print("   [!] Lỗi: Vui lòng nhập số.")

    # ===== LƯU DỮ LIỆU  =====
    TB = tinh_diem_tong_ket(temp_sv['CC'], temp_sv['GK'], temp_sv['CK'])

    temp_arr[temp_sv['ID']] = {
        "Họ và Tên": temp_sv['NAME'],
        "Điểm CC": temp_sv['CC'],
        "Điểm GK": temp_sv['GK'],
        "Điểm CK": temp_sv['CK'],
        "Điểm TB": TB
    }

    print(f"   -> Đã LƯU: {temp_sv['NAME']} (TB: {TB:.2f})")

def delete_infor():
    id_xoa = input("Nhập ID cần xóa: ")
    if id_xoa in temp_arr:
        del temp_arr[id_xoa]
        print("-> Đã xóa.")
    else:
        print("Không tìm thấy!")

def modify_infor(m=None):
    import os
    if m==None:
        print("Nhập '<' hoặc '0' để quay lại.")
        m=input('Nhập ID cần chỉnh sửa:')
    if m=='<' or m=='0':
        return False # ở đây return lại chương trình trước đó, có thể dùng os để xóa màn hình
    while m not in temp_arr:
        os.system('cls')
        print("Nhập '<' hoặc '0' để quay lại.")
        m=input('ID không tồn tại,vui lòng nhập lại:')
        if m=='<' or m=='0':
            return False # ở đây return lại chương trình trước đó, có thể dùng os để xóa màn hình
    else:
        os.system('cls')
        Name_ban_đầu={temp_arr[m]["Họ và Tên"]}
        Điểm_CC_ban_đầu={temp_arr[m]["Điểm CC"]}
        Điểm_GK_ban_đầu= {temp_arr[m]["Điểm GK"]}
        Điểm_CK_ban_đầu= {temp_arr[m]["Điểm CK"]}
        Điểm_TB_ban_đầu={temp_arr[m]["Điểm TB"]}
        Xác_nhận=False
        while Xác_nhận==False:
            ten=input(f"""
Nhập '<' hoặc '_esc_' để quay lại.
=======================================             
                      
          THÔNG TIN HỌC SINH                                     
Họ và Tên: {Name_ban_đầu}                                
Điểm CC : {Điểm_CC_ban_đầu}                         
Điểm GK : {Điểm_GK_ban_đầu}                        
Điểm CK : {Điểm_CK_ban_đầu}                         
Điểm TB : {Điểm_TB_ban_đầu}                                          
======================================= 
=======================================
            CHỈNH SỬA 
Họ và Tên:
Điểm CC:
Điểm GK:
Điểm CK:
Điểm TB:
=======================================
Nhập tên:                                            
""")
            if ten== '<' or ten=='_esc_':
                return False
            os.system('cls')
            điểm_cc=input(f"""      
=======================================
            CHỈNH SỬA
Họ và Tên:{ten}
Điểm CC:
Điểm GK:
Điểm CK:
Điểm TB:
=======================================
Nhập điểm CC:                                                   
""")
            if điểm_cc== '<' or điểm_cc=='_esc_':
                return False
            os.system('cls')
            điểm_gk=input(f""" 
=======================================
            CHỈNH SỬA 
Họ và Tên:{ten}
Điểm CC:{điểm_cc}
Điểm GK:
Điểm CK:
Điểm TB:
=======================================
Nhập điểm GK:                                            
""")
            if điểm_gk== '<' or điểm_gk=='_esc_':
                return False
            os.system('cls')
            điểm_ck=input(f""" 
=======================================
            CHỈNH SỬA 
Họ và Tên:{ten}
Điểm CC:{điểm_cc}
Điểm GK:{điểm_gk}
Điểm CK:
Điểm TB:
=======================================
Nhập điểm CK:                                            
""")
            if điểm_ck== '<' or điểm_ck=='_esc_':
                return False
            os.system('cls')
            xn=input(f""" 
=======================================
            CHỈNH SỬA 
Họ và Tên:{ten}
Điểm CC:{điểm_cc}
Điểm GK:{điểm_gk}
Điểm CK:{điểm_ck}
Điểm TB:{float(điểm_cc)*0.1+float(điểm_gk)*0.3+float(điểm_ck)*0.6}
=======================================
Xác nhận thay đổi ? (y/n)                                
""")
            if xn=='y':
                Xác_nhận=True
                print('Đã chỉnh sửa thông tin')
                temp_arr[m]={"Name": ten, "Điểm CC": điểm_cc, "Điểm GK": điểm_gk, "Điểm CK": điểm_ck, "Điểm TB": float(điểm_cc)*0.1+float(điểm_gk)*0.3+float(điểm_ck)*0.6}
            if xn=='n':
                xn_2=input("""
==============================
Chọn tác vụ:
1.Sửa lại
2.Quay vê
""")
                while xn_2!='1' and xn_2!='2':
                    os.system('cls')
                    print('Không hợp lệ')
                    xn_2=input("""
==============================
Chọn tác vụ:
1.Sửa lại
2.Quay vê
""")
                    if xn_2=='2':
                        return False
                    if xn_2=='1':
                        os.system('cls')




def main():
    n = 0 
    while True:
        if n == 0:
            n = int(input("Nhập số tương ứng với yêu cầu mà bạn muốn: "))
        if n == 1:
            show_grade(temp_arr, "All")
          
        elif n == 2:
            delete_infor()
        elif n == 3:
            Add_infor()
        elif n == 4:
            modify_infor()
        elif n == 5:
            return False
        n = 0
main()
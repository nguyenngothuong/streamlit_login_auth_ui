import streamlit as st
from streamlit_login_auth_ui.widgets import __login__

__login__obj = __login__(auth_token = "courier_auth_token",
                    company_name = "Shims",
                    width = 200, height = 250,
                    logout_button_name = 'Logout', hide_menu_bool = False,
                    hide_footer_bool = False,
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()
username = __login__obj.get_username()

if LOGGED_IN == True:
    # Tiêu đề của ứng dụng
    st.title("Danh sách thông tin học viên")
    hoc_vien = [
      {"ten": "Nguyễn Văn A", "sdt": "0123456789", "mon_hoc": "Toán", "khoa_hoc": "Khóa 1", "trang_thai": False},
      {"ten": "Trần Thị B", "sdt": "0987654321", "mon_hoc": "Lý", "khoa_hoc": "Khóa 2", "trang_thai": False},
      {"ten": "Lê Văn C", "sdt": "0909090909", "mon_hoc": "Hóa", "khoa_hoc": "Khóa 1", "trang_thai": False},
      {"ten": "Phạm Thị D", "sdt": "0888888888", "mon_hoc": "Văn", "khoa_hoc": "Khóa 3", "trang_thai": False},
      {"ten": "Hoàng Văn E", "sdt": "0777777777", "mon_hoc": "Toán", "khoa_hoc": "Khóa 2", "trang_thai": False},
      {"ten": "Vũ Thị F", "sdt": "0666666666", "mon_hoc": "Lý", "khoa_hoc": "Khóa 1", "trang_thai": False},
      {"ten": "Đặng Văn G", "sdt": "0555555555", "mon_hoc": "Hóa", "khoa_hoc": "Khóa 3", "trang_thai": False},
      {"ten": "Bùi Thị H", "sdt": "0444444444", "mon_hoc": "Văn", "khoa_hoc": "Khóa 2", "trang_thai": False},
      {"ten": "Lý Văn I", "sdt": "0333333333", "mon_hoc": "Toán", "khoa_hoc": "Khóa 3", "trang_thai": False},
      {"ten": "Trương Thị K", "sdt": "0222222222", "mon_hoc": "Lý", "khoa_hoc": "Khóa 1", "trang_thai": False},
      {"ten": "Ngô Văn L", "sdt": "0111111111", "mon_hoc": "Hóa", "khoa_hoc": "Khóa 2", "trang_thai": False},
      {"ten": "Hà Thị M", "sdt": "0999999999", "mon_hoc": "Văn", "khoa_hoc": "Khóa 1", "trang_thai": False},
      {"ten": "Dương Văn N", "sdt": "0888888888", "mon_hoc": "Toán", "khoa_hoc": "Khóa 2", "trang_thai": False},
      {"ten": "Tạ Thị O", "sdt": "0777777777", "mon_hoc": "Lý", "khoa_hoc": "Khóa 3", "trang_thai": False},
      {"ten": "Phan Văn P", "sdt": "0666666666", "mon_hoc": "Hóa", "khoa_hoc": "Khóa 1", "trang_thai": False},
      {"ten": "Đỗ Thị Q", "sdt": "0555555555", "mon_hoc": "Văn", "khoa_hoc": "Khóa 2", "trang_thai": False},
      {"ten": "Vương Văn R", "sdt": "0444444444", "mon_hoc": "Toán", "khoa_hoc": "Khóa 1", "trang_thai": False},
      {"ten": "Lâm Thị S", "sdt": "0333333333", "mon_hoc": "Lý", "khoa_hoc": "Khóa 3", "trang_thai": False},
      {"ten": "Trần Văn T", "sdt": "0222222222", "mon_hoc": "Hóa", "khoa_hoc": "Khóa 2", "trang_thai": False},
      {"ten": "Nguyễn Thị U", "sdt": "0111111111", "mon_hoc": "Văn", "khoa_hoc": "Khóa 1", "trang_thai": False}
   ]

      # Lấy danh sách khóa học
      
    khoa_hoc_list = list(set(hv['khoa_hoc'] for hv in hoc_vien))

    # Chọn khóa học
    selected_khoa_hoc = st.selectbox("Chọn khóa học", khoa_hoc_list)

    # Lấy danh sách môn học theo khóa học đã chọn
    mon_hoc_list = list(set(hv['mon_hoc'] for hv in hoc_vien if hv['khoa_hoc'] == selected_khoa_hoc))

    # Chọn môn học
    selected_mon_hoc = st.selectbox("Chọn môn học", mon_hoc_list)

    # Lọc danh sách học viên theo khóa học và môn học đã chọn
    filtered_hoc_vien = [hv for hv in hoc_vien if hv['khoa_hoc'] == selected_khoa_hoc and hv['mon_hoc'] == selected_mon_hoc]

    # Hiển thị thông tin học viên và checkbox để tích chọn trạng thái
    for i, hv in enumerate(filtered_hoc_vien):
        st.write(f"Tên: {hv['ten']}")
        st.write(f"Số điện thoại: {hv['sdt']}")
        hv['trang_thai'] = st.checkbox("Đã học", key=f"{selected_khoa_hoc}_{selected_mon_hoc}_{i}")
        st.write("---")

    # Nút xác nhận gửi đi
    if st.button("Xác nhận"):
        # In ra trạng thái học viên đã chọn
        for hv in filtered_hoc_vien:
            if hv['trang_thai']:
                st.write(f"Học viên {hv['ten']} đã học.")
            else:
                st.write(f"Học viên {hv['ten']} chưa học.")
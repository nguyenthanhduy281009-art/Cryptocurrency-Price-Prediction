import streamlit as st

st.set_page_config(page_title="Liên Quân Counter-Pick AI", page_icon="⚔️")
st.title("⚔️ AI Draft Pick: Khắc Chế & Tỷ Lệ Thắng")

# Dữ liệu mẫu (Bạn có thể tiếp tục thêm đầy đủ các tướng vào đây)
# Format: "Tên Tướng": [Khắc chế cùng đường, Khắc chế đường khác, Mẹo, Winrate]
data_lien_quan = {
    "Airi": [["Yena", "Richter", "Florentino"], ["Arum", "Aleister"], "Chờ Airi hết lướt mới tung chiêu khống chế.", "49.5%"],
    "Aleister": [["Zata", "Liliana", "Raz"], ["Ngộ Không", "Nakroth"], "Áp sát nhanh trước khi hắn kịp đặt ma trận.", "51.2%"],
    "Arum": [["Hayate", "Maloch", "Elsu"], ["Paine", "Kriknak"], "Giữ khoảng cách, cấu rỉa từ xa thay vì áp sát.", "52.0%"],
    "Elsu": [["Max", "Joker", "Violet"], ["Ngộ Không", "Quillen"], "Dùng các tướng áp sát nhanh hoặc lộ diện tàng hình.", "50.8%"],
    "Florentino": [["Omen", "Richter", "Yena"], ["Arum", "Aleister"], "Hạn chế solo 1vs1, ưu tiên khống chế cứng.", "53.4%"],
    "Grakk": [["Chaugnar", "Toro", "Maloch"], ["Hayate", "Violet"], "Đứng sau lính và dùng tướng có giải khống chế.", "48.9%"],
    "Hayate": [["Valhein", "Joker", "Elsu"], ["Zuka", "Ngộ Không"], "Dùng tướng có sát thương dồn nhanh (Burst Damage).", "51.5%"],
    "Nakroth": [["Zephys", "Wonder Woman"], ["Arum", "Aleister"], "Pick tướng chịu đòn tốt hoặc khống chế chỉ định.", "50.2%"],
    "Ngộ Không": [["Max", "Lindis", "Elsu"], ["Baldum", "Thane"], "Sử dụng các tướng có khả năng soi map/tàng hình.", "52.1%"],
    "Raz": [["Lauriel", "Liliana"], ["TeeMee", "Gildur"], "Tránh đứng thẳng hàng với cú đấm chân không.", "50.6%"],
    "Tulane": [["Liliana", "Zata"], ["Nakroth", "Kriknak"], "Lên trang bị kháng phép sớm để giảm sát thương.", "51.0%"],
    "Zill": [["Keera", "Lữ Bố"], ["Arum", "Aleister"], "Dùng tướng có khả năng không thể bị chọn làm mục tiêu.", "49.8%"],
    "Zuka": [["Omen", "Skud", "Maloch"], ["Arum", "Aleister"], "Đợi Zuka dồn hết combo rồi mới phản công.", "52.7%"],
}

# --- GIAO DIỆN ---
st.info("💡 Mẹo: Bạn chỉ cần gõ chữ cái đầu (ví dụ: 'Z'), app sẽ hiện ra Zuka, Zill...")

# Thanh tìm kiếm có gợi ý (selectbox tự động lọc khi gõ)
tuong_selected = st.selectbox(
    "Nhập tên tướng địch để phân tích:",
    options=[""] + sorted(list(data_lien_quan.keys())),
    format_func=lambda x: "Chọn tướng..." if x == "" else x
)

if tuong_selected:
    res = data_lien_quan[tuong_selected]
    
    # Hiển thị Tỷ lệ thắng của tướng địch
    st.subheader(f"📊 Phân tích: {tuong_selected}")
    st.write(f"**Tỷ lệ thắng hiện tại của {tuong_selected}:** `{res[3]}`")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**🛡️ Khắc chế cùng đường (Lane):**")
        for t in res[0]:
            st.write(f"- {t}")
            
    with col2:
        st.info("**🎯 Khắc chế từ vị trí khác:**")
        for t in res[1]:
            st.write(f"- {t}")
            
    st.warning(f"📝 **Mẹo đối đầu:** {res[2]}")
    
    # Gợi ý thêm tỷ lệ thắng nếu bạn pick khắc chế
    st.divider()
    st.caption(f"Nếu bạn chọn các tướng gợi ý trên, tỷ lệ thắng của Team có thể tăng thêm 5-10%.")

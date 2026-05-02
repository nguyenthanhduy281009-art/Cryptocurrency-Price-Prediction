import streamlit as st

st.set_page_config(page_title="Liên Quân Counter-Pick", page_icon="⚔️", layout="wide")

st.title("⚔️ Siêu Tool Khắc Chế Toàn Bộ  Vị Tướng")

# Dữ liệu 128 vị tướng (Duy có thể cập nhật thêm mẹo chi tiết cho từng con)
# Cấu trúc: "Tên": [Khắc chế cùng đường, Khắc chế đường khác, Mẹo, Winrate]
data_lq = {
    "Airi": [["Yena", "Richter"], ["Arum", "Aleister"], "Cẩn thận Airi lướt ảo diệu, dùng khống chế cứng.", "49.5%"],
    "Aleister": [["Zata", "Liliana"], ["Ngộ Không", "Nakroth"], "Áp sát nhanh trước khi hắn đặt ma trận.", "51.2%"],
    "Alice": [["TeeMee", "Chaugnar"], ["Zuka", "Paine"], "Lên giải khống chế để né choáng liên tục.", "50.1%"],
    "Allain": [["Omen", "Lu Bu"], ["Hayate", "Valhein"], "Đừng solo khi Allain đang tích đủ nội tại.", "51.3%"],
    "Amily": [["Omen", "Roxie"], ["Hayate", "Elsu"], "Amily solo 1vs1 cực mạnh, hãy đánh hội đồng.", "48.9%"],
    "Annette": [["Chaugnar", "Zipt"], ["Nakroth", "Kriknak"], "Tránh đứng tụ lại gần các cơn gió của cô ấy.", "49.6%"],
    "Aoi": [["Arum", "Aleister"], ["Hayate", "Valhein"], "Dùng khống chế khi Aoi đang đu dây.", "52.7%"],
    "Arthur": [["Maloch", "Hayate"], ["Slimz", "Elsu"], "Dùng sát thương chuẩn để xuyên lớp giáp dày.", "47.8%"],
    "Arum": [["Hayate", "Maloch"], ["Paine", "Zill"], "Giữ khoảng cách, đừng để Arum áp sát xích.", "52.1%"],
    "Astrid": [["Hayate", "Maloch"], ["Allain", "Tulen"], "Cẩn thận chiêu cuối miễn thương của Astrid.", "49.3%"],
    "Ata": [["Hayate", "Maloch"], ["D'Arcy", "Gildur"], "Lên trang bị giảm hồi máu để khắc chế nội tại.", "48.2%"],
    "Aya": [["Chaugnar", "TeeMee"], ["Wukong", "Quillen"], "Dùng sát thương dồn nhanh để hạ gục vật chủ.", "53.0%"],
    "Azzen'Ka": [["Liliana", "Tulen"], ["Nakroth", "Aoi"], "Né các vùng khống chế hất tung dưới chân.", "46.5%"],
    "Baldum": [["Chaugnar", "Hayate"], ["Elsu", "Slimz"], "Cẩn thận bị Baldum úp lồng trong giao tranh.", "50.4%"],
    "Batman": [["Lindis", "Max"], ["Baldum", "Thane"], "Dùng đồ phụ trợ soi tàng hình sớm.", "51.5%"],
    "Bijan": [["Omen", "Toro"], ["Hayate", "Aleister"], "Khống chế cứng để chặn xe của Bijan.", "52.2%"],
    "Bolt Baron": ["Dữ liệu đang cập nhật"],
    "Bright": [["Omen", "Arum"], ["Aleister", "Zata"], "Đợi Bright hết trạng thái bất tử rồi mới dồn dame.", "50.8%"],
    "Capheny": [["Joker", "Elsu"], ["Wukong", "Zuka"], "Dùng sát thương dồn nhanh trước khi cô ấy kịp bắn.", "51.1%"],
    "Chaugnar": [["Maloch", "Hayate"], ["Baldum", "Thane"], "Chaugnar hóa giải khống chế rất tốt, đừng dồn CC.", "48.7%"],
    "Charlotte": ["Dữ liệu đang cập nhật"],
    "Celica": [["D'Arcy", "Gildur"], ["Ngộ Không", "Paine"], "Áp sát nhanh khi cô ấy đang dựng pháo.", "49.9%"],
    "Cresht": [["Hayate", "Maloch"], ["Elsu", "Slimz"], "Đừng đánh khi Cresht đang ở dạng Thủy quái.", "49.1%"],
    "D'Arcy": [["Chaugnar", "Liliana"], ["Nakroth", "Aoi"], "Lên giải khống chế để thoát khỏi vòng lập phương.", "50.3%"],
    "Dextra": [["Omen", "Arum"], ["Aleister", "Hayate"], "Đừng đánh khi Dextra đang bật chiêu cuối hồi máu.", "48.6%"],
    "Dirak": [["Liliana", "Raz"], ["Nakroth", "Quillen"], "Áp sát từ phía sau hoặc hai bên sườn.", "51.4%"],
    "Dolia": ["Dữ liệu đang cập nhật"],
    "Dieu Thuyen": [["Chaugnar", "Liliana"], ["Nakroth", "Zuka"], "Lên giày kiên cường để giảm thời gian đóng băng.", "47.9%"],
    "Dyadia": ["Dữ liệu đang cập nhật"],
    "Elsu": [["Max", "Joker"], ["Ngộ Không", "Quillen"], "Dùng tướng áp sát nhanh hoặc tàng hình.", "52.5%"],
    "Enzo": [["Chaugnar", "Lữ Bố"], ["Arum", "Aleister"], "Tránh để Enzo móc trúng chiêu 2.", "49.2%"],
    "Eland'orr": [["Valhein", "Joker"], ["Zuka", "Ngộ Không"], "Khống chế cứng khi hắn biến về vị trí lồng đèn.", "50.7%"],
    "Fennik": [["Joker", "Elsu"], ["Nakroth", "Kriknak"], "Giữ khoảng cách tránh bị nổ dấu ấn chiêu 1.", "48.4%"],
    "Flowborn(pháp sư)": ["Dữ liệu đang cập nhật"],
    "Flowborn(xạ thủ)": ["Dữ liệu đang cập nhật"],
    "Florentino": [["Omen", "Richter"], ["Arum", "Aleister"], "Cấm hoặc dùng khống chế chỉ định.", "54.2%"],
    "Goverra": ["Dữ liệu đang cập nhật"],
    "Gildur": [["Chaugnar", "Liliana"], ["Nakroth", "Zuka"], "Lên giày kiên cường và né các cú bắn vàng.", "50.1%"],
    "Grakk": [["Chaugnar", "Toro"], ["Hayate", "Slimz"], "Đứng sau lính để tránh bị kéo.", "48.8%"],
    "Hayate": [["Valhein", "Joker"], ["Zuka", "Ngộ Không"], "Áp sát nhanh, đừng để hắn thả diều.", "51.6%"],
    "Helen": [["Max", "Mganga"], ["Tulen", "Liliana"], "Bắt buộc phải lên Sách/Đao truy hồn.", "52.9%"],
    "Heino":  ["Dữ liệu đang cập nhật"],
    "Ignis": [["Tulen", "Liliana"], ["Nakroth", "Quillen"], "Né các vùng lửa để không bị choáng liên tục.", "49.5%"],
    "Illumia": [["Liliana", "Tulen"], ["Ngộ Không", "Paine"], "Cẩn thận bị đẩy lùi và choáng từ xa.", "50.2%"],
    "Ishar": [["Liliana", "Raz"], ["Nakroth", "Kriknak"], "Hạ gục thú cưng Tí Nị trước khi bắt Ishar.", "48.7%"],
    "Jinna": [["Liliana", "Tulen"], ["Zuka", "Nakroth"], "Tránh đứng gần khi hắn bật chiêu cuối.", "50.4%"],
    "Kahlii": [["Liliana", "Tulen"], ["Nakroth", "Quillen"], "Né đường đạn từ chiêu cuối của cô ấy.", "49.8%"],
    "Keera": [["Zill", "Lữ Bố"], ["Arum", "Aleister"], "Cẩn thận bụi rậm, Keera dồn dame rất nhanh.", "51.7%"],
    "Kil'Groth": [["Omen", "Hayate"], ["Arum", "Aleister"], "Khống chế cứng khi hắn hết chiêu cuối.", "48.1%"],
    "Kriknak": [["Zephys", "Toro"], ["Arum", "Aleister"], "Lên đồ thủ sớm để tránh bị vồ bốc hơi.", "50.9%"],
    "Krixi": [["Liliana", "Raz"], ["Nakroth", "Quillen"], "Dùng tướng cơ động để né Bướm ảo.", "51.0%"],
    "Krizzix": [["Lindis", "Max"], ["Thane", "Baldum"], "Dùng đồ soi tàng hình để chặn hắn kéo.", "49.4%"],
    "Lauriel": [["Aleister", "Arum"], ["Hayate", "Valhein"], "Đừng giao tranh lâu trong vòng tròn của Lauriel.", "50.6%"],
    "Laville": [["Joker", "Elsu"], ["Ngộ Không", "Zuka"], "Dùng tướng có khống chế cứng hoặc dồn dame.", "51.2%"],
    "Liliana": [["Tulane", "Zata"], ["Nakroth", "Aoi"], "Né đạn linh lực và cẩn thận dạng cáo.", "52.4%"],
    "Lindis": [["Max", "Ngộ Không"], ["Zuka", "Kriknak"], "Ép rừng sớm, không cho Lindis xanh.", "48.3%"],
    "Lorion": [["Chaugnar", "Liliana"], ["Nakroth", "Quillen"], "Cẩn thận quả cầu của hắn gây choáng diện rộng.", "51.1%"],
    "Lumburr": [["Hayate", "Maloch"], ["Thane", "Baldum"], "Né chiêu cuối hất tung của hắn.", "49.7%"],
    "Lữ Bố": [["Hayate", "Omen"], ["Arum", "Aleister"], "Lên đồ giảm hồi máu và tránh solo khi hắn bật Ulti.", "50.2%"],
    "Maloch": [["Hayate", "Richter"], ["Baldum", "Thane"], "Tránh tụ lại để hắn chém Quỷ kiếm.", "51.8%"],
    "Marja": [["Hayate", "Valhein"], ["Arum", "Aleister"], "Đừng lãng phí chiêu thức khi cô ấy hóa bóng đêm.", "48.5%"],
    "Max": [["Hayate", "Omen"], ["Arum", "Aleister"], "Cẩn thận bị Max bay vào bắt lẻ khi thấp máu.", "50.9%"],
    "Mganga": [["Liliana", "Tulen"], ["Nakroth", "Quillen"], "Lên kháng phép và giảm hồi máu sớm.", "49.2%"],
    "Mina": [["Hayate", "Maloch"], ["Elsu", "Slimz"], "Đừng đánh thường quá nhiều vào Mina.", "50.5%"],
    "Moren": [["Joker", "Elsu"], ["Ngộ Không", "Zuka"], "Ngăn cản Moren tích nội tại giáp.", "48.1%"],
    "Murad": [["Arum", "Aleister"], ["Hayate", "Valhein"], "Phá quái rừng và lính để Murad không có mục tiêu tích số.", "51.4%"],
    "Nakroth": [["Zephys", "Rourke"], ["Arum", "Aleister"], "Dùng khống chế chỉ định không thể né.", "52.1%"],
    "Natalya": [["Liliana", "Raz"], ["Nakroth", "Ngộ Không"], "Né tia sáng của cô ấy và áp sát từ phía sau.", "47.6%"],
    "Ngộ Không": [["Max", "Lindis"], ["Baldum", "Thane"], "Sử dụng phụ trợ soi tàng hình sớm.", "53.2%"],
    "Nishin": [["Hayate", "Omen"], ["Arum", "Aleister"], "Tướng mới, cần khống chế cứng để bắt.", "50.0%"],
    "Omega": [["Hayate", "Maloch"], ["Baldum", "Thane"], "Cẩn thận khả năng đẩy trụ nhanh của hắn.", "48.9%"],
    "Omen": [["Richter", "Florentino"], ["Hayate", "Slimz"], "Cẩn thận bị xích vào cột và bị thả diều.", "51.3%"],
    "Ormarr": [["Hayate", "Maloch"], ["Thane", "Baldum"], "Lên giày kiên cường để giảm thời gian bị choáng.", "47.7%"],
    "Paine": [["Chaugnar", "Lữ Bố"], ["Arum", "Aleister"], "Lên kháng phép sớm và dùng khống chế.", "52.8%"],
    "Preyta": [["Liliana", "Tulen"], ["Nakroth", "Quillen"], "Né hơi độc và cẩn thận khi hắn hóa rồng.", "46.2%"],
    "Quillen": [["Lindis", "Max"], ["Arum", "Aleister"], "Luôn quay mặt về phía Quillen để giảm sát thương.", "51.6%"],
    "Raz": [["Lauriel", "Liliana"], ["TeeMee", "Gildur"], "Tránh đứng thẳng hàng với cú đấm.", "52.0%"],
    "Richter": [["Florentino", "Omen"], ["Arum", "Aleister"], "Cẩn thận Richter núp bụi dồn dame.", "51.9%"],
    "Riktor": [["Florentino", "Omen"], ["Arum", "Aleister"], "Tương tự Richter, cẩn thận bụi cỏ.", "50.5%"],
    "Roxie": [["Hayate", "Maloch"], ["Elsu", "Slimz"], "Đừng đuổi theo Roxie khi cô ấy đang bật lửa.", "49.4%"],
    "Rourke": [["Hayate", "Omen"], ["Arum", "Aleister"], "Phá lớp giáp ảo của Rourke trước khi dồn dame.", "48.8%"],
    "Ryoma": [["Florentino", "Richter"], ["Zuka", "Ngộ Không"], "Áp sát nhanh vì Ryoma mạnh ở tầm trung.", "50.2%"],
    "Sephera": [["Liliana", "Tulen"], ["Nakroth", "Paine"], "Lên kháng phép và tránh đứng trong vòng nước.", "49.1%"],
    "Sinestrea": [["Arum", "Aleister"], ["Hayate", "Elsu"], "Cẩn thận khả năng đổi máu của cô ấy.", "51.4%"],
    "Skud": [["Hayate", "Maloch"], ["Slimz", "Elsu"], "Cẩn thận cú đấm gồng cực đau của hắn.", "50.7%"],
    "Slimz": [["Joker", "Valhein"], ["Zuka", "Ngộ Không"], "Né mũi lao cơ khí của Slimz.", "51.5%"],
    "Stuart": [["Elsu", "Joker"], ["Ngộ Không", "Zuka"], "Đợi hắn hết chiêu 2 miễn thương rồi mới đánh.", "52.6%"],
    "Superman": [["Omen", "Arum"], ["Aleister", "Alice"], "Dùng khống chế hoặc làm chậm để ngắt phi hành.", "50.3%"],
    "Edras": ["Dữ liệu đang cập nhật"],
    "Tachi": [["Omen", "Hayate"], ["Arum", "Aleister"], "Đừng để Tachi tích đủ nội tại sát thương chuẩn.", "49.8%"],
    "Taara": [["Hayate", "Maloch"], ["Max", "Mganga"], "Bắt buộc phải có giảm hồi máu.", "47.5%"],
    "Teeri": [["Joker", "Elsu"], ["Wukong", "Zuka"], "Áp sát nhanh không để Teeri bắn lan.", "51.9%"],
    "TeeMee": [["Chaugnar", "Gildur"], ["Nakroth", "Kriknak"], "Cẩn thận chiêu cuối hồi sinh của hắn.", "50.1%"],
    "Thane": [["Hayate", "Maloch"], ["Elsu", "Slimz"], "Đừng dồn hết chiêu vào Thane khi hắn còn thấp máu.", "51.0%"],
    "The Flash": [["Arum", "Aleister"], ["Hayate", "Valhein"], "Khống chế khi hắn vừa lao vào.", "48.4%"],
    "Thorne": [["Joker", "Elsu"], ["Ngộ Không", "Paine"], "Ép sớm không cho Thorne đủ 3 viên đạn tím.", "52.3%"],
    "Toro": [["Hayate", "Maloch"], ["Slimz", "Elsu"], "Đừng dồn khống chế vào Toro khi hắn đang gồng chiêu.", "48.6%"],
    "Tulen": [["Liliana", "Zata"], ["Nakroth", "Quillen"], "Lên trang bị kháng phép sớm.", "51.5%"],
    "Valhein": [["Joker", "Elsu"], ["Zuka", "Ngộ Không"], "Lên giày kiên cường để giảm choáng.", "50.8%"],
    "Veera": [["Liliana", "Raz"], ["Nakroth", "Zuka"], "Lên Huân chương Troy sớm để không bị sốc dame.", "49.3%"],
    "Veres": [["Omen", "Hayate"], ["Arum", "Aleister"], "Né vòng quay của Veres để cô ấy không hồi máu.", "51.7%"],
    "Violet": [["Joker", "Elsu"], ["Ngộ Không", "Paine"], "Áp sát khi cô ấy vừa dùng chiêu 1 để lộn.", "50.4%"],
    "Volkath": [["Arum", "Aleister"], ["Hayate", "Slimz"], "Đợi Volkath xuống ngựa rồi mới dồn dame.", "51.2%"],
    "Wonder Woman": [["Hayate", "Omen"], ["Arum", "Aleister"], "Cẩn thận khả năng chống chịu và khống chế của cô ấy.", "50.9%"],
    "Wiro": [["Hayate", "Maloch"], ["Baldum", "Thane"], "Hạ gục nhanh lần 1 rồi canh hồi sinh.", "46.1%"],
    "Xeniel": [["Hayate", "Maloch"], ["Baldum", "Thane"], "Dùng khống chế để ngắt chiêu cuối bay đi của hắn.", "49.6%"],
    "Yan": [["Omen", "Arum"], ["Aleister", "Baldum"], "Ép giao tranh sớm trước khi Yan đạt cấp 12.", "53.1%"],
    "Y'bneth": [["Hayate", "Maloch"], ["D'Arcy", "Gildur"], "Tránh đứng trong vùng chiêu cuối của hắn.", "50.2%"],
    "Yena": [["Florentino", "Richter"], ["Arum", "Aleister"], "Cẩn thận bị câm lặng và đẩy lùi liên tục.", "52.0%"],
    "Yorn": [["Ngộ Không", "Nakroth"], ["Zuka", "Paine"], "Yorn không có cơ động, sát thủ dồn dame là chết.", "50.7%"],
    "Zata": [["Aleister", "Arum"], ["Hayate", "Valhein"], "Dùng Quả cầu băng sương khi Zata bay lên.", "52.8%"],
    "Zephys": [["Lữ Bố", "Omen"], ["Arum", "Aleister"], "Càng thấp máu Zephys càng trâu, hãy dồn dame nhanh.", "49.9%"],
    "Zill": [["Keera", "Lữ Bố"], ["Arum", "Aleister"], "Dùng tướng có khả năng không thể bị chọn.", "49.0%"],
    "Zipt": [["Chaugnar", "Gildur"], ["Hayate", "Slimz"], "Cẩn thận Zipt hút đồng đội thoát thân.", "51.6%"],
    "Zuka": [["Skud", "Roxie"], ["Arum", "Aleister"], "Đừng đứng tụ lại để Zuka giẫm trúng nhiều người.", "53.5%"],
}

# --- GIAO DIỆN ---
st.write("---")
# Thanh tìm kiếm thông minh có gợi ý tên tướng
tuong_selected = st.selectbox(
    "🔥 Nhập tên tướng địch (Ví dụ: Zuka, Yan, Stuart...):",
    options=[""] + sorted(list(data_lq.keys())),
    format_func=lambda x: "Gõ để tìm kiếm..." if x == "" else x
)

if tuong_selected:
    res = data_lq[tuong_selected]
    
    # Hiển thị Tỷ lệ thắng
    st.markdown(f"### 📊 Phân tích tướng: **{tuong_selected}**")
    st.write(f"Tỷ lệ thắng (Winrate): **{res[3]}**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**🛡️ Khắc chế cùng đường (Solo):**")
        for t in res[0]:
            st.write(f"- {t}")
            
    with col2:
        st.info("**🎯 Khắc chế từ vị trí khác (Gank):**")
        for t in res[1]:
            st.write(f"- {t}")
            
    st.warning(f"📝 **Mẹo đối đầu:** {res[2]}")

st.divider()
st.caption("Dữ liệu được cập nhật dựa trên Meta 2026. Chúc bạn leo rank thành công!")

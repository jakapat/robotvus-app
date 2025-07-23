import streamlit as st

st.set_page_config(
    page_title="โรบอทวุส | Mental Scanner",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
    <style>
    .big-font {
        font-size: 28px;
        font-weight: bold;
        color: #00c6ff;
    }
    .robot-box {
        background-color: #1e1e1e;
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        box-shadow: 0 0 12px rgba(0,255,255,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# ส่วนหัว
st.markdown('<p class="big-font">🤖 ระบบสแกนสภาพจิตใจโดย โรบอทวุส</p>', unsafe_allow_html=True)
st.markdown('<div class="robot-box">', unsafe_allow_html=True)
st.write("กรุณากรอกข้อมูลของคุณเพื่อให้โรบอทวุสประเมินสถานะทางอารมณ์และความเครียด")
st.markdown('</div>', unsafe_allow_html=True)
st.write("")

# รับข้อมูล
st.subheader("📥 ข้อมูลผู้ใช้งาน")
mood = st.text_input("🔸 อารมณ์ปัจจุบันของคุณคืออะไร?")
stress_level = st.slider("🔸 ระดับความเครียด (0 = สบายมาก / 100 = เครียดสุด)", 0, 100, 50)
sleep_hours = st.number_input("🔸 คุณนอนกี่ชั่วโมงเมื่อคืนนี้?", 0.0, 24.0, 7.0, step=0.5)
social = st.radio("🔸 ตอนนี้คุณอยากคุยกับใครไหม?", ["ใช่", "ไม่ใช่"])

# ประเมินผล
if st.button("🚀 เริ่มวิเคราะห์ด้วยระบบ AI"):
    st.markdown("---")
    st.subheader("🧠 ผลวิเคราะห์โดยโรบอทวุส")

    # กล่องประเมิน
    with st.container():
        if stress_level > 80:
            st.error("⚠️ ระบบตรวจพบระดับความเครียดสูง! โปรดดูแลตัวเองอย่างจริงจัง")
        elif 50 < stress_level <= 80:
            st.warning("🟠 ระดับความเครียดปานกลาง โปรดหาเวลาพักบ้าง")
        else:
            st.success("🟢 ระดับความเครียดอยู่ในเกณฑ์ดี")

        if sleep_hours < 5:
            st.info("😴 คุณนอนน้อย อาจส่งผลต่ออารมณ์และสมองของคุณ")
        else:
            st.info("✅ เวลานอนเพียงพอ ระบบประสาทพร้อมใช้งาน")

        if social == "ไม่ใช่":
            st.info("🤖 โหมด: Isolation detected – แนะนำให้หาเพื่อนคุยหรือพักใจ")
        else:
            st.info("👥 ยินดีที่คุณยังเปิดรับการเชื่อมต่อกับโลกภายนอก")

    # สรุปข้อมูล
    st.markdown("### 📄 สรุปข้อมูล")
    st.write(f"• อารมณ์: `{mood}`")
    st.write(f"• ความเครียด: `{stress_level}/100`")
    st.write(f"• การนอน: `{sleep_hours}` ชั่วโมง")
    st.write(f"• อยากคุยกับคนอื่น: `{social}`")

    st.markdown("---")
    st.markdown("⚡ **ระบบโดย: โรบอทวุส รุ่นทดลอง | Powered by Streamlit**")

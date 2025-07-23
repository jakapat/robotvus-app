import streamlit as st

st.set_page_config(page_title="โรบอทวุส 🧠", page_icon="🤖")
st.title("🤖 ระบบตรวจสภาพจิตใจ ‘โรบอทวุส’")

mood = st.text_input("อารมณ์ตอนนี้เป็นยังไง?")
stress_level = st.slider("ระดับความเครียด (0–100)", 0, 100, 50)
sleep_hours = st.number_input("นอนกี่ชั่วโมงเมื่อคืน?", 0.0, 24.0, 7.0, step=0.5)
social = st.radio("อยากพูดคุยกับใครไหม?", ["ใช่", "ไม่ใช่"])

if st.button("📊 ประเมินผล"):
    st.subheader("ผลประเมินโดย โรบอทวุส")
    # ความเครียด
    if stress_level > 80:
        st.error("⚠️ เครียดสูงมาก — ระบบเตือนให้พักผ่อนนะ")
    elif stress_level > 50:
        st.warning("🟠 ความเครียดอยู่ระดับกลาง — ระวังสุขภาพใจ")
    else:
        st.success("🟢 ความเครียดอยู่ในเกณฑ์ปกติ")

    # การนอน
    if sleep_hours < 5:
        st.info("😴 นอนน้อย — ควรพักผ่อนมากขึ้น")
    else:
        st.info("✅ การนอนมีความเพียงพอ")

    # ความต้องการสื่อสาร
    if social == "ไม่ใช่":
        st.info("🤖 โหมดโดดเดี่ยว: แนะนำให้หาเพื่อนคุยบ้าง")
    else:
        st.info("👥 ดีที่อยากเชื่อมต่อกับคนอื่น")

    st.write("---")
    st.write("**สรุป:**")
    st.write(f"- อารมณ์: {mood}")
    st.write(f"- ระดับความเครียด: {stress_level}/100")
    st.write(f"- ชั่วโมงการนอน: {sleep_hours} ชม.")
    st.write(f"- อยากคุยกับใคร: {social}")

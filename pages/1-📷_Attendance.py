import datetime
import sqlite3
import streamlit as st

st.title("📷 التقاط الحضور عبر الكاميرا")

img = st.camera_input("التقط صورتك لتسجيل الحضور")

name = st.text_input("أدخل اسم الطالب:")

if st.button("تثبيت الحضور"):
  if name and img:
    now = datetime.datetime.now()
    d = now.strftime("%Y-%m-%d")
    t = now.strftime("%H:%M:%S")

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO attendance (name, date, time) VALUES (?, ?, ?)",
        (name, d, t),
    )
    conn.commit()
    conn.close()

    st.success(f"تم تسجيل حضور الطالب: {name} بنجاح! 🎓")
  else:
    st.warning("الرجاء التقاط الصورة كتابة الاسم أولاً.")

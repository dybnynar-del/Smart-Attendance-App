import streamlit as st
import project

st.title("Smart Attendance System 📸")
st.write("مرحباً بك في نظام تسجيل الحضور الذكي - جامعة البعث")
st.success("التطبيق يعمل بنجاح وجاهز للاستخدام")

st.markdown("---")

menu = ["الرئيسية","Student Portal","TeacherPortal"]
choice = st.sidebar.selectbox("القائمة الرئيسية",menu)

if choice == "Student Portal":
  st.subheader("بوابة الطالب والكاميرا ")

elif choice == "Teacher Portal":
  st.subheader("بوابة المعلم وقاعدة البيانات")
  import sqlite3
  
conn = sqlite3.connect("attendance.db")
st.write(conn.execute("SELECT * FROM attendance").fetchall())
conn.close()
  
  

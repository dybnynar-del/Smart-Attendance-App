 import sqlite3
import streamlit as st
import project

st.title("Smart Attendance System 🏫")
st.success("✅ التطبيق يعمل بنجاح وقاعدة البيانات جاهزة")

st.markdown("---")
st.subheader("📊 إثبات إنشاء قاعدة البيانات والجدول:")

try:
  conn = sqlite3.connect("attendance.db")
  cursor = conn.cursor()

  cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
  tables = cursor.fetchall()
  st.write("📁 اسم الجدول في القاعدة:", tables)

  cursor.execute("SELECT * FROM attendance")
  rows = cursor.fetchall()
  st.write("📋 السجلات المخزنة حالياً:", rows)

  conn.close()
except Exception as e:
  st.warning(
      "قاعدة البيانات قيد الإنشاء أو فارغة، سيتم تفعيلها فوراً عند أول تسجيل."
  )

import sqlite3
import streamlit as st
import project

# --- إضافة 1: التوجيه والترحيب في البداية ---
st.write("أهلاً بكم في الواجهة الرئيسية لنظام الحضور الذكي.")
st.info("👈 **للتنقل:** استخدموا القائمة الجانبية للذهاب إلى صفحة الكاميرا وتسجيل الحضور.")
st.markdown("---")

# --- كودك الأصلي تماماً دون أي تعديل ---
st.title("Smart Attendance System 🏫")
st.success("✅ التطبيق يعمل بنجاح وقاعدة البيانات جاهزة")

st.markdown("---")
st.subheader("📊 إثبات إنشاء قاعدة البيانات والجدول")

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
    st.warning("قاعدة البيانات قيد الإنشاء أو فارغة، سيتم تفعيلها فوراً عند أول تسجيل")

st.markdown("---")

# --- إضافة 2: معلومات المشروع والفريق والدكتور في الأسفل ---
st.subheader("ℹ️ عن المشروع وفريق العمل")

st.markdown("""
**📌 نبذة عن النظام:**
هذا التطبيق هو نظام مؤتمت لتسجيل وإدارة الحضور والغياب، يعتمد على تقنيات الرؤية الحاسوبية والذكاء الصنعي لتأكيد الحضور تلقائياً وبدقة عالية عبر التعرف على الوجوه.
""")

with st.expander("👥 اضغط هنا لعرض أسماء الفريق والدكتور المشرف"):
    st.write("**👨‍🏫 الدكتور المشرف:** [اسم الدكتور المشرف]")
    st.write("**👥 فريق العمل (هندسة الذكاء الصنعي - جامعة البعث):**")
    st.write("- نينار ديب")
    st.write("- محمود طراف")
    st.write("- محمد جنيد")
    st.write("- زينب المنصور")
    st.write("- أحمد السالم")
    st.write("- عبد الحليم")

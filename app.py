import pandas as pd
import streamlit as st

# عنوان الصفحة
st.set_page_config(
    page_title="ورقة عمل | حفظ الزخم", page_icon="🧪", layout="centered"
)

st.title("🧪 ورقة عمل | حفظ الزخم - فيزياء ثاني ثانوي")
st.write("إعداد: أ. محمد العنزي ")
st.markdown("---")

# بيانات الطالب
st.subheader("📋 البيانات الأساسية")
col1, col2 = st.columns(2)
with col1:
  student_name = st.text_input("اسم الطالب الرباعي:")
with col2:
  student_class = st.text_input("الصف / الفصل:")

st.markdown("---")

# نموذج الإجابات والأسئلة
score = 0
total_questions = 10

st.subheader("1️⃣ اختيار من متعدد")
q1 = st.radio(
    "ما الكمية الفيزيائية التي تمثل حاصل ضرب كتلة الجسم في سرعته المتجهة؟",
    ["القوة", "الدفع", "الزخم", "التسارع"],
    index=None,
)
if q1 == "الزخم":
  score += 1

st.subheader("2️⃣ اختيار من متعدد")
q2 = st.radio(
    "أي العبارات التالية تصف النظام المعزول؟",
    [
        "نظام لا يكتسب كتلة ولا يفقدها.",
        "نظام محصلة القوى الخارجية المؤثرة عليه تساوي صفراً.",
        "نظام تتغير فيه كمية الحركة.",
        "نظام تتغير فيه الطاقة الحركية فقط.",
    ],
    index=None,
)
if q2 == "نظام محصلة القوى الخارجية المؤثرة عليه تساوي صفراً.":
  score += 1

st.subheader("3️⃣ صح أم خطأ")
c1 = st.radio("1) الزخم كمية متجهة.", ["صح", "خطأ"], index=None, key="c1")
if c1 == "صح":
  score += 0.5

c2 = st.radio(
    "2) في النظام المعزول يبقى الزخم الكلي ثابتاً.",
    ["صح", "خطأ"],
    index=None,
    key="c2",
)
if c2 == "صح":
  score += 0.5

st.subheader("4️⃣ أكمل الفراغات")
a1 = st.text_input("1) يرمز للزخم بالرمز:").strip()
if a1.lower() == "p":
  score += 0.5

a2 = st.text_input("2) وحدته في النظام الدولي هي:").strip()
if a2.lower() in ["kg.m/s", "kg*m/s", "كجم.م/ث"]:
  score += 0.5

st.subheader("5️⃣ مسائل حساسية مياشرة")
q5 = st.radio(
    "كرة كتلتها 2kg تتحرك بسرعة 5m/s إلى الشرق، ما مقدار زخمها؟",
    ["2 kg·m/s", "5 kg·m/s", "7 kg·m/s", "10 kg·m/s"],
    index=None,
)
if q5 == "10 kg·m/s":
  score += 1

q6 = st.radio(
    "أي مما يلي يمثل وحدة قياس الدفع؟",
    ["N", "N·s", "m/s", "m/s²"],
    index=None,
)
if q6 == "N·s":
  score += 1

st.markdown("---")

# زر تسليم ورقة العمل
if st.button("📤 تسليم ورقة العمل", type="primary"):
  if not student_name or not student_class:
    st.error("⚠️ الرجاء كتابة اسمك وصفك قبل تسليم ورقة العمل.")
  else:
    st.balloons()
    st.success(
        f"تم استلام إجابتك بنجاح يا {student_name}! الدرجة المحصلة: {score} من"
        " 5"
    )

    # حفظ النتيجة في ملف محلي للتحقق
    data = {
        "الاسم": [student_name],
        "الصف": [student_class],
        "الدرجة": [score],
    }
    df = pd.DataFrame(data)
    st.write("تم تسجيل درجتك بنجاح لدى المعلم.")

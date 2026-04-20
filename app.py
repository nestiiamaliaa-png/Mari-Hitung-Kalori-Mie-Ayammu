import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Hitung Kalori Mie Ayam", page_icon="🍜", layout="centered")

st.title("🍜 Hitung Kalori Mie Ayam")
st.markdown("### Virtual Lab Matematika: Menghitung kalori mie ayam dengan konsep integral ✨")

st.write("---")

# =========================
# INPUT DASAR
# =========================
porsi = st.number_input("🍽️ Jumlah porsi", 1, 10, 1)
mie = st.slider("🍜 Berat mie (gram)", 50, 500, 100, step=10)

def jumlah_item(label, default=0.0):
    return st.number_input(label, min_value=0.0, max_value=10.0, value=default, step=0.5)

# =========================
# INPUT USER
# =========================
st.subheader("🥬 Sayur & Protein")
minyak = jumlah_item("Minyak ayam (sdm)", 1.0)
sawi = jumlah_item("Sawi (lembar)", 1.0)
daun_bawang = jumlah_item("Daun bawang (sdm)", 1.0)
ayam = jumlah_item("Ayam cincang (sdm)", 1.0)

st.subheader("🍢 Topping")
ceker = jumlah_item("Ceker (buah)")
bakso = jumlah_item("Bakso (buah)")
telur_ayam = jumlah_item("Telur ayam (butir)")
telur_puyuh = jumlah_item("Telur puyuh (butir)")
krupuk = jumlah_item("Kerupuk pangsit (sdm)")
bawang = jumlah_item("Bawang goreng (sdm)")
acar = jumlah_item("Acar (sdm)")

st.subheader("🌶️ Saus")
sambal = jumlah_item("Sambal (sdm)")
kecap = jumlah_item("Kecap (sdm)")
saos = jumlah_item("Saus tomat (sdm)")
chili_oil = jumlah_item("Chili oil (sdm)")

# =========================
# DATA KALORI
# =========================
kalori = {
    "mie": 1.3662,
    "minyak": 89.82,
    "sawi": 9.52,
    "daun_bawang": 6.53,
    "ayam": 31.24,
    "ceker": 104.90,
    "bakso": 80.04,
    "telur_ayam": 65.84,
    "telur_puyuh": 15.26,
    "krupuk": 34.20,
    "bawang": 51.00,
    "acar": 3.10,
    "sambal": 14.75,
    "kecap": 31.09,
    "saos": 11.07,
    "chili_oil": 86.57
}

# =========================
# HITUNG DETAIL
# =========================
detail = {
    "Mie": mie * kalori["mie"],
    "Minyak ayam": minyak * kalori["minyak"],
    "Sawi": sawi * kalori["sawi"],
    "Daun bawang": daun_bawang * kalori["daun_bawang"],
    "Ayam cincang": ayam * kalori["ayam"],
    "Ceker": ceker * kalori["ceker"],
    "Bakso": bakso * kalori["bakso"],
    "Telur ayam": telur_ayam * kalori["telur_ayam"],
    "Telur puyuh": telur_puyuh * kalori["telur_puyuh"],
    "Kerupuk pangsit": krupuk * kalori["krupuk"],
    "Bawang goreng": bawang * kalori["bawang"],
    "Acar": acar * kalori["acar"],
    "Sambal": sambal * kalori["sambal"],
    "Kecap": kecap * kalori["kecap"],
    "Saus tomat": saos * kalori["saos"],
    "Chili oil": chili_oil * kalori["chili_oil"]
}

total = sum(detail.values()) * porsi

# =========================
# OUTPUT TOTAL
# =========================
st.write("---")
st.subheader("🔥 Total Kalori")
st.success(f"{total:.2f} kkal")

# =========================
# TABEL SEMUA DATA
# =========================
st.write("---")
st.subheader("📋 Tabel Lengkap Data Gizi")

rows = [
["Mie", mie, 4.51*(mie/100), 25.01*(mie/100), 2.06*(mie/100), detail["Mie"]],
["Minyak ayam", minyak, 0, 0, 9.98*minyak, detail["Minyak ayam"]],
["Sawi", sawi, 0.41*sawi, 0.96*sawi, 0.45*sawi, detail["Sawi"]],
["Daun bawang", daun_bawang, 0.15*daun_bawang, 1.42*daun_bawang, 0.03*daun_bawang, detail["Daun bawang"]],
["Ayam cincang", ayam, 6.20*ayam, 0, 0.71*ayam, detail["Ayam cincang"]],
["Ceker", ceker, 9.70*ceker, 0.10*ceker, 7.30*ceker, detail["Ceker"]],
["Bakso", bakso, 4.12*bakso, 5.17*bakso, 4.76*bakso, detail["Bakso"]],
["Telur ayam", telur_ayam, 5.51*telur_ayam, 0.49*telur_ayam, 4.65*telur_ayam, detail["Telur ayam"]],
["Telur puyuh", telur_puyuh, 1.30*telur_puyuh, 0.04*telur_puyuh, 1.10*telur_puyuh, detail["Telur puyuh"]],
["Kerupuk pangsit", krupuk, 1.26*krupuk, 3.05*krupuk, 1.89*krupuk, detail["Kerupuk pangsit"]],
["Bawang goreng", bawang, 1*bawang, 5*bawang, 3*bawang, detail["Bawang goreng"]],
["Acar", acar, 0.09*acar, 0.62*acar, 0.03*acar, detail["Acar"]],
["Sambal", sambal, 0.50*sambal, 1.50*sambal, 0.75*sambal, detail["Sambal"]],
["Kecap", kecap, 0.13*kecap, 7.64*kecap, 0, detail["Kecap"]],
["Saus tomat", saos, 0.17*saos, 2.51*saos, 0.04*saos, detail["Saus tomat"]],
["Chili oil", chili_oil, 0.07*chili_oil, 0.30*chili_oil, 9.45*chili_oil, detail["Chili oil"]],
]

df = pd.DataFrame(rows, columns=[
    "Komponen", "Jumlah",
    "Protein (g)", "Karbo (g)",
    "Lemak (g)", "Kalori (kkal)"
])

st.dataframe(df, use_container_width=True)

# =========================
# TOTAL GIZI
# =========================
st.write("### 🔢 Total Gizi")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Protein", f"{df['Protein (g)'].sum():.2f} g")
col2.metric("Karbo", f"{df['Karbo (g)'].sum():.2f} g")
col3.metric("Lemak", f"{df['Lemak (g)'].sum():.2f} g")
col4.metric("Kalori", f"{total:.2f} kkal")

# =========================
# GRAFIK
# =========================
st.write("---")
st.subheader("📊 Distribusi Kalori")

fig, ax = plt.subplots(figsize=(8,8))
ax.pie(detail.values(), labels=detail.keys(), autopct="%1.1f%%")
st.pyplot(fig)

# =========================
# INTEGRAL
# =========================
st.write("---")
st.subheader("📘 Konsep Integral")

st.latex(r"E = \int_{0}^{m}(4P + 4K + 9L)\,dx")

st.markdown("""
**Keterangan**
- E = Energi total (kkal)
- m = massa makanan (gram)
- P = protein per gram
- K = karbohidrat per gram
- L = lemak per gram

### Acuan Atwater:
- 1 g protein = 4 kkal
- 1 g karbohidrat = 4 kkal
- 1 g lemak = 9 kkal
""")

st.info("Integral digunakan untuk menjumlahkan kontribusi energi tiap gram makanan.")

st.write("---")
st.caption("✨ Virtual Lab Kalori Mie Ayam - Final Fix")

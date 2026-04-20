import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Hitung Kalori Mie Ayam", page_icon="🍜")

st.title("🍜 Berapa Kalori Mie Ayam yang Kamu Makan Hari Ini?")
st.markdown("### Siapa sangka ternyata kita bisa menghitung kalori mie ayam menggunakan konsep integral dalam kehidupan nyata ✨")

st.write("---")

# =========================
# INPUT DASAR
# =========================
porsi = st.number_input("🍽️ Jumlah mangkok/porsi", 1, 10, 1)

mie_option = st.selectbox("🍜 Jumlah mie (dalam gram)", ["100", "200", "300", "400", "500", "lebih"])
if mie_option == "lebih":
    mie_val = st.number_input("Masukkan gram mie:", 500, 1000, 600)
else:
    mie_val = int(mie_option)

# =========================
# FUNGSI INPUT FLEXIBLE
# =========================
def input_flex(label, opsi, min_val=1):
    pilihan = st.selectbox(label, opsi)
    if pilihan == "lebih":
        return st.number_input(
            f"Masukkan jumlah {label}",
            min_value=float(min_val),
            max_value=100.0,
            value=float(min_val),
            step=0.5
        )
    return float(pilihan)

input_fleksibel = input_flex

# =========================
# INPUT LAIN
# =========================
minyak = input_fleksibel("🛢️ Minyak ayam (sdm)", ["0.5","1","2","3","lebih"])

st.subheader("🥬 Sayuran")
sawi = input_fleksibel("Sawi (lembar)", ["1","2","3","lebih"], 1)
daun_bawang = input_fleksibel("Daun bawang (sdm)", ["0.5","1","2","3","lebih"])

st.subheader("🍗 Ayam")
ayam = input_fleksibel("Ayam cincang (sdm)", ["1","2","3","4","5","lebih"], 1)

st.subheader("🍢 Topping")

def topping_input(nama, opsi):
    pakai = st.radio(f"{nama}?", ["Tidak", "Ya"], horizontal=True)
    if pakai == "Ya":
        return input_fleksibel(f"Jumlah {nama}", opsi)
    return 0

ceker = topping_input("Ceker 🍗", ["1","2","3","lebih"])
bakso = topping_input("Bakso 🧆", ["1","2","3","lebih"])

telur_pakai = st.radio("Telur?", ["Tidak", "Ya"], horizontal=True)
telur_ayam = 0
telur_puyuh = 0

if telur_pakai == "Ya":
    jenis = st.radio("Jenis telur", ["Telur Ayam 🥚", "Telur Puyuh 🐣"], horizontal=True)
    jumlah = input_fleksibel("Jumlah telur", ["1","2","3","lebih"], 1)
    if "Ayam" in jenis:
        telur_ayam = jumlah
    else:
        telur_puyuh = jumlah

krupuk = topping_input("Kerupuk pangsit (sdm)", ["1","2","3","lebih"])
bawang = topping_input("Bawang goreng (sdm)", ["1","2","3","lebih"])
acar = topping_input("Acar (sdm)", ["1","2","3","lebih"])

st.subheader("🌶️ Saos")
sambal = topping_input("Sambal (sdm)", ["0.5","1","2","3","4","5","lebih"])
kecap = topping_input("Kecap (sdm)", ["0.5","1","2","3","4","5","lebih"])
saos = topping_input("Saos tomat (sdm)", ["0.5","1","2","3","4","5","lebih"])
chili_oil = topping_input("Chili Oil (sdm)", ["0.5","1","2","3","4","5","lebih"])

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
# HITUNG
# =========================
detail = {}

detail["Mie"] = mie_val * kalori["mie"]
detail["Minyak ayam"] = minyak * kalori["minyak"]
detail["Sawi"] = sawi * kalori["sawi"]
detail["Daun bawang"] = daun_bawang * kalori["daun_bawang"]
detail["Ayam cincang"] = ayam * kalori["ayam"]
detail["Ceker"] = ceker * kalori["ceker"]
detail["Bakso"] = bakso * kalori["bakso"]
detail["Telur ayam"] = telur_ayam * kalori["telur_ayam"]
detail["Telur puyuh"] = telur_puyuh * kalori["telur_puyuh"]
detail["Kerupuk pangsit"] = krupuk * kalori["krupuk"]
detail["Bawang goreng"] = bawang * kalori["bawang"]
detail["Acar"] = acar * kalori["acar"]
detail["Sambal"] = sambal * kalori["sambal"]
detail["Kecap"] = kecap * kalori["kecap"]
detail["Saos tomat"] = saos * kalori["saos"]
detail["Chili Oil"] = chili_oil * kalori["chili_oil"]

total = sum(detail.values()) * porsi

# =========================
# OUTPUT
# =========================
st.write("---")
st.subheader("🔥 Total Kalori")
st.success(f"{int(total)} kkal")

if total < 400:
    st.success("🟢 Rendah kalori")
elif total < 800:
    st.warning("🟡 Kalori sedang")
else:
    st.error("🔴 Kalori tinggi")

# =========================
# GRAFIK
# =========================
st.subheader("📊 Distribusi Kalori")
fig, ax = plt.subplots(figsize=(8,8))
ax.pie(detail.values(), labels=detail.keys(), autopct='%1.1f%%')
st.pyplot(fig)

# =========================
# TABEL DATA GIZI
# =========================
st.write("---")
st.subheader("📋 Tabel Data Gizi & Kalori")

rows = []

data_input = [
    ("Mie", mie_val, detail["Mie"], 14.0*(mie_val/100), 72.0*(mie_val/100), 2.0*(mie_val/100)),
    ("Minyak ayam", minyak, detail["Minyak ayam"], 0, 0, 9.98 * minyak),
    ("Sawi", sawi, detail["Sawi"], 0.41 * sawi, 0.96 * sawi, 0.45 * sawi),
    ("Daun bawang", daun_bawang, detail["Daun bawang"], 0.15 * daun_bawang, 1.42 * daun_bawang, 0.03 * daun_bawang),
    ("Ayam cincang", ayam, detail["Ayam cincang"], 6.20 * ayam, 0, 0.71 * ayam),
    ("Ceker", ceker, detail["Ceker"], 9.70 * ceker, 0.10 * ceker, 7.30 * ceker),
    ("Bakso", bakso, detail["Bakso"], 4.12 * bakso, 5.17 * bakso, 4.76 * bakso),
    ("Telur ayam", telur_ayam, detail["Telur ayam"], 5.51 * telur_ayam, 0.49 * telur_ayam, 4.65 * telur_ayam),
    ("Telur puyuh", telur_puyuh, detail["Telur puyuh"], 1.30 * telur_puyuh, 0.04 * telur_puyuh, 1.10 * telur_puyuh),
    ("Kerupuk pangsit", krupuk, detail["Kerupuk pangsit"], 1.26 * krupuk, 3.05 * krupuk, 1.89 * krupuk),
    ("Bawang goreng", bawang, detail["Bawang goreng"], 1 * bawang, 5 * bawang, 3 * bawang),
    ("Acar", acar, detail["Acar"], 0.09 * acar, 0.62 * acar, 0.03 * acar),
    ("Sambal", sambal, detail["Sambal"], 0.50 * sambal, 1.50 * sambal, 0.75 * sambal),
    ("Kecap", kecap, detail["Kecap"], 0.13 * kecap, 7.64 * kecap, 0),
    ("Saos tomat", saos, detail["Saos tomat"], 0.17 * saos, 2.51 * saos, 0.04 * saos),
    ("Chili Oil", chili_oil, detail["Chili Oil"], 0.07 * chili_oil, 0.30 * chili_oil, 9.45 * chili_oil),
]

for nama, qty, kal, p, k, l in data_input:
    if qty > 0:
        rows.append({
            "Komponen": nama,
            "Jumlah": qty,
            "Protein (g)": round(p,2),
            "Karbo (g)": round(k,2),
            "Lemak (g)": round(l,2),
            "Kalori (kkal)": round(kal,2)
        })

df = pd.DataFrame(rows)
st.dataframe(df, use_container_width=True)

st.write("### 🔢 Total Gizi")

total_protein = df["Protein (g)"].sum() * porsi
total_karbo = df["Karbo (g)"].sum() * porsi
total_lemak = df["Lemak (g)"].sum() * porsi

col1, col2, col3, col4 = st.columns(4)

col1.metric("Protein", f"{total_protein:.2f} g")
col2.metric("Karbo", f"{total_karbo:.2f} g")
col3.metric("Lemak", f"{total_lemak:.2f} g")
col4.metric("Kalori", f"{total:.2f} kkal")

# =========================
# PENJELASAN INTEGRAL
# =========================
st.write("---")
st.subheader("📘 Pendekatan Integral")

st.latex(r"E = \int_{0}^{m} \left(4P + 4K + 9L\right)\,dx")

st.markdown("""
### Keterangan:
- **E** = energi total (kkal)
- **m** = massa bahan makanan (gram)
- **P** = kandungan protein per gram
- **K** = kandungan karbohidrat per gram
- **L** = kandungan lemak per gram

### Acuan Nilai Kalori Makronutrien:
- 1 gram protein = **4 kkal**
- 1 gram karbohidrat = **4 kkal**
- 1 gram lemak = **9 kkal**
""")

st.info("Integral digunakan untuk menjumlahkan kontribusi energi secara kontinu berdasarkan massa setiap komponen makanan.")

st.write("---")
st.caption("✨ Virtual Lab Matematika - Integral Kalori Mie Ayam 🚀")

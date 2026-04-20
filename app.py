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

st.caption("Kategori berdasarkan acuan FDA:")

if total <= 40:
    st.success("🟢 Rendah kalori")
elif total <= 100:
    st.warning("🟡 Kalori sedang")
elif total >= 400:
    st.error("🔴 Tinggi kalori")
else:
    st.info("🟠 Di antara kategori sedang dan tinggi")

# =========================
# GRAFIK
# =========================
st.subheader("📊 Distribusi Kalori")
fig, ax = plt.subplots(figsize=(8,8))
ax.pie(detail.values(), labels=detail.keys(), autopct='%1.1f%%')
st.pyplot(fig)

# =========================
# TABEL DATA GIZI (SEMUA DATA ACUAN)
# =========================
st.write("---")
st.subheader("📋 Tabel Data Gizi & Kalori (Semua Komponen)")

rows_all = []

data_input = [
    (1,"Mie","100 g",100,mie_val/100,detail["Mie"],4.51,25.01,2.06,"E_mie = ∫₀¹⁰⁰ (4P+4K+9L) dx"),
    (2,"Minyak ayam","1 sdm",10,minyak,detail["Minyak ayam"],0.00,0.00,9.98,"E_mb = ∫₀¹⁰ (9L) dx"),
    (3,"Sawi","1 lembar",20,sawi,detail["Sawi"],0.41,0.96,0.45,"E_sawi = ∫₀²⁰ (4P+4K+9L) dx"),
    (4,"Daun bawang","1 sdm",10,daun_bawang,detail["Daun bawang"],0.15,1.42,0.03,"E_db = ∫₀¹⁰ (4P+4K+9L) dx"),
    (5,"Ayam cincang","1 sdm",20,ayam,detail["Ayam cincang"],6.20,0.00,0.71,"E_ac = ∫₀²⁰ (4P+9L) dx"),
    (6,"Ceker","1 buah",50,ceker,detail["Ceker"],9.70,0.10,7.30,"E_ceker = ∫₀⁵⁰ (4P+4K+9L) dx"),
    (7,"Bakso","1 buah",30,bakso,detail["Bakso"],4.12,5.17,4.76,"E_bakso = ∫₀³⁰ (4P+4K+9L) dx"),
    (8,"Telur ayam","1 butir",60,telur_ayam,detail["Telur ayam"],5.51,0.49,4.65,"E_ta = ∫₀⁶⁰ (4P+4K+9L) dx"),
    (9,"Telur puyuh","1 butir",9,telur_puyuh,detail["Telur puyuh"],1.30,0.04,1.10,"E_tp = ∫₀⁹ (4P+4K+9L) dx"),
    (10,"Kerupuk pangsit","1 sdm",10,krupuk,detail["Kerupuk pangsit"],1.26,3.05,1.89,"E_kp = ∫₀¹⁰ (4P+4K+9L) dx"),
    (11,"Bawang goreng","1 sdm",10,bawang,detail["Bawang goreng"],1.00,5.00,3.00,"E_bg = ∫₀¹⁰ (4P+4K+9L) dx"),
    (12,"Acar","1 sdm",15,acar,detail["Acar"],0.09,0.62,0.03,"E_acar = ∫₀¹⁵ (4P+4K+9L) dx"),
    (13,"Sambal","1 sdm",10,sambal,detail["Sambal"],0.50,1.50,0.75,"E_sambal = ∫₀¹⁰ (4P+4K+9L) dx"),
    (14,"Saus tomat","1 sdm",10,saos,detail["Saos tomat"],0.17,2.51,0.04,"E_st = ∫₀¹⁰ (4P+4K+9L) dx"),
    (15,"Kecap","1 sdm",10,kecap,detail["Kecap"],0.13,7.64,0.00,"E_kecap = ∫₀¹⁰ (4P+4K) dx"),
    (16,"Chili oil","1 sdm",10,chili_oil,detail["Chili Oil"],0.07,0.30,9.45,"E_co = ∫₀¹⁰ (4P+4K+9L) dx"),
]

for no,nama,takaran,berat,qty,kal,p,k,l,integral in data_input:
    rows_all.append({
        "No": no,
        "Komponen": nama,
        "Takaran Pakai": takaran,
        "Berat (g)": berat,
        "Protein (g)": p,
        "Karbohidrat (g)": k,
        "Lemak (g)": l,
        "Konsep Integral": integral,
        "Kalori (kkal)": round(kal if nama=="Mie" else (4*p+4*k+9*l),2)
    })

df_all = pd.DataFrame(rows_all)
df_all.index = range(1, len(df_all)+1)
st.dataframe(df_all, use_container_width=True)

# =========================
# TABEL ITEM YANG DIPILIH USER
# =========================
st.subheader("🛒 Tabel Item yang Dipilih")

rows_pilih = []

for no,nama,takaran,berat,qty,kal,p,k,l,integral in data_input:
    if qty > 0:
        rows_pilih.append({
            "No": no,
            "Komponen": nama,
            "Jumlah Dipilih": qty,
            "Berat Total (g)": round(berat*qty,2),
            "Protein (g)": round(p*qty,2),
            "Karbohidrat (g)": round(k*qty,2),
            "Lemak (g)": round(l*qty,2),
            "Kalori (kkal)": round(kal,2)
        })

df_pilih = pd.DataFrame(rows_pilih)
df_pilih.index = range(1, len(df_pilih)+1)
st.dataframe(df_pilih, use_container_width=True)

# =========================
# TOTAL GIZI
# =========================
st.write("### 🔢 Total Gizi")

total_protein = df_pilih["Protein (g)"].sum() * porsi
total_karbo = df_pilih["Karbohidrat (g)"].sum() * porsi
total_lemak = df_pilih["Lemak (g)"].sum() * porsi

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

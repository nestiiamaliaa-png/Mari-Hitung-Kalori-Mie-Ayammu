import streamlit as st
import matplotlib.pyplot as plt

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

(Acuan umum: **Atwater General Factor System**, digunakan dalam ilmu gizi internasional)
""")

st.markdown(f"""
### Contoh pada mie {mie_val} gram:

E = ∫₀^({mie_val}) (4P + 4K + 9L) dx

Hasil energi mie = **{detail["Mie"]:.2f} kkal**

### Total seluruh komponen:

K_total = Σ Eᵢ

Total kalori mie ayam = **{total:.2f} kkal**
""")

st.info("Integral digunakan untuk menjumlahkan kontribusi energi secara kontinu berdasarkan massa setiap komponen makanan.")

st.write("---")
st.caption("✨ Virtual Lab Matematika - Integral Kalori Mie Ayam 🚀")

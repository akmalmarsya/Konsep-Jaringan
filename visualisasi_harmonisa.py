import numpy as np
import matplotlib.pyplot as plt

HARMONISA = [1, 3, 5, 7, 9, 10]   
F0 = 1.0                          
PERIODE_TAMPIL = 2               

t = np.linspace(0, PERIODE_TAMPIL / F0, 2000)


def komponen(n, t):
    """Satu komponen harmonisa ke-n (amplitudo mengecil 1/n)."""
    return (4 / (np.pi * n)) * np.sin(2 * np.pi * n * F0 * t)


persegi_ideal = np.sign(np.sin(2 * np.pi * F0 * t))

semua_komponen = {n: komponen(n, t) for n in HARMONISA}

jumlah_bertahap = []        
total = np.zeros_like(t)
dipakai = []
for n in HARMONISA:
    total = total + semua_komponen[n]
    dipakai.append(str(n))
    jumlah_bertahap.append(("+".join(dipakai), total.copy()))

warna = plt.cm.viridis(np.linspace(0, 0.9, len(HARMONISA)))

fig, axs = plt.subplots(2, 2, figsize=(14, 8.5))
fig.suptitle("Penjumlahan Sinyal Harmonisa: " + ", ".join(map(str, HARMONISA)),
             fontsize=15, fontweight="bold")

ax = axs[0, 0]
for (n, y), c in zip(semua_komponen.items(), warna):
    ax.plot(t, y, color=c, lw=1.5, label=f"n = {n}")
ax.set_title("(a) Komponen harmonisa individu")
ax.set_xlabel("Waktu (detik)")
ax.set_ylabel("Amplitudo")
ax.axhline(0, color="gray", lw=0.8)
ax.legend(ncol=3, fontsize=9, loc="upper right")
ax.grid(alpha=0.3)

ax = axs[0, 1]
amplitudo = [4 / (np.pi * n) for n in HARMONISA]
bars = ax.bar([str(n) for n in HARMONISA], amplitudo, color=warna)
for b, a in zip(bars, amplitudo):
    ax.text(b.get_x() + b.get_width() / 2, a + 0.02, f"{a:.2f}",
            ha="center", fontsize=9)
ax.set_title("(b) Spektrum amplitudo  A_n = 4 / (πn)")
ax.set_xlabel("Nomor harmonisa (n)")
ax.set_ylabel("Amplitudo")
ax.set_ylim(0, max(amplitudo) * 1.15)
ax.grid(axis="y", alpha=0.3)

ax = axs[1, 0]
for (label, y), c in zip(jumlah_bertahap, warna):
    ax.plot(t, y, color=c, lw=1.4, alpha=0.9,
            label=f"{label}")
ax.set_title("(c) Penjumlahan bertahap (makin banyak komponen)")
ax.set_xlabel("Waktu (detik)")
ax.set_ylabel("Amplitudo")
ax.axhline(0, color="gray", lw=0.8)
ax.legend(fontsize=8, loc="upper right", title="komponen dijumlah")
ax.grid(alpha=0.3)

ax = axs[1, 1]
ax.plot(t, persegi_ideal, "--", color="gray", lw=1.5,
        label="Gelombang persegi ideal")
ax.plot(t, jumlah_bertahap[-1][1], color="#d62728", lw=2,
        label="Jumlah: " + " + ".join(map(str, HARMONISA)))
ax.set_title("(d) Hasil penjumlahan vs gelombang persegi")
ax.set_xlabel("Waktu (detik)")
ax.set_ylabel("Amplitudo")
ax.axhline(0, color="gray", lw=0.8)
ax.legend(fontsize=9, loc="upper right")
ax.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("visualisasi_harmonisa.png", dpi=150)
print("Gambar disimpan: visualisasi_harmonisa.png")
plt.show()
# Latihan Bab 1: Pengantar Jaringan Internet

## Level A — Ingatan dan Pemahaman

### 1. Pengertian Jaringan Komputer dan Empat Unsur Pokoknya
Jaringan komputer adalah sekumpulan perangkat otonom yang saling terhubung melalui satu atau lebih media komunikasi untuk bertukar data dan berbagi sumber daya. Empat unsur pokoknya meliputi:
* **Perangkat akhir (host/end system):** Sumber atau tujuan data, seperti laptop atau server.
* **Media komunikasi:** Jalur pengiriman data, baik berupa fisik (kabel tembaga/fiber) maupun nirkabel (gelombang radio).
* **Perangkat perantara:** Alat pengatur lalu lintas data, seperti switch dan router.
* **Protokol:** Aturan baku yang disepakati agar perangkat bisa saling berkomunikasi.

### 2. Perangkat Otonom dalam Definisi Jaringan
Perangkat otonom berarti setiap komputer atau perangkat tetap memiliki kendali, sistem operasi, dan fungsi komputasinya sendiri secara mandiri. Ketika laptop bergabung ke jaringan kampus, ia tidak kehilangan identitasnya atau diambil alih sepenuhnya menjadi satu mesin raksasa.

### 3. Perbedaan Data, Sinyal, dan Paket
* **Data:** Informasi aslinya, berupa teks, gambar, atau video.
* **Sinyal:** Bentuk fisik dari data agar bisa merambat melalui media, seperti pulsa cahaya di kabel optik atau tegangan listrik.
* **Paket:** Data berukuran besar yang sudah dipecah menjadi potongan-potongan kecil dan diberi label atau header agar mudah dikirim secara bergantian melalui jaringan.

### 4. Perbedaan PAN, LAN, MAN, dan WAN
* **PAN (Personal Area Network):** Jaringan untuk perangkat sangat dekat yang sifatnya personal dan berfokus pada *user* tunggal (misalnya HP ke *smartwatch*).
* **LAN (Local Area Network):** Jaringan dengan kendali administratif milik satu organisasi, biasanya menggunakan teknologi Ethernet/Wi-Fi dengan kapasitas tinggi.
* **MAN (Metropolitan Area Network):** Jaringan metropolitan yang menghubungkan beberapa LAN dalam satu kota, biasanya melibatkan pihak ketiga atau operator untuk penyediaan infrastruktur *backbone*.
* **WAN (Wide Area Network):** Jaringan antar-wilayah yang infrastrukturnya dominan dikelola oleh operator telekomunikasi (ISP) dengan variasi kualitas dan latensi, memanfaatkan tautan khusus, VPN, atau satelit.

### 5. Perbedaan Intranet, Ekstranet, dan Internet Publik
* **Intranet:** Jaringan tertutup yang aksesnya khusus untuk orang dalam organisasi saja (contoh: portal sistem informasi akademik mahasiswa).
* **Ekstranet:** Intranet yang sebagian layanannya dibuka untuk pihak luar tertentu yang sudah diberi izin (seperti mitra atau vendor).
* **Internet Publik:** Jaringan yang terbuka untuk umum dan masyarakat luas, meskipun beberapa layanannya tetap membutuhkan *login*.

### 6. Alasan Wi-Fi Tidak Dapat Disamakan dengan Internet
Wi-Fi hanyalah teknologi media transmisi nirkabel untuk membangun jaringan lokal (LAN). Perangkat bisa saja saling terhubung ke satu Wi-Fi yang sama untuk berbagi file atau mencetak dokumen, meskipun jaringan router Wi-Fi tersebut sedang terputus (tidak ada koneksi) ke Internet luar.

### 7. Perbedaan Client, Server, dan Peer
* **Client:** Perangkat yang tugasnya meminta data atau layanan, misalnya browser di laptop.
* **Server:** Perangkat pusat yang bertugas menyediakan layanan secara terus-menerus.
* **Peer:** Perangkat dalam jaringan P2P yang dapat bertindak sebagai *client* yang meminta file sekaligus *server* yang memberikan file ke *user* lain secara bersamaan.

### 8. Perbedaan Bandwidth, Throughput, dan Goodput
* **Bandwidth:** Kapasitas maksimal teoritis dari sebuah jalur jaringan.
* **Throughput:** Kecepatan asli dari seluruh data yang berhasil terkirim dalam satu waktu, termasuk *overhead* dari protokol.
* **Goodput:** Kecepatan spesifik dari data/muatan aplikasi yang benar-benar berguna dan diterima dengan utuh.

### 9. Empat Komponen Nodal Delay
* **Processing delay:** Waktu perangkat perantara (seperti router) memeriksa paket.
* **Queuing delay:** Waktu tunggu paket saat antre di dalam *buffer* router.
* **Transmission delay:** Waktu yang dibutuhkan untuk mendorong seluruh bit paket masuk ke dalam kabel media transmisi.
* **Propagation delay:** Waktu tempuh rambatan sinyal dari satu titik ke titik lain.

### 10. Alasan Web Tidak Sama dengan Internet
Internet adalah infrastruktur dasar berupa jaringan dari jaringan di seluruh dunia. Sedangkan Web hanyalah salah satu layanan aplikasi berbasis HTTP/HTML yang beroperasi menumpang di atas infrastruktur Internet tersebut. Layanan lain seperti surel (email) dan koneksi SSH juga menggunakan Internet tanpa harus menggunakan Web.

---

## Level B — Penerapan dan Analisis

### 11. Perhitungan Transmission Delay dan Komponen Delay Lainnya
* **Diketahui:**
  * Ukuran paket ($L$) = $1.000\text{ byte} = 8.000\text{ bit}$
  * Kecepatan tautan ($R$) = $10\text{ Mbps} = 10.000.000\text{ bps}$
* **Rumus:**
  $$d_{\text{trans}} = \frac{L}{R}$$
* **Perhitungan:**
  $$d_{\text{trans}} = \frac{8.000}{10.000.000} = 0,0008\text{ detik} = 0,8\text{ ms}$$
* **Komponen Delay Lain yang Belum Tercakup:**
  1. **Processing delay:** Waktu router memproses header paket.
  2. **Queuing delay:** Waktu tunggu paket saat antre di buffer router.
  3. **Propagation delay:** Waktu tempuh sinyal fisik merambat di dalam media transmisi.

### 12. Hipotesis Masalah Throughput Rendah di Satu Lantai Kampus
Jika koneksi pusat atau ISP aman, masalah kemungkinan ada di area lokal (*access network* / *network edge*):
1. Access Point (Wi-Fi) di lantai tersebut terlalu padat karena menampung terlalu banyak *user* di waktu yang sama.
2. Terjadi interferensi frekuensi radio di lantai tersebut (misalnya banyak tembok tebal atau bentrok dengan sinyal perangkat lain).
3. Kabel fisik (LAN) yang menyambungkan switch utama ke switch lantai tersebut mengalami kerusakan atau kualitasnya menurun.
4. Port *uplink* pada switch di lantai tersebut mentok di limit kapasitas rendah (misalnya hanya pakai port 100 Mbps).
5. Adanya salah konfigurasi pada aturan QoS (*Quality of Service*) yang mencekik batasan bandwidth khusus untuk subnet di lantai itu.

### 13. Perbandingan Kebutuhan Jaringan: Transfer Berkas Cadangan vs Panggilan Video
* **Transfer Berkas Cadangan:** Kebutuhan utamanya adalah integritas data (tidak boleh ada paket yang korup/hilang) dan kapasitas yang besar. Metrik paling penting adalah **throughput**. Toleran terhadap delay/jitter, serta menangani *packet loss* dengan pengiriman ulang (TCP).
* **Panggilan Video:** Kebutuhan utamanya adalah kelancaran dan waktu respons seketika (*real-time*). Metrik paling penting adalah **latency/delay** dan **jitter** yang harus sangat rendah. Masih menoleransi sedikit *packet loss* karena kehilangan beberapa frame gambar lebih baik daripada video tertunda lama.

### 14. Evaluasi Redundansi Dua Koneksi Operator pada Jalur Ducting yang Sama
Kualitas redundansinya buruk dari sisi topologi fisik. Meskipun secara logis dan administratif organisasi tersebut menggunakan dua operator berbeda, strategi ini masih memiliki *Single Point of Failure*. Jika ada pohon tumbang menimpa tiang, tiang ditabrak mobil, atau galian tanah memutus *ducting*, kedua koneksi Internet akan mati secara bersamaan. Redundansi ideal harus memiliki jalur fisik (rute kabel) yang terpisah.

### 15. Alasan Penambahan Bandwidth Tidak Selalu Mengurangi Waktu Akses Server Jauh
Bandwidth hanya memperlebar jalur agar lebih banyak paket data yang dapat dikirim secara bersamaan (*transmission delay*). Namun, bandwidth tidak bisa mempercepat rambatan fisik sinyal data dari komputer ke server beda benua (*propagation delay*). Sebesar apa pun kapasitas bandwidth yang dibeli, kecepatan sinyal tetap dibatasi oleh jarak fisik dan batas kecepatan cahaya di dalam media fiber optik.

### 16. Perhitungan Downtime Ketersediaan 99,9% vs 99,99% Dalam Satu Tahun
Satu tahun (non-kabisat) = $365\text{ hari} = 8.760\text{ jam} = 525.600\text{ menit}$.
* **Ketersediaan 99,9% (Downtime 0,1%):**
  $$\text{Downtime} = 0,001 \times 8.760\text{ jam} = 8,76\text{ jam}$$
* **Ketersediaan 99,99% (Downtime 0,01%):**
  $$\text{Downtime} = 0,0001 \times 525.600\text{ menit} = 52,56\text{ menit per tahun}$$
* **Perbandingan:** Target 99,99% jauh lebih ketat karena hanya mengizinkan layanan mati kurang dari 1 jam dalam setahun penuh, berbeda dengan 99,9% yang masih menoleransi mati sistem hingga nyaris 9 jam.

### 17. Kelebihan dan Kelemahan Client–Server vs P2P untuk Distribusi Berkas Besar
* **Client–Server:**
  * *Kelebihan:* Pengelolaan data, keamanan, dan pembaruan file sangat mudah karena terpusat di satu server.
  * *Kelemahan:* Rawan menjadi titik kemacetan (*bottleneck*). Jika ribuan *user* mengunduh file besar bersamaan, server kelebihan beban dan membutuhkan biaya bandwidth yang mahal.
* **Peer-to-Peer (P2P):**
  * *Kelebihan:* Sangat mudah diperluas (*scalable*). Semakin banyak *user* yang mengunduh, semakin banyak sumber data yang membagikan file tersebut, sehingga beban server utama sangat ringan.
  * *Kelemahan:* Keamanan dan konsistensi file sulit dijamin karena data tersebar di banyak perangkat asing, serta kecepatan unduhan tidak menentu bergantung pada partisipasi *peer* lain.

### 18. Contoh Perbedaan Topologi Fisik dan Topologi Logis pada Jaringan Kampus
* Secara **fisik**, puluhan komputer di laboratorium dosen dan laboratorium mahasiswa menggunakan Topologi Star, di mana semuanya ditarik menggunakan kabel dan berkumpul dicolokkan ke satu Switch fisik yang sama di ruang server.
* Secara **logis**, administrator jaringan mengonfigurasi Virtual LAN (VLAN): PC Dosen dimasukkan ke VLAN 10 dan PC Mahasiswa ke VLAN 20. Meskipun tergabung di perangkat fisik yang sama, lalu lintas data mereka terpisah dan tidak bisa saling bertukar data tanpa melewati sebuah Router.

---
## Level C — Evaluasi dan Sintesis

### 19. Rancangan Klasifikasi Kebutuhan Jaringan Kampus dan Segmentasi

#### A. Klasifikasi dan Segmentasi Jaringan (VLAN / Subnetting)
Untuk mengelola jaringan kampus secara optimal, infrastruktur dibagi menjadi 5 segmen logis (*Virtual LAN* / Subnet):

| Kelompok Pengguna | Segmen Jaringan (VLAN) | Tingkat Prioritas (QoS) | Batas Bandwidth |
| :--- | :--- | :--- | :--- |
| **Mahasiswa** | VLAN 10 (Academic-Student) | Best Effort | Dibatasi per pengguna |
| **Staf Administrasi** | VLAN 20 (Admin-Staff) | Tinggi (High Priority) | Diberikan alokasi stabil |
| **Tamu (Guest)** | VLAN 30 (Guest-Network) | Rendah (Low Priority) | Dibatasi secara ketat |
| **Kamera Pengawas (CCTV)** | VLAN 40 (Surveillance-IoT) | Murni Lokal (No Internet) | Alokasi khusus internal |
| **Laboratorium Riset** | VLAN 50 (Research-Lab) | Sangat Tinggi (High Throughput) | Bandwidth besar / Uncapped |

#### B. Alasan Utama Segmentasi Jaringan
1. **Keamanan Data & Privasi:** Mencegah pengguna tidak berhak (mahasiswa/tamu) mengakses data sensitif seperti sistem penilaian, data kepegawaian, dan transaksi keuangan kampus di segmen staf administrasi.
2. **Efisiensi Trafik (Membatasi Broadcast Domain):** Mencegah kemacetan jaringan akibat lalu lintas *broadcast/multicast* yang menyebar ke seluruh kampus.
3. **Manajemen Bandwidth & Quality of Service (QoS):** Memastikan lalu lintas kritis (misalnya transaksi akademik staf dan transfer data riset) tidak terganggu oleh penggunaan hiburan atau *download* dari mahasiswa/tamu.
4. **Isolasi Masalah dan Keandalan:** Apabila segmen mahasiswa atau tamu terkena serangan *malware/virus*, infeksi terisolasi di segmen tersebut dan tidak melumpuhkan seluruh jaringan kampus.

#### C. Aturan Komunikasi Utama (Inter-VLAN Routing & Firewall Policy)
* **Mahasiswa:** Hanya dapat mengakses Internet publik dan Server Akademik (SIAKAD/LMS) via port HTTP/HTTPS (80/443). Dilarang keras mengakses VLAN Admin, CCTV, dan Lab Riset.
* **Staf Administrasi:** Diberi akses ke Internet, Server Admin, Sistem Keuangan, dan Printer Lokal. Terisolasi penuh dari VLAN Mahasiswa dan Tamu.
* **Tamu:** Hanya diizinkan mengakses Internet melalui *Captive Portal* terotentikasi. Terisolasi total dari seluruh jaringan internal kampus (*Client Isolation* diaktifkan).
* **Kamera Pengawas (CCTV):** **Dilarang memiliki akses ke Internet publik**. Kamera hanya dapat mengirim aliran video ke Server NVR (*Network Video Recorder*) lokal di VLAN 40, dan hanya dapat diakses oleh *workstation* staf keamanan di VLAN Admin.
* **Laboratorium Riset:** Diberikan akses Internet *high-speed* dan server komputasi lokal. Akses antar-lab riset diatur khusus menggunakan *Access Control List* (ACL) teridentifikasi.

---

### 20. Evaluasi Pernyataan: “Jaringan internal tidak memerlukan enkripsi karena sudah dilindungi firewall.”

Pernyataan tersebut **SALAH / TIDAK VALID**. Dalam arsitektur keamanan modern, pandangan bahwa area di dalam *firewall* perimeter pasti aman merupakan kekeliruan fatal. Prinsip keamanan modern menganut konsep **Zero Trust Architecture** (*"Never Trust, Always Verify"*).

#### Evaluasi Berdasarkan Tiga Pilar Keamanan Informasi (CIA Triad):
1. **Kerahasiaan (*Confidentiality*):**
   * *Firewall* perimeter hanya menyaring lalu lintas dari dan ke luar jaringan. *Firewall* tidak mencegah penyadapan (*packet sniffing*) di dalam jaringan lokal.
   * Apabila data internal (seperti kata sandi, NIK, atau nilai mahasiswa) dikirim tanpa enkripsi (misal via HTTP, FTP, atau Telnet), peretas yang terhubung ke Wi-Fi kampus atau orang dalam (*insider threat*) dapat membaca data sensitif tersebut menggunakan alat analisis paket.
2. **Integritas (*Integrity*):**
   * Tanpa enkripsi dan penandatanganan digital (seperti TLS/HTTPS, SSH, IPsec), data yang merambat di jaringan internal dapat diubah di tengah jalan melalui serangan *Man-in-the-Middle* (MitM), seperti *ARP Spoofing* atau *DNS Poisoning*.
   * Penyerang lokal dapat memanipulasi isi data atau menyuntikkan *code* berbahaya tanpa terdeteksi oleh *firewall*.
3. **Ketersediaan (*Availability*):**
   * Tanpa enkripsi dan otentikasi antar-layanan internal, penyerang internal yang berhasil menembus satu perangkat yang lemah dapat bergerak secara leluasa (*lateral movement*) dan menyuntikkan perintah berbahaya untuk menjatuhkan server internal (*Denial of Service*).

**Kesimpulan:** Enkripsi *end-to-end* (seperti HTTPS, TLS, SSH, MACsec) tetap mutlak diperlukan di jaringan internal.

---

### 21. Diskusi: Perkembangan Internet Tanpa Otoritas Teknis Pusat Tunggal

Internet dapat berkembang pesat hingga skala global karena dibangun di atas **Model Tata Kelola Multi-Stakeholder** dan **Arsitektur Berbasis Standar Terbuka (*Open Standards*)**. Internet bukan satu jaringan raksasa yang dimiliki satu pihak, melainkan gabungan puluhan ribu jaringan otonom (*Autonomous Systems*) yang saling terhubung secara sukarela.

Pengelolaan teknis diserahkan kepada konsorsium dan organisasi independen nirlaba, seperti:
* **IETF (*Internet Engineering Task Force*):** Mengembangkan standar dan protokol teknis (RFC).
* **IANA / ICANN:** Mengoordinasikan alokasi nama domain (DNS) dan blok alamat IP global.
* **RIRs (seperti APNIC, IDNIC):** Mengalokasikan alamat IP untuk wilayah regional.

#### A. Manfaat Tata Kelola Desentralisasi
1. **Inovasi Tanpa Izin (*Permissionless Innovation*):** Siapa pun dapat mengembangkan aplikasi baru (seperti Web, Streaming, AI) tanpa perlu meminta izin ke otoritas pusat.
2. **Skalabilitas dan Ketahanan Luar Biasa:** Tidak ada *Single Point of Failure* tingkat global. Jika satu negara atau ISP mengalami gangguan, rute lalu lintas Internet global secara otomatis memutar lewat jalur lain.
3. **Fleksibilitas dan Inklusivitas:** Standar terbuka memastikan perangkat buatan vendor mana pun di seluruh dunia dapat saling berkomunikasi secara harmonis.

#### B. Risiko Tata Kelola Desentralisasi
1. **Ancaman Fragmentasi (*Splinternet*):** Beberapa negara dapat menerapkan blokir, filter nasional, atau membuat jaringan terisolasi sendiri karena alasan politik/geopolitik.
2. **Keterlambatan Adopsi Standar Baru:** Karena transisi bersifat konsensus sukarela, pembaruan standar penting (seperti migrasi dari IPv4 ke IPv6) membutuhkan waktu puluhan tahun.
3. **Tantangan Penegakan Hukum & Keamanan Siber:** Sulit menindak kejahatan siber lintas negara karena tidak ada polisi atau otoritas peradilan tunggal yang memegang kendali atas seluruh Internet.

---

### 22. Perbandingan Circuit Switching dan Packet Switching untuk Layanan Suara

| Parameter | Circuit Switching (Contoh: Telepon Rumah / PSTN) | Packet Switching (Contoh: VoIP / WhatsApp Call / VoLTE) |
| :--- | :--- | :--- |
| **Prinsip Kerja** | Membuka saluran fisik khusus (*dedicated circuit*) dari ujung ke ujung selama panggilan. | Memecah suara digital menjadi paket-paket kecil dan dikirim secara independen melalui jaringan berbagi. |
| **Efisiensi Bandwidth** | **Sangat Rendah.** Jalur tetap terkunci meskipun ada hening/diam dalam percakapan. | **Sangat Tinggi.** Jalur digunakan bersama secara dinamis saat ada data suara yang dikirim saja. |
| **Latensi & Jitter** | Sangat konsisten dan dapat diprediksi (hampir nol *jitter*). | Bervariasi, tergantung kepadatan lalu lintas jaringan. |
| **Biaya Infrastruktur** | Sangat mahal karena membutuhkan jalur kabel/koneksi khusus. | Jauh lebih murah karena menumpang pada infrastruktur data terpadu. |

#### Alasan Suara Modern Berjalan di Jaringan Paket
Meskipun jaringan paket awalnya dirancang untuk data non-realtime, layanan suara modern (VoIP/VoLTE) dapat berjalan dengan kualitas sangat tinggi karena:
1. **Peningkatan Kapasitas Bandwidth & Kecepatan:** Jaringan modern (Fiber Optik, 4G, 5G) memiliki bandwidth sangat besar sehingga *transmission delay* menjadi sangat minim.
2. **Penerapan Quality of Service (QoS):** Perangkat perantara (router/switch) dikonfigurasi untuk memberi prioritas tertinggi pada paket suara dibanding paket data biasa (web/download).
3. **Codec Suara Canggih:** *Codec* modern (seperti OPUS) dilengkapi algoritma *Error Concealment* dan *Jitter Buffer* yang dapat menutupi sedikit hilangnya paket tanpa merusak kualitas suara yang didengar pengguna.

---

### 23. Prosedur Troubleshooting Kasus “Internet Lambat”

**Skenario Kasus:** Pengguna di Perpustakaan Kampus mengeluhkan Internet sangat lambat saat mengakses portal akademik dan video pembelajaran.

#### A. Prosedur Pengumpulan Bukti (Evidence Collection)
1. **Bukti Subjektif:** Catat identitas pengguna, waktu kejadian, lokasi spesifik, tipe koneksi (Wi-Fi/LAN), dan aplikasi yang terdampak.
2. **Bukti Objektif (Metrik Teknis):**
   * Uji latensi dan *packet loss* menggunakan `ping` ke gateway lokal, DNS kampus, dan IP luar (misal `8.8.8.8`).
   * Jalankan `traceroute` untuk melihat lompatan (*hop*) mana yang mengalami delay tinggi.
   * Amati grafik utilisasi bandwidth port *uplink* switch/Access Point perpustakaan pada dashboard NMS (*Network Management System*).

#### B. Pengujian Hipotesis
* **Hipotesis 1 (Kepadatan Frekuensi Wi-Fi):** Terlalu banyak *client* terhubung ke 1 Access Point (AP).  
  * *Pengujian:* Cek jumlah *associated client* di controller AP. Jika > 60 user per AP, Wi-Fi mengalami *saturation*.
* **Hipotesis 2 (Masalah Resolusi Nama / DNS):** Server DNS lambat merespons.  
  * *Pengujian:* Jalankan `nslookup` domain portal. Bandingkan hasil waktu balik saat ping IP langsung vs ping nama domain.
* **Hipotesis 3 (Batas Bandwidth Terpakai Habis / Congestion Uplink):** Ada pengguna yang melakukan pengunduhan file raksasa.  
  * *Pengujian:* Cek utilitas *bandwidth utilization* pada port switch *uplink* perpustakaan.

#### C. Kriteria Keberhasilan Perbaikan
* **Latensi RTT Lokal:** $< 10\text{ ms}$ ke gateway lokal, dan $< 50\text{ ms}$ ke server portal.
* **Packet Loss:** $0\%$.
* **Throughput Hasil Uji:** Mencapai SLA minimal per user (misalnya minimal $10\text{ Mbps}$ simetris per perangkat).
* **Verifikasi Pengguna:** Portal akademik dapat terbuka penuh dalam waktu kurang dari 2 detik.

---

### 24. Statistik Adopsi IPv6 di Indonesia (Google vs. APNIC)

Data pengukuran diambil dari laporan pemantauan adopsi IPv6 global:

#### A. Catatan Data Statistik
* **Tanggal Pengamatan:** Oktober 2026
* **Sumber 1: Google IPv6 Statistics**
  * *Metrik:* Persentase pengguna yang mengakses layanan Google (Google Search, YouTube, dsb.) melalui koneksi IPv6 native.
  * *Populasi:* Pengguna Internet nasional yang secara aktif mengakses infrastruktur Google.
  * *Tingkat Adopsi Indonesia:* **~15% – 16%**
* **Sumber 2: APNIC Labs IPv6 Measurement**
  * *Metrik:* **IPv6 Capable Rate** (perangkat yang mampu mengunci rute IPv6) dan **IPv6 Preferred Rate** (perangkat yang lebih memprioritaskan rute IPv6 saat *dual-stack* aktif).
  * *Populasi:* Sampel pengguna acak dari berbagai ISP di Indonesia yang memuat skrip pengujian APNIC (via *Ad-based measurement*).
  * *Tingkat Adopsi Indonesia:* **~15.8% (Preferred) / ~16.5% (Capable)**

#### B. Penyebab Perbedaan Angka Antara Kedua Sumber
1. **Metodologi Pengukuran:** Google hanya mengukur lalu lintas asli (*real user traffic*) dari pengguna yang berkunjung ke platform milik Google. APNIC menggunakan eksperimen berbasis iklan (*Ad-tracker*) yang terpasang di ribuan situs web untuk menguji kemampuan IPv6 secara otomatis di latar belakang.
2. **Efek Happy Eyeballs:** Algoritma *Happy Eyeballs* pada *browser* secara otomatis akan memilih koneksi IPv4 jika jangkauan IPv6 lokal sedikit lebih lambat, sehingga APNIC mengukur *Preferred Rate* yang sedikit berbeda dari trafik absolut yang diterima server Google.
3. **Cakupan Populasi:** Pengguna Google cenderung didominasi oleh pengguna perangkat seluler (4G/5G) yang ISP-nya telah mengaktifkan IPv6, sementara sampel APNIC mencakup variasi pengguna dari jaringan kabel (*Fixed Broadband*) daerah yang adopsi IPv6-nya masih lebih lambat.

---

### 25. Evaluasi Penggunaan Satelit Orbit Rendah (LEO) bagi Kampus Terpencil

Penggunaan satelit LEO (seperti Starlink) sangat direkomendasikan sebagai **koneksi utama (jika belum ada Fiber Optik)** atau **koneksi cadangan (*backup backhaul*)** untuk kampus di daerah 3T (Tertinggal, Terdepan, Terluar).

#### Matriks Penilaian Kriteria:
1. **Kinerja (Sangat Baik):** Latensi LEO berkisar antara $25 - 50\text{ ms}$, jauh lebih unggul dibandingkan Satelit GEO tradisional ($500 - 600\text{ ms}$). *Throughput* dapat mencapai $100 - 300+\text{ Mbps}$, sangat memadai untuk mendukung pembelajaran jarak jauh, *Webinar Video*, dan akses LMS.
2. **Biaya (Efisien):** Biaya investasi awal (*CAPEX*) dan operasional bulanan (*OPEX*) jauh lebih murah dibanding pengadaan penarikan kabel Fiber Optik melintasi hutan/lautan puluhan kilometer.
3. **Ketergantungan Cuaca (Sedang - Rentan Hujan Lezat):** Menggunakan frekuensi tinggi (Ku/Ka-band) yang rentan mengalami penurunan sinyal (*rain fade*) saat terjadi hujan lebat atau awan tebal.
4. **Pengelolaan (Sangat Mudah):** Perangkat antena bersifat *auto-pointing* (*plug-and-play*), sehingga tidak membutuhkan teknisi ahli lokal untuk penataan frekuensi rumit.
5. **Keamanan (Membutuhkan Perlindungan Tambahan):** Karena gelombang memancar bebas di udara, lalu lintas data rawan intersepsi. Kampus wajib mengimplementasikan enkripsi tingkat lanjut (*IPsec VPN*) untuk mengamankan data internal kampus ke pusat data utama.

---

### 26. Otomatisasi Jaringan: Konsistensi, Dampak Kesalahan, dan Kontrol Risiko

Otomatisasi jaringan menggunakan skrip (Python, Ansible, Terraform) menggantikan konfigurasi manual via CLI.

* **Meningkatkan Konsistensi:** Menghilangkan potensi *human error* (salah ketik) dalam tugas berulang. Konfigurasi standar (VLAN, ACL, Routing) dapat diterapkan secara identik $100\%$ pada ratusan perangkat jaringan dalam hitungan detik.
* **Memperbesar Dampak Kesalahan (*Blast Radius*):** Jika terdapat kesalahan logika atau *bug* pada satu baris skrip otomatisasi, kesalahan tersebut akan direplikasi secara masif ke seluruh perangkat jaringan serentak, yang berpotensi menyebabkan **pemadaman total seluruh jaringan kampus (*total network outage*)**.

#### Kontrol Teknis dan Proses Mitigasi Risiko:
1. **Penerapan Pipeline CI/CD dan Automated Testing:** Setiap skrip otomatisasi wajib diuji secara otomatis di jaringan simulasi/emulator (GNS3, EVE-NG, atau Containerlab) sebelum diterapkan ke perangkat produksi.
2. **Peluncuran Bertahap (*Canary / Rolling Deployment*):** Perubahan konfigurasi dieksekusi secara bertahap (misalnya $5\%$ perangkat di satu gedung terlebih dahulu), bukan sekaligus ke $100\%$ perangkat kampus.
3. **Mekanisme Automatic Rollback:** Sistem otomatisasi harus memiliki fungsi pengecekan kesehatan otomatis (*health check*). Jika indikator jaringan memburuk pasca-eksekusi, sistem langsung mengembalikan (*rollback*) konfigurasi ke kondisi stabil sebelumnya.
4. **Penerapan Infrastructure as Code (IaC) & Git:** Semua konfigurasi disimpan di dalam pustaka kode (Git) untuk mencatat riwayat perubahan (*audit trail*) dan mempermudah pemulihan data.

---

## Standar Protokol pada Teknologi Wi-Fi

| Standar IEEE | Nama Populer | Frekuensi Utama | Kecepatan Maksimal (Teoritis) | Fitur Utama & Keterangan |
| :--- | :--- | :--- | :--- | :--- |
| **802.11b / 802.11g** | Wi-Fi Lama | 2.4 GHz | 11 Mbps / 54 Mbps | Standar awal. Rawan interferensi dari alat rumah tangga (microwave, Bluetooth) karena frekuensi sempit. |
| **802.11n** | Wi-Fi 4 | 2.4 GHz & 5 GHz | Hingga 600 Mbps | Memperkenalkan teknologi **MIMO** (*Multiple-Input Multiple-Output*) dengan banyak antena untuk stabilitas koneksi. |
| **802.11ac** | Wi-Fi 5 | 5 GHz | Hingga 3,5 Gbps | Beroperasi di pita 5 GHz yang sepi. Sangat cocok untuk transfer file besar dan streaming video HD di jaringan lokal. |
| **802.11ax** | Wi-Fi 6 & 6E | 2.4 GHz, 5 GHz, & 6 GHz | Hingga 9,6 Gbps | Dirancang khusus untuk area sangat padat (*high-density*). Menggunakan teknologi **OFDMA** untuk efisiensi antrean paket. |
| **802.11be** | Wi-Fi 7 | 2.4 GHz, 5 GHz, & 6 GHz | Hingga 46 Gbps | Generasi masa depan. Menawarkan *Extreme High Throughput* (EHT), lebar kanal hingga 320 MHz, modulasi 4096-QAM, dan latensi mendekati nol. |

---
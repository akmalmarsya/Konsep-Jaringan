# Latihan Bab 2: Model Referensi OSI dan TCP/IP

## Level A — Ingatan dan Pemahaman

### 1. Alasan Komunikasi Jaringan Disusun Berlapis
Komunikasi jaringan disusun berlapis untuk membagi masalah komunikasi yang sangat kompleks menjadi bagian-bagian yang lebih kecil dengan tanggung jawab yang jelas. Manfaat utamanya meliputi:
* **Modularidad:** Fungsi kompleks dibagi menjadi modul yang lebih kecil sehingga lebih mudah dipahami dan dirancang.
* **Interoperabilitas:** Perangkat dan perangkat lunak dari vendor berbeda dapat saling berkomunikasi selama menerapkan standar protokol yang sama.
* **Evolusi Independen:** Teknologi pada satu lapisan dapat diperbarui tanpa harus merombak seluruh sistem, selama antarmuka dan layanannya tetap kompatibel.
* **Kemudahan Pengujian dan Troubleshooting:** Memudahkan isolasi dan penelusuran gangguan berdasarkan lapisan yang terdampak.
* **Penggunaan Kembali (Reusability):** Satu protokol lapisan bawah dapat mendukung berbagai aplikasi di lapisan atasnya.

---

### 2. Perbedaan Layanan, Antarmuka, dan Protokol
* **Layanan (Service):** Kemampuan atau fungsi yang diberikan oleh suatu lapisan kepada lapisan di atasnya pada sistem yang sama (*Apa yang disediakan?*).
* **Antarmuka (Interface):** Mekanisme lokal berupa API, pemanggilan fungsi, atau driver yang digunakan oleh lapisan atas untuk mengakses layanan lapisan bawah pada sistem yang sama (*Bagaimana cara mengaksesnya?*).
* **Protokol (Protocol):** Sederet aturan dan format pesan yang mengatur komunikasi antara entitas sejawat (*peer entities*) pada lapisan yang sama di sistem yang berbeda (*Bagaimana entitas sejawat berkomunikasi?*).

---

### 3. Tujuh Lapisan OSI dari Bawah ke Atas beserta Fungsi Utamanya
1. **Physical (Layer 1):** Mengirimkan bit data mentah melalui media fisik berupa sinyal listrik, cahaya, atau gelombang radio.
2. **Data Link (Layer 2):** Membentuk frame, mengelola pengalamatan fisik (MAC address), mengontrol akses media, dan melakukan deteksi kesalahan lokal pada satu tautan.
3. **Network (Layer 3):** Memproses pengalamatan logis (IP address) dan menentukan rute terbaik (routing) untuk mengantarkan paket melintasi beberapa jaringan.
4. **Transport (Layer 4):** Menyediakan komunikasi logis end-to-end antarproses aplikasi pada host yang berbeda, menggunakan nomor port untuk multiplexing, serta mengelola keandalan data (TCP vs UDP).
5. **Session (Layer 5):** Mengelola dialog atau sesi komunikasi (pembentukan, pemeliharaan, sinkronisasi, dan pengakhiran sesi) antaraplikasi.
6. **Presentation (Layer 6):** Menangani representasi data agar dipahami oleh kedua sistem, meliputi konversi format, pengodean karakter, kompresi, dan enkripsi/dekripsi data.
7. **Application (Layer 7):** Menyediakan antarmuka protokol jaringan langsung yang digunakan oleh aplikasi pengguna (contoh: HTTP, DNS, SMTP, SSH).

---

### 4. Empat Lapisan Model TCP/IP
1. **Network Access (atau Link):** Mengurus transmisi fisik dan framing pada jaringan lokal.
2. **Internet:** Mengurus pengalamatan IP dan routing paket lintas jaringan.
3. **Transport:** Mengurus komunikasi logis antaraplikasi (TCP/UDP).
4. **Application:** Menggabungkan fungsi aplikasi, representasi data, dan manajemen sesi.

---

### 5. Alasan Model TCP/IP Kadang Disajikan sebagai Lima Lapisan
Model TCP/IP kadang disajikan sebagai lima lapisan untuk kebutuhan pengajaran/pedagogis. Dalam pendekatan lima lapisan, lapisan *Network Access* dipisah menjadi dua lapisan terpisah, yaitu **Data Link Layer** dan **Physical Layer**. Pemisahan ini membantu mahasiswa membedakan antara karakteristik sinyal/media fisik dengan mekanisme pembentukan frame (*framing*) dan *switching*.

---

### 6. Perbedaan Frame, IP Packet, TCP Segment, dan UDP Datagram
* **Frame:** PDU pada Data Link Layer (Layer 2) yang memuat header L2 (alamat MAC) dan trailer deteksi kesalahan (FCS).
* **IP Packet (IP Datagram):** PDU pada Network Layer (Layer 3) yang memuat header IP (alamat IP sumber dan tujuan).
* **TCP Segment:** PDU pada Transport Layer (Layer 4) yang menggunakan protokol TCP, bersifat berorientasi koneksi (*connection-oriented*), andal, serta memiliki informasi nomor urut (*sequence number*) dan penanganan arus.
* **UDP Datagram:** PDU pada Transport Layer (Layer 4) yang menggunakan protokol UDP, bersifat tanpa koneksi (*connectionless*), sederhana, ringan, dan tanpa jaminan retransmisi.

---

### 7. Definisi Header, Trailer, dan Payload
* **Header:** Informasi kendali yang ditambahkan di **depan** (awal) data utama untuk membawa parameter komunikasi seperti alamat asal/tujuan, nomor port, atau flag.
* **Trailer:** Informasi kendali yang ditambahkan di **belakang** (akhir) data utama, biasanya memuat nilai cek kesalahan seperti Frame Check Sequence (FCS).
* **Payload:** Data atau muatan utama yang dibawa oleh suatu PDU, yang umumnya merupakan unit PDU utuh dari lapisan di atasnya.

---

### 8. Pengertian Enkapsulasi dan Dekapsulasi
* **Enkapsulasi:** Proses pembungkusan data dengan menambahkan informasi kendali (header dan/atau trailer) secara bertahap saat data bergerak **turun** dari lapisan atas ke lapisan bawah pada komputer pengirim.
* **Dekapsulasi:** Proses pelepasan dan pemeriksaan informasi kendali (header dan/atau trailer) secara bertahap saat data bergerak **naik** dari lapisan bawah ke lapisan atas pada komputer penerima.

---

### 9. Fungsi Multiplexing dan Demultiplexing
* **Multiplexing:** Proses menggabungkan beberapa aliran data dari berbagai aplikasi di lapisan atas agar dapat dikirimkan bersama-sama melalui satu saluran/layanan komunikasi di lapisan bawah.
* **Demultiplexing:** Proses memisahkan data yang diterima di lapisan bawah dan menyerahkannya kepada proses/aplikasi lapisan atas yang tepat berdasarkan pengenal khusus (seperti nomor port atau EtherType).

---

### 10. Alasan Model OSI Tidak Boleh Dianggap sebagai Spesifikasi Implementasi
Model OSI dikembangkan sebagai **model referensi konseptual** (kerangka kerja standar) untuk memandu standardisasi dan mempermudah analisis fungsi jaringan. ISO secara eksplisit menyatakan bahwa OSI bukanlah cetak biru atau spesifikasi kode program (*software stack*) yang harus diwujudkan secara persis tujuh komponen. Dalam dunia nyata, tumpukan protokol yang benar-benar diimplementasikan pada komputer dan Internet adalah model pragmatis TCP/IP.

---

## Level B — Penerapan dan Analisis

### 11. Pemetaan Protokol ke Model TCP/IP

Pemetaan sepuluh protokol ke dalam empat lapisan model TCP/IP adalah sebagai berikut:

* **Application Layer:**
  * **HTTP** (Protokol transfer web)
  * **DNS** (Layanan pemetaan nama domain)
  * **TLS** *(memerlukan penjelasan)*
* **Transport Layer:**
  * **TCP** (Protokol transport andal berorientasi koneksi)
  * **UDP** (Protokol transport datagram tanpa koneksi)
  * **QUIC** *(memerlukan penjelasan)*
* **Internet Layer:**
  * **IPv6** (Protokol pengalamatan dan routing utama)
  * **ICMP** *(memerlukan penjelasan)*
* **Network Access Layer:**
  * **Ethernet** (Teknologi LAN kabel)
  * **Wi-Fi** (Teknologi LAN nirkabel / IEEE 802.11)

#### Penjelasan Protokol Khusus:
1. **TLS (Transport Layer Security):** Dalam pemetaan OSI tradisional, TLS sering dikategorikan di *Presentation* atau *Session layer*. Namun pada model TCP/IP pragmatis, TLS bekerja di atas TCP untuk mengamankan data Application sebelum diserahkan ke Transport layer.
2. **QUIC:** QUIC dibungkus di dalam UDP datagram, tetapi secara fungsi arsitektural ia menyediakan layanan *Transport Layer* lengkap (seperti kontrol kemacetan, pengurutan, enkripsi terintegrasi, dan *stream multiplexing*).
3. **ICMP (Internet Control Message Protocol):** Pesan ICMP dienkapsulasi di dalam datagram IP, namun ICMP bertindak sebagai protokol kontrol dan pelaporan kesalahan pendukung langsung bagi *Internet Layer*.

---

### 12. Enkapsulasi Permintaan DNS melalui UDP, IPv4, dan Ethernet

Proses enkapsulasi permintaan DNS dari lapisan atas ke bawah beserta pengenal pada setiap batas lapisan:

1. **Application Layer (DNS Query):**
   * *Data/Message:* Permintaan pencarian nama domain (misal: `pens.ac.id`).
   * *Pengenal Batas (ke Transport):* Port Tujuan **53**.
2. **Transport Layer (UDP Datagram):**
   * *Header:* Menambahkan UDP Header (Port Sumber acak, Port Tujuan 53).
   * *Pengenal Batas (ke Internet):* Field Protocol ID di IPv4 Header = **17** (menunjukkan UDP).
3. **Internet Layer (IPv4 Packet):**
   * *Header:* Menambahkan IPv4 Header (IP Sumber Host, IP Tujuan Server DNS, TTL, Protocol=17).
   * *Pengenal Batas (ke Link):* Field EtherType di Ethernet Header = **`0x0800`** (menunjukkan IPv4).
4. **Data Link Layer (Ethernet Frame):**
   * *Header & Trailer:* Menambahkan Ethernet Header (MAC Sumber Host, MAC Tujuan Next-Hop/Gateway) dan Trailer FCS (*Frame Check Sequence*).
   * *Pengenal Batas (ke Physical):* Alamat MAC lokal.
5. **Physical Layer:** Frame diubah menjadi deretan bit/sinyal fisik untuk ditransmisikan melalui media.

---

### 13. Enkapsulasi HTTP/3 melalui QUIC dan Alasan Posisi QUIC

#### Alur Enkapsulasi HTTP/3:
1. **Application Layer:** Pesan HTTP/3 (Metode, URI, Header).
2. **Transport Layer (QUIC + TLS):** Data dienkapsulasi ke dalam *QUIC Packet* yang memuat Stream ID dan enkripsi TLS terintegrasi.
3. **Transport Layer (UDP Wrapper):** QUIC Packet dibungkus ke dalam *UDP Datagram* dengan Port Tujuan 443.
4. **Internet Layer:** Dibungkus IP Header (IPv4/IPv6) dengan Protocol ID = 17 (UDP) atau Next Header = 17.
5. **Data Link Layer:** Dibungkus Ethernet Header (MAC Address) dan FCS Trailer (EtherType `0x0800` atau `0x86DD`).

#### Mengapa QUIC Tetap Dianggap Protokol Transport?
Meskipun QUIC menumpang di atas UDP datagram di *user space*, QUIC secara independen menyediakan seluruh layanan utama *Transport Layer*:
* Pengiriman data yang andal (*reliable delivery*).
* Kontrol kemacetan (*congestion control*) dan kontrol aliran (*flow control*).
* Multipleks aliran (*stream multiplexing*) tanpa mengalami *head-of-line blocking*.

Penggunaan UDP hanyalah trik pembungkus (*passthrough*) agar paket QUIC dapat melewati *middlebox* (firewall/router) di Internet publik yang umumnya memblokir protokol IP baru selain TCP dan UDP.

---

### 14. Perubahan Header Paket Saat Melewati Satu Router (Tanpa NAT)

Ketika paket melewati satu router antar-subnet:

#### Header/Elemen yang BERUBAH:
1. **Header & Trailer Layer 2 (Data Link):**
   * **MAC Address Sumber:** Berubah menjadi MAC Address port keluaran (*egress interface*) milik router.
   * **MAC Address Tujuan:** Berubah menjadi MAC Address host penerima (atau router next-hop berikutnya).
   * **FCS (Frame Check Sequence):** Dihitung ulang sepenuhnya karena header L2 diganti.
2. **Header Layer 3 (IP):**
   * **TTL (IPv4) / Hop Limit (IPv6):** Berkurang 1 (dikurangi oleh router).
   * **Header Checksum (IPv4):** Dihitung ulang karena nilai TTL berubah.

#### Header/Elemen yang TETAP:
1. **IP Address Sumber dan Tujuan (Layer 3):** Tetap tidak berubah karena tidak ada NAT.
2. **Header Transport Layer (Layer 4):** Nomor Port Sumber/Tujuan, Sequence Number, ACK Number, dan TCP Checksum tetap.
3. **Data Aplikasi (Payload):** Tidak disentuh atau diubah oleh router biasa.

---

### 15. Perubahan Analisis Apabila Router Melakukan NAT/PAT

Jika router melakukan **NAT/PAT (Network/Port Address Translation)**:
1. **IP Address Sumber (L3):** Berubah dari IP Privat host pengirim menjadi IP Publik milik router saat keluar ke Internet.
2. **Port Number Sumber (L4):** Berubah dari port sumber asli host menjadi port baru yang dialokasikan oleh tabel translasi PAT router.
3. **Checksum:** Header Checksum IP dan Checksum L4 (TCP/UDP) **dihitung ulang** oleh router karena IP dan Port telah berubah.
4. **Dampak Analisis:** Asumsi bahwa "Header Layer 3 dan 4 selalu tetap end-to-end" menjadi **tidak berlaku**. Router tidak lagi hanya membaca Layer 3, melainkan membaca dan memodifikasi informasi Layer 3 dan Layer 4 sekaligus.

---

### 16. Hipotesis Terkait TCP Checksum Offload pada Rekaman Paket

#### Hipotesis: Fitur *TCP Checksum Offload* (Tx Checksum Offload) Aktif pada NIC Host Pengirim.

* **Penjelasan:** Ketika aplikasi *packet capture* (seperti Wireshark) merekam paket keluar pada host pengirim, ia mengambil salinan paket langsung dari tumpukan sistem operasi **sebelum** paket tersebut diserahkan ke kartu jaringan (*Network Interface Card* / NIC).
* Apabila fitur *Checksum Offload* diaktifkan, sistem operasi sengaja membiarkan field TCP Checksum bernilai salah/kosong (`0x0000`) dan menyerahkan kalkulasi matematika checksum ke perangkat keras (*hardware*) NIC.
* Akibatnya, Wireshark di host pengirim mencatat *bad checksum*, tetapi paket yang sebenarnya dipancarkan oleh NIC ke kabel fisik sudah memiliki checksum yang benar, sehingga host penerima menerima paket tanpa error dan komunikasi berjalan lancar.

---

### 17. Diagnosis Kasus "Dapat Akses via IP, Tetapi Gagal via Nama" Berdasarkan Model Lapisan

#### Hasil Diagnosis Berdasarkan Model Lapisan:

1. **Layer 1 hingga Layer 4 (Physical, Data Link, Network, Transport): SANGAT SEHAT**
   * **Bukti:** Pengguna berhasil membuka portal menggunakan alamat IP langsung. Hal ini membuktikan bahwa koneksi kabel/Wi-Fi (L1), *framing/switching* (L2), *routing* IP (L3), serta *handshake* TCP di port 80/443 (L4) berfungsi normal.
2. **Layer 7 (Application Layer): BERMASALAH pada Layanan DNS (Name Resolution)**
   * Masalah terisolasi penuh pada proses penerjemahan nama domain (FQDN) menjadi IP Address.
   * **Kemungkinan Penyebab:**
     * Alamat IP Server DNS pada konfigurasi jaringan host salah/tidak ada.
     * Port 53 (UDP/TCP) menuju server DNS terblokir oleh firewall lokal.
     * Cache DNS pada sistem operasi host terinfeksi atau korup.
     * *Record* A/AAAA untuk nama portal pada server DNS belum dikonfigurasi.

---

### 18. Enam Hipotesis Kasus "Ping Berhasil, Tetapi HTTPS Gagal" (Layer Transport hingga Application)

1. **Transport Layer (L4) — Port 443 Terblokir:** Firewall memblokir lalu lintas TCP port 443 (HTTPS), namun mengizinkan paket ICMP (ping).
2. **Transport Layer (L4) — Layanan Web Server Mati:** Aplikasi web server (Nginx/Apache) di server tujuan tidak berjalan (*not listening*) di port 443, meskipun OS server tetap merespons ICMP.
3. **Presentation/Transport Layer — Negosiasi TLS Handshake Gagal:** Terjadi ketidakcocokan versi TLS (misal server mewajibkan TLS 1.3 tetapi client hanya mendukung TLS 1.1) atau *cipher suite* tidak cocok.
4. **Presentation/Application Layer — Sertifikat TLS/SSL Tidak Valid:** Sertifikat SSL server telah kedaluwarsa, *hostname mismatch*, atau berasal dari CA yang tidak terpercaya (*Untrusted CA*), sehingga browser memutus koneksi demi keamanan.
5. **Application Layer — Pemblokiran oleh WAF (Web Application Firewall):** WAF di sisi server memblokir permintaan HTTP/HTTPS berdasarkan aturan keamanan aplikasi (misal *User-Agent* atau reputasi IP).
6. **Application Layer — Masalah Konfigurasi Virtual Host / HTTP Error 5xx:** Web server menerima koneksi TCP tetapi mengalami *Internal Server Error* (500/502/503) atau menolak *Host Header* yang dikirimkan browser.

---

### 19. Perbandingan Sesi Aplikasi dengan Koneksi TCP dan Contoh Kasusnya

#### Perbandingan:
* **Koneksi TCP (Transport Layer):** Terikat pada status jaringan ephemeral (*4-tuple*: IP Sumber, Port Sumber, IP Tujuan, Port Tujuan). Koneksi TCP akan langsung **putus** jika salah satu IP Address atau Port berubah.
* **Sesi Aplikasi (Session/Application Layer):** Terikat pada status logis/identitas pengguna (menggunakan *Session ID*, *Cookie*, atau *JSON Web Token - JWT*). Sesi aplikasi dapat **bertahan** selama token autentikasi masih valid, meskipun koneksi TCP di bawahnya berkali-kali putus atau berganti.

#### Contoh Kasus Sesi Bertahan saat Koneksi Berubah:
* **Perpindahan Jaringan Seluler / Wi-Fi pada Smartphone:**  
  Ketika pengguna sedang mengisi formulir di portal akademik menggunakan Wi-Fi kampus, kemudian berjalan keluar gedung sehingga HP berpindah ke jaringan seluler 4G/5G.
  * *Yang terjadi di Transport Layer:* IP Address HP berubah, koneksi TCP lama putus, dan koneksi TCP baru dibentuk dari IP 4G.
  * *Yang terjadi di Session Layer:* Sesi login pengguna di portal **tetap bertahan** (*logged in*) tanpa perlu mengetik ulang *username* dan *password*, karena browser/aplikasi mengirimkan kembali *Session Cookie/Token* yang sama pada koneksi TCP baru tersebut.

---

### 20. Alasan Enkripsi Tidak Dapat Selalu Ditempatkan Secara Mutlak pada Presentation Layer

Enkripsi tidak dapat ditempatkan secara mutlak pada *Presentation Layer* karena **kebutuhan perlindungan data dan batas kepercayaan (*trust boundary*) bervariasi tergantung pada lapisan mana yang ingin dilindungi**:

1. **Perlindungan Tautan Lokal (Layer 2 / MACsec):** Mengenkripsi seluruh frame Ethernet (termasuk header IP dan Port) untuk melindungi lalu lintas fisik antar-switch dari penyadapan kabel/Wi-Fi lokal.
2. **Perlindungan Jaringan / VPN (Layer 3 / IPsec):** Mengenkripsi seluruh paket IP antarnode/router untuk menyembunyikan header L4 dan payload dari jaringan perantara yang tidak terpercaya.
3. **Perlindungan Saluran Transport (Layer 4 / TLS):** Mengenkripsi aliran data antara dua *endpoint* aplikasi, tetapi header IP dan Port tetap dapat dibaca oleh router perantara untuk kebutuhan routing.
4. **Perlindungan Data Aplikasi End-to-End (Layer 7 / Application-Level Encryption):** Mengenkripsi pesan langsung di dalam aplikasi (contoh: S/MIME pada email atau *Signal Protocol* pada WhatsApp) sebelum data diserahkan ke tumpukan protokol jaringan. Dengan cara ini, bahkan server perantara (*proxy/middlebox*) tidak dapat membaca isi data.

#### Kesimpulan:
Enkripsi adalah fungsi arsitektural fleksibel. Penempatan enkripsi harus disesuaikan dengan aset apa yang dilindungi, metadata apa yang boleh terlihat di jaringan, dan di mana titik pemutusan kepercayaan (*termination point*) berada. 

---

## Level C — Evaluasi dan Sintesis

### 21. Evaluasi Pernyataan: “Model OSI tidak lagi relevan karena Internet menggunakan TCP/IP.”

Pernyataan tersebut **TIDAK TEPAT / KELIRU**. Meskipun tumpukan protokol yang diimplementasikan pada Internet secara praktis adalah TCP/IP, Model OSI tetap memiliki relevansi yang sangat tinggi.

#### Argumen Akademik:
1. **Perbedaan Model Referensi vs Spesifikasi Protokol:**
   * **OSI** adalah *reference model* (kerangka konseptual) yang dikembangkan untuk memandu standardisasi dan memisahkan fungsi komunikasi secara abstrak.
   * **TCP/IP** adalah *protocol suite* (arsitektur protokol nyata) yang tumbuh dari implementasi praktis Internet.
2. **Kegunaan Pedagogis dan Kosakata Standar Industri:**
   * Model OSI menyediakan bahasa baku industri untuk menjelaskan lokasi fungsi, jenis gangguan, dan spesifikasi perangkat. Istilah seperti *"Layer 2 Switch"*, *"Layer 3 Routing"*, *"Layer 4 Port"*, *"Layer 7 Firewall"*, *"PDU"*, serta *"Enkapsulasi"* diambil langsung dari terminologi OSI.
3. **Pemisahan Konseptual Lapisan Atas:**
   * Model OSI secara eksplisit memisahkan *Session* (Layer 5) dan *Presentation* (Layer 6). Pemisahan ini sangat membantu secara akademis untuk memahami fungsi abstrak seperti manajemen token/cookie sesi serta transformasi format data (JSON, XML, TLS, kompresi) yang pada model TCP/IP sering tersembunyi di dalam *Application Layer*.

---

### 22. Analisis Keuntungan dan Kerugian *Strict Layering* serta *Cross-Layer Information*

#### Keuntungan *Strict Layering* (Pemisahan Lapisan Ketat):
* **Modularitas dan Interoperabilitas:** Mengurangi kompleksitas desain karena setiap lapisan hanya berinteraksi dengan lapisan di atas dan di bawahnya melalui antarmuka resmi.
* **Isolasi Perubahan:** Teknologi pada satu lapisan dapat diganti (misal berpindah dari Ethernet ke Wi-Fi) tanpa perlu mengubah protokol aplikasi (seperti HTTP).
* **Kemudahan Pengujian:** Memungkinkan diagnosis dan isolasi kesalahan secara terstruktur.

#### Kerugian *Strict Layering*:
* **Overhead Pemrosesan dan Memori:** Setiap lapisan menambahkan header/trailer dan memerlukan penyalinan buffer data di memori kernel.
* **Duplikasi Fungsi:** Fungsi seperti deteksi kesalahan atau kontrol alur dapat terulang di Data Link, Transport, dan Application layer.
* **Penyembunyian Informasi Penting:** Lapisan bawah tidak dapat dengan mudah memberikan informasi kondisi jaringan secara langsung ke aplikasi.

#### Kapan *Cross-Layer Information* Membantu?
* **Aplikasi Real-Time & Mobile:** Pada aplikasi streaming video adaptif atau VoIP di jaringan nirkabel/seluler, informasi *cross-layer* (seperti RSSI, tingkat retri Wi-Fi, atau estimasi bandwidth L1/L2) dapat langsung digunakan oleh L7 untuk menyesuaikan *bitrate* video secara instan sebelum terjadi kemacetan.

#### Kapan *Cross-Layer Information* Merusak Modularitas?
* Ketika aplikasi atau protokol dirancang bergantung pada parameter spesifik media bawah (misal kode aplikasi *hardcoded* membaca header Wi-Fi/Ethernet tertentu). Hal ini membuat sistem menjadi kaku (*tightly coupled*), tidak portabel, dan rusak apabila media fisik di bawahnya diganti.

---

### 23. Prosedur Penelusuran Gangguan Video Konferensi Tersendat pada Wi-Fi Kampus Jam Sibuk

Skenario gangguan diisolasi dengan mengorelasikan bukti pada **empat lapisan**:

1. **Physical Layer (Layer 1):**
   * *Prosedur:* Mengukur tingkat sinyal radio (RSSI) dan tingkat bising (*noise floor*) di area kuliah.
   * *Bukti:* RSSI berada pada pita 2.4 GHz dengan Signal-to-Noise Ratio (SNR) yang rendah akibat interferensi frekuensi dan daya pancar Access Point (AP) tetangga.
2. **Data Link Layer (Layer 2):**
   * *Prosedur:* Memeriksa utilisasi *airtime* pada AP, jumlah *associated client*, dan tingkat retransmisi frame Wi-Fi (*frame retry rate*).
   * *Bukti:* Terjadi ketersendatan akibat *airtime contention* (CSMA/CA) dengan persentase *frame retry rate* melebihi 25% karena terlalu banyak client terhubung ke satu AP pada jam sibuk.
3. **Transport Layer (Layer 4):**
   * *Prosedur:* Merekam paket di laptop pengguna untuk menganalisis statistik *Round Trip Time* (RTT), *jitter*, dan persentase *packet loss* pada aliran datagram UDP/RTP.
   * *Bukti:* Jitter melonjak drastis dan terjadi *packet loss* berulang pada segmen UDP yang memicu keterlambatan paket audio/video.
4. **Application Layer (Layer 7):**
   * *Prosedur:* Memeriksa statistik internal aplikasi video konferensi (misal Zoom/Google Meet QoE stats).
   * *Bukti:* Algoritma *adaptive bitrate* aplikasi mendeteksi hilangnya paket, lalu secara agresif menurunkan resolusi video dan *frame rate* (FPS) hingga gambar patah-patah atau audio terputus.

---

### 24. Rancangan Skenario Laboratorium Perekaman Paket Tanpa Mengumpulkan Data Sensitif

#### A. Tujuan Skenario
Mengamati alur enkapsulasi dan tumpukan protokol lengkap dari Layer 2 hingga Layer 7 pada sesi web HTTPS terkontrol tanpa melanggar privasi atau merekam data sensitif.

#### B. Lingkungan Laboratorium
* Menggunakan mesin virtual (VM) terisolasi (*isolated virtual lab*) tanpa akses ke Internet luar.
* Server web lokal (misal Nginx) dijalankan di dalam VM untuk melayani halaman statis sederhana (`https://test.local`).

#### C. Langkah-Langkah Eksekusi
1. Jalankan aplikasi perekam paket (Wireshark) pada antarmuka virtual VM client.
2. Buka peramban web dan akses `https://test.local`.
3. Hentikan perekaman paket dan filter hasilnya menggunakan *display filter*: `ip.addr == <IP_Server_Lokal>`.

#### D. Hasil Analisis Tumpukan Protokol pada Wireshark
* **Layer 2 (Data Link):** Ethernet II Header — Mengamati MAC Address Sumber, MAC Address Tujuan, dan EtherType `0x0800` (IPv4).
* **Layer 3 (Internet):** IPv4 Header — Mengamati IP Sumber, IP Tujuan, TTL, dan Protocol ID `6` (TCP).
* **Layer 4 (Transport):** TCP Header — Mengamati Port Sumber (port dinamis), Port Tujuan (`443`), Sequence Number, ACK Number, dan Flag (`SYN`, `ACK`).
* **Layer 5/6 (Presentation/Session - TLS):** TLS Record Protocol — Mengamati proses *TLS Handshake* (*Client Hello*, *Server Hello*, Pertukaran Sertifikat, dan *Cipher Suite*).
* **Layer 7 (Application):** Enkripsi *Application Data* — Mengamati bahwa payload HTTP terenkripsi sepenuhnya dan tidak dapat dibaca dalam bentuk teks biasa.

#### E. Kontrol Etika dan Keamanan Data
* Menggunakan server web tes lokal dan sertifikat mandiri (*self-signed certificate*).
* Dilarang menginput nama, kata sandi, atau token otentikasi nyata.
* Berkas rekaman paket (`.pcapng`) dibersihkan dari metadata sebelum disimpan.

---

### 25. Urutan Header VXLAN di atas UDP dan IPsec Tunnel serta Risiko MTU

#### A. Urutan Header Paket (Dari Luar ke Dalam / Outer to Inner)

```text
[ Outer Ethernet Header ]
[ Outer IP Header (IPsec) ]
[ ESP Header (IPsec) ]
[ Outer UDP Header (Port 4789) ]
[ VXLAN Header (VNI 24-bit) ]
[ Inner Ethernet Header ]
[ Inner IP Header ]
[ Inner TCP/UDP Header ]
[ Data / Payload Aplikasi ]
[ ESP Trailer & Auth ]
[ Outer FCS ]
```

#### B. Analisis Risiko MTU (Maximum Transmission Unit)
1. **Penambahan Overhead yang Signifikan:**
   * Outer IP Header: 20 byte (IPv4)
   * ESP Header & Trailer (IPsec): ~30–50 byte (tergantung cipher)
   * Outer UDP Header: 8 byte
   * VXLAN Header: 8 byte
   * Inner Ethernet Header: 14 byte
   * Total overhead enkapsulasi bertumpuk dapat mencapai **50 hingga 100+ byte** per paket.
2. **Dampak Jika MTU Fisik Underlay Tetap 1.500 Byte:**
   * Paket internal yang berukuran 1.500 byte setelah dibungkus header overlay akan melebihi batas MTU fisik jaringan *underlay* (misal menjadi 1.580 byte).
   * **Terjadi Fragmentasi IP:** Router/VTEP harus memecah paket outer IP, yang meningkatkan beban CPU perangkat secara drastis dan memperlambat throughput.
   * **Terjadi Black Hole MTU:** Jika flag *Don't Fragment* (DF) diaktifkan pada paket IP, router perantara akan membuang paket tersebut dan mengirimkan pesan ICMP *Destination Unreachable (Fragmentation Needed)*. Jika pesan ICMP ini terblokir firewall, koneksi TCP/aplikasi akan mengalami *hang* atau putus total.
3. **Solusi Mitigasi:**
   * Konfigurasi **Jumbo Frames** pada seluruh infrastruktur underlay (misal MTU 1.600 atau 9.000 byte).
   * Konfigurasi **MSS Clamping** pada TCP untuk memaksa paket inner TCP tidak melebihi batas payload aman.

---

### 26. Perbandingan MACsec, IPsec, TLS, dan Enkripsi End-to-End Aplikasi

| Parameter | MACsec (IEEE 802.1AE) | IPsec (Tunnel/Transport) | TLS / SSL | Enkripsi End-to-End Aplikasi |
| :--- | :--- | :--- | :--- | :--- |
| **Lapisan Dominan** | Data Link (Layer 2) | Network (Layer 3) | Transport / Session (L4/L5) | Application (Layer 7) |
| **Cakupan Perlindungan** | Hop-by-hop pada satu tautan LAN kabel lokal | Network-to-Network atau Host-to-Gateway (VPN) | Host-to-Server (End-to-End Transport) | Client-to-Client (Pure End-to-End) |
| **Titik Terminasi Enkripsi** | Antarmuka fisik switch/NIC berikutnya | Router VPN / Gateway IPsec atau Host OS | Aplikasi Klien & Web Server / Load Balancer | Aplikasi Klien Pengirim & Penerima Akhir |
| **Aset yang Dilindungi** | Seluruh isi Frame L2 (termasuk Header IP & Port) | Seluruh Paket IP internal atau Payload L3 | Payload Aplikasi (Data HTTP/SMTP) | Isi Pesan/Data Spesifik Aplikasi |
| **Transparansi Perangkat Jaringan** | Terbuka di switch/router hop berikutnya | Router perantara hanya melihat Outer IP Header | Router/Switch melihat IP dan Port L4 | Seluruh jaringan & server perantara hanya melihat data terenkripsi |

---

### 27. Tantangan Firewall, Proxy, dan Load Balancer terhadap *Strict Layering*

Model klasik berasumsi bahwa perangkat jaringan bekerja secara independen pada lapisannya masing-masing (misal switch hanya di L2, router hanya di L3). Perangkat jaringan modern menantang asumsi ini:

1. **Stateful & Next-Generation Firewall (NGFW):**
   * Firewall tidak lagi hanya memeriksa alamat IP (L3) atau Port (L4). NGFW melakukan *Deep Packet Inspection* (DPI) hingga ke Layer 7 untuk mengidentifikasi aplikasi (misal membedakan lalu lintas Facebook dari web HTTPS biasa) serta mendeteksi malware di dalam payload.
2. **Proxy Aplikasi (Layer 7 Proxy):**
   * Proxy bertindak sebagai *circuit terminator*. Proxy mengakhiri koneksi TCP/TLS dari client (L4/L6), mengurai data HTTP (L7), lalu membuat koneksi TCP baru ke server tujuan. Hal ini mematahkan prinsip bahwa transport layer harus terhubung langsung *end-to-end* antar-host.
3. **Layer 7 Load Balancer (Reverse Proxy):**
   * Load balancer memeriksa header HTTP (seperti Cookie, URL Path, atau Host Header) di Layer 7 untuk mengambil keputusan penerusan (*content-based routing*), serta melakukan *TLS Termination* (mengubah HTTPS menjadi HTTP ke arah backend server).

**Kesimpulan:** Perangkat jaringan modern bersifat *cross-layer* dan memproses informasi dari beberapa lapisan sekaligus demi meningkatkan keamanan, efisiensi, dan kontrol lalu lintas.

---

### 28. Evaluasi Penempatan Fungsi Pemeriksaan Integritas Berkas Berdasarkan Prinsip End-to-End

Prinsip *end-to-end* menyatakan bahwa fungsi tertentu hanya dapat diterapkan secara lengkap dengan pengetahuan dan partisipasi sistem akhir.

#### Evaluasi Penempatan Fungsi:

1. **Penempatan pada Router (Perangkat Perantara Jaringan):**
   * *Evaluasi:* **TIDAK MEMADAI**. Router hanya memeriksa integritas per-hop/per-paket (seperti CRC/FCS atau IP Checksum). Router tidak tahu apakah berkas utuh di disk pengirim atau jika berkas mengalami korupsi di memori internal router itu sendiri sebelum dikirimkan kembali.
2. **Penempatan pada Transport Layer (TCP Checksum):**
   * *Evaluasi:* **BELUM CUKUP**. TCP Checksum hanya menjamin bahwa segmen data tidak rusak selama transit di media jaringan antara tumpukan OS pengirim dan penerima. Ia tidak melindungi data jika terjadi kerusakan berkas pada media penyimpanan (disk) atau aplikasi.
3. **Penempatan pada Application Layer (End-to-End Hash Verification):**
   * *Evaluasi:* **MUTLAK DIPERLUKAN dan SESUAI PRINSIP END-TO-END**. Hanya aplikasi pengirim dan penerima yang memiliki pengetahuan penuh tentang berkas secara utuh. Dengan menghitung nilai cryptographic hash (misal SHA-256) dari berkas sebelum dikirim dan memverifikasinya setelah berkas tersimpan di disk penerima, aplikasi menjamin bahwa berkas 100% identik dan bebas dari kerusakan di media penyimpanan, memori, maupun jaringan.

---

### 29. Potensi *Retry Storm* pada Aplikasi, Service Mesh, dan Client

#### A. Penjelasan Fenomena *Retry Storm*
*Retry Storm* terjadi ketika terjadi kemacetan atau peningkatan latensi singkat pada server backend, yang kemudian memicu mekanisme pengulangan otomatis (*retry*) secara berantai di beberapa tingkatan arsitektur sistem.

#### B. Mengapa Masalah Ini Bersifat Lintas Lapisan (*Cross-Layer*)?
Masalah ini muncul akibat **duplikasi mekanisme keandalan** yang tidak terkoordinasi antar-lapisan:
* **Layer 4 (Transport Layer):** TCP melakukan retransmisi segmen secara otomatis karena timer ACK habis akibat kemacetan jaringan.
* **Layer 4/7 (Service Mesh Proxy - misal Envoy/Istio):** Proxy mengamati respon timeout dari backend, lalu melakukan *retry* permintaan HTTP sebanyak 3 kali secara otomatis.
* **Layer 7 (Aplikasi Client / Browser):** Aplikasi pengguna tidak menerima respon tepat waktu, lalu kode JavaScript atau pengguna secara manual melakukan *refresh/retry* permintaan HTTP sebanyak 3 kali lagi.

#### C. Dampak Eksponensial (*Traffic Amplification*)
Satu permintaan asli yang tertunda memicu multiplikasi permintaan ($1 \times 3 \times 3 = 9$ kali lipat trafik tambahan). Lonjakan beban retri ini membanjiri server backend yang sedang sesak, memperburuk kemacetan jaringan, dan memicu pemadaman sistem secara berantai (*cascading failure*).

---

### 30. Argumen Pemilihan Model Pengajaran Jaringan Pemula (OSI vs TCP/IP vs Model 5-Lapisan)

#### Rekomendasi Terbaik: **Model 5-Lapisan (Hybrid Model)**

#### A. Tujuan Pembelajaran
Memberikan pemahaman konseptual yang kokoh mengenai perbedaan fungsi fisik, pengalamatan lokal, routing global, transport antarproses, dan protokol aplikasi tanpa kebingungan teori usang.

#### B. Manfaat Model 5-Lapisan (Application, Transport, Network, Data Link, Physical):
1. **Memisahkan Lapisan Akses Media:** Memisahkan *Data Link* dan *Physical* dari lapisan *Network Access* TCP/IP 4-layer. Hal ini penting agar mahasiswa dapat membedakan dengan jelas antara sinyal/kabel/gelombang (L1) dan pembentukan frame/MAC address/switching (L2).
2. **Sesuai Realitas Internet Modern:** Menggabungkan fungsi *Session*, *Presentation*, dan *Application* OSI menjadi satu *Application Layer*, yang mencerminkan cara kerja perangkat lunak dan protokol Internet saat ini.

#### C. Keterbatasan Pilihan Lain:
* **Model OSI 7-Lapisan:** Terlalu teoretis di lapisan atas. Lapisan *Session* dan *Presentation* tidak pernah diimplementasikan secara terpisah pada tumpukan protokol Internet nyata, sehingga sering membingungkan pemula.
* **Model TCP/IP 4-Lapisan:** Terlalu kasar di lapisan bawah. Menggabungkan kabel fisik, modulasi, alamat MAC, dan switch Ethernet ke dalam satu kotak *Network Access*, padahal prinsip kerja fisika dan logika di dalamnya sangat berbeda.
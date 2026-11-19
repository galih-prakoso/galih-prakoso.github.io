---
layout: post
lang: id
title: "Masalah John dan Seni Menjaga Keseimbangan Stok: Pengantar Model EOQ"
date: 2026-11-17 12:00:00 +0300
description: "Optimasi di Teknik Industri, Hari #2: bagaimana menentukan jumlah pesanan yang paling ekonomis?"
permalink: /id/tulisan/2026/masalah-john-model-eoq/
tags: optimasi eoq inventory-management teknik-industri supply-chain
categories: seri-optimasi
giscus_comments: false
related_posts: false
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=5">

<script src="{{ '/assets/js/lang-nav-id.js' | relative_url }}" defer></script>

*Seri: Optimasi di Teknik Industri, Hari #2. Topik 1.2: John's Problem, Introduction to the EOQ* · [Read in English]({{ '/blog/2026/johns-problem-eoq-inventory/' | relative_url }})

Pada pembahasan sebelumnya, kita telah melihat bagaimana prinsip optimasi sebenarnya sudah sangat akrab dengan berbagai keputusan sehari-hari. Kali ini, pembahasan berlanjut ke salah satu persoalan klasik yang paling mendasar dalam Teknik Industri dan manajemen rantai pasok, yakni pengelolaan persediaan barang (*inventory*).

Agar konsepnya mudah diikuti oleh pemula, mari simak sebuah studi kasus sederhana yang dalam literatur sering diperkenalkan sebagai **Masalah John (*John's Problem*)**.

Misalkan John adalah seorang pengelola toko ritel yang menjual produk kebutuhan harian. Berdasarkan catatan penjualan tahun-tahun sebelumnya, permintaan pelanggan terhadap produk tersebut tergolong stabil dan dapat diperkirakan setiap tahunnya. Secara sekilas, tugas John tampak sederhana: ia hanya perlu memesan barang dari pemasok (*supplier*) agar stok di toko selalu tersedia saat pelanggan datang membeli.

Namun, begitu perhitungan biaya operasional mulai dilakukan, muncul sebuah dilema yang kerap membuat para pengelola usaha ragu dalam mengambil keputusan: **berapa banyak unit barang yang sebaiknya dipesan setiap kali melakukan pemesanan?**

### Dua Pilihan Ekstrem yang Sama-Sama Merugikan

Jika berada di posisi John, setidaknya ada dua pendekatan ekstrem yang dapat ditempuh:

- **Pilihan Pertama: Memesan dalam jumlah sedikit, tetapi sangat sering.** Dengan cara ini, gudang tidak perlu menampung terlalu banyak barang. Ruang penyimpanan menjadi lebih lega, modal tidak banyak tertahan dalam bentuk stok barang, dan risiko kerusakan atau kedaluwarsa pun kecil. Akan tetapi, konsekuensinya muncul di sisi lain: setiap kali pemesanan dilakukan, toko harus menanggung biaya administrasi serta ongkos kirim (*transportasi*) yang bersifat tetap. Jika frekuensi pemesanan terlalu tinggi, total ongkos kirim dalam setahun akan membengkak.
- **Pilihan Kedua: Memesan dalam jumlah sangat besar sekaligus, tetapi jarang.** Dengan memesan stok untuk kebutuhan enam bulan atau satu tahun penuh dalam satu kali pengiriman, biaya transportasi memang dapat dihemat secara signifikan. Sebagai gantinya, diperlukan ruang gudang yang jauh lebih luas, biaya listrik, perawatan, serta asuransi penyimpanan menjadi lebih tinggi, dan dana tunai perusahaan akan mengendap lama di gudang.

Di sinilah esensi optimasi kembali terlihat nyata. Memesan terlalu sedikit membuat **biaya pemesanan** melambung, sedangkan memesan terlalu banyak membuat **biaya penyimpanan** membengkak. Tantangannya adalah menemukan titik tengah yang paling seimbang agar **total keseluruhan biaya** berada pada level paling rendah.

### Mengenal Model *Economic Order Quantity* (EOQ)

Dalam Teknik Industri, pendekatan matematis untuk menjawab dilema tersebut dikenal dengan nama model **EOQ (*Economic Order Quantity*)**. Model klasik ini pertama kali diperkenalkan oleh Ford W. Harris pada tahun 1913 dan tetap menjadi fondasi utama manajemen persediaan hingga hari ini karena logikanya yang sangat intuitif.

Untuk memahami cara kerja model ini tanpa perlu terjebak pada penurunan rumus kalkulus yang rumit, cukup kenali empat komponen dasar berikut:

1. **$$D$$ (*Annual Demand*):** Total kebutuhan atau permintaan barang selama satu tahun (dalam satuan unit).
2. **$$S$$ (*Ordering / Setup Cost*):** Biaya tetap setiap kali satu kali pemesanan dan pengiriman dilakukan, terlepas dari berapa banyak unit yang diangkut.
3. **$$H$$ (*Holding Cost*):** Biaya untuk menyimpan satu unit barang di gudang selama satu tahun penuh (mencakup sewa ruang, listrik, asuransi, dan biaya modal).
4. **$$Q$$ (*Order Quantity*):** Jumlah unit barang yang dipesan setiap kali mengisi ulang stok. Nilai $$Q$$ inilah yang berperan sebagai **variabel keputusan**.

Apabila pergerakan stok barang di gudang John diamati dari waktu ke waktu, polanya akan menyerupai **sawtooth pattern**. Saat kiriman barang datang, jumlah stok berada di titik tertinggi sebesar $$Q$$. Seiring berjalannya waktu, barang terjual secara bertahap hingga menyentuh angka $$0$$, tepat ketika kiriman berikutnya tiba. Karena stok bergerak turun secara teratur dari $$Q$$ ke $$0$$, rata-rata jumlah barang yang tersimpan di gudang setiap harinya adalah setengah dari ukuran pesanan, atau ditulis sebagai $$\frac{Q}{2}$$.

Dari logika sederhana tersebut, total biaya persediaan tahunan terdiri atas dua komponen utama yang saling tarik-menarik:

- **Biaya Pemesanan Tahunan:** Diperoleh dari frekuensi pemesanan dalam setahun ($$\frac{D}{Q}$$) dikalikan dengan biaya per satu kali pesan ($$S$$), sehingga membentuk persamaan $$\frac{D}{Q} \cdot S$$. Semakin besar nilai $$Q$$, komponen biaya ini akan **semakin turun**.
- **Biaya Penyimpanan Tahunan:** Diperoleh dari rata-rata stok di gudang ($$\frac{Q}{2}$$) dikalikan dengan biaya simpan per unit per tahun ($$H$$), sehingga membentuk persamaan $$\frac{Q}{2} \cdot H$$. Semakin besar nilai $$Q$$, komponen biaya ini justru **semakin naik**.

Ketika kedua komponen biaya tersebut digabungkan menjadi fungsi tujuan total biaya $$TC(Q) = \frac{D}{Q}S + \frac{Q}{2}H$$, akan terbentuk sebuah kurva menyerupai huruf **U**. Titik terendah pada dasar huruf U tersebut ternyata terjadi tepat pada saat **biaya pemesanan tahunan sama besar dengan biaya penyimpanan tahunan**. Secara matematis, *optimal order quantity* ($$Q^*$$) dapat langsung dihitung menggunakan rumus:

$$Q^* = \sqrt{\frac{2DS}{H}}$$

<img src="{{ '/assets/img/blog/optimization-day-2-id.svg' | relative_url }}" alt="Ilustrasi siklus persediaan sawtooth dan kurva trade-off biaya EOQ" style="max-width: 100%; height: auto; display: block; margin: 1rem auto 0.25rem;">
<p style="text-align: center;"><em>Gambar 1. Pola siklus stok sawtooth (kiri) dan titik keseimbangan kurva biaya pada model EOQ (kanan).</em></p>


### Simulasi Angka Sederhana untuk Toko John

Agar gambaran penerapannya terasa lebih nyata, mari masukkan angka operasional ke dalam studi kasus toko John:

- Permintaan tahunan ($$D$$) = 1.000 unit per tahun.
- Biaya pemesanan dan pengiriman ($$S$$) = USD 50 setiap kali pesan.
- Biaya penyimpanan ($$H$$) = USD 4 per unit per tahun.

Dengan memasukkan data tersebut ke dalam rumus EOQ, ukuran pesanan paling ekonomis bagi John dapat langsung ditemukan:

$$Q^* = \sqrt{\frac{2 \times 1000 \times 50}{4}} = \sqrt{\frac{100000}{4}} = \sqrt{25000} \approx 158 \text{ unit}$$

Tabel berikut memperlihatkan perbandingan besarnya penghematan yang diperoleh apabila John mengikuti hasil optimasi tersebut dibandingkan hanya menebak-nebak jumlah pesanan:

| Skenario Keputusan | Jumlah Pesan (Q) | Frekuensi Pesan/Tahun | Biaya Pemesanan Tahunan | Biaya Simpan Tahunan | **Total Biaya Variabel** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Terlalu sedikit (sering pesan) | 50 unit | 20 kali | USD 1.000 | USD 100 | **USD 1.100** |
| **Optimal (Model EOQ)** | **158 unit** | **≈ 6,3 kali** | **USD 316** | **USD 316** | **USD 632** |
| Terlalu banyak (jarang pesan) | 500 unit | 2 kali | USD 100 | USD 1.000 | **USD 1.100** |

Dari perbandingan angka pada tabel tersebut, terlihat sebuah temuan yang menarik. Baik saat memesan terlalu sedikit (50 unit) maupun terlalu banyak (500 unit), John sama-sama harus mengeluarkan biaya logistik dan penyimpanan sebesar USD 1.100 per tahun. Namun, dengan memesan sekitar 158 unit setiap kali pesan, total biayanya turun drastis menjadi USD 632 per tahun, sebuah penghematan lebih dari 40% hanya dengan mengatur ritme pemesanan secara tepat.

### Menjembatani Teori Klasik ke Dunia Nyata

Melalui Masalah John, kerangka pemodelan optimasi terlihat bekerja secara utuh: terdapat **variabel keputusan** berupa jumlah pesanan ($$Q$$) dan **fungsi tujuan** untuk meminimalkan total biaya persediaan.

Tentu saja, dalam dunia industri yang sesungguhnya, persoalan persediaan dapat berkembang jauh lebih menantang. Bagaimana jika pemasok menawarkan **diskon harga** apabila perusahaan bersedia membeli dalam jumlah sangat besar (*volume discounts*)? Atau bagaimana jika luas gudang memiliki **batasan kapasitas** maksimal yang tidak boleh dilanggar?

Pada kondisi yang lebih kompleks seperti itu, rumus aljabar sederhana seperti EOQ klasik sering kali tidak lagi memadai untuk langsung memberikan jawaban akhir. Di titik inilah metode pencarian numerik dan algoritma optimasi modern mulai berperan penting, topik yang akan kita bahas secara bertahap pada tulisan-tulisan berikutnya.

---

### Referensi

Cuevas, E., Rosas Caro, J. C., Alejo Reyes, A., González Ayala, P., & Rodriguez, A. (2025). *Optimization in Industrial Engineering: From Classical Methods to Modern Metaheuristics with MATLAB Applications* (Chapter 1, Section 1.2: John's Problem, Introduction to the EOQ, pp. 3–7). Springer Nature.

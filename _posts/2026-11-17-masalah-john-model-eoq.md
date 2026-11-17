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

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=2">

<script src="{{ '/assets/js/lang-nav-id.js' | relative_url }}" defer></script>

*Seri: Optimasi di Teknik Industri, Hari #2. Topik 1.2: John's Problem, Introduction to the EOQ* · [Read in English]({{ '/blog/2026/johns-problem-eoq-inventory/' | relative_url }})

<img src="{{ '/assets/img/blog/optimization-day-2-id.svg' | relative_url }}" alt="Ilustrasi siklus persediaan gigi gergaji dan kurva trade-off biaya EOQ" style="max-width: 100%; height: auto; display: block; margin: 1rem auto;">

Pada pembahasan sebelumnya, kita telah melihat bagaimana prinsip optimasi sebenarnya sudah akrab dengan keputusan kita sehari-hari. Kali ini, kita akan melangkah sedikit lebih jauh ke dalam salah satu persoalan klasik yang sangat mendasar di dunia Teknik Industri dan manajemen rantai pasok, yakni persoalan pengelolaan persediaan barang (*inventory*).

Untuk memahaminya secara perlahan dan mudah, mari kita simak sebuah kisah sederhana yang dalam literatur sering diperkenalkan sebagai **Masalah John (*John's Problem*)**.

Bayangkan John adalah seorang pengelola toko ritel yang menjual suatu produk kebutuhan harian. Dari catatan penjualan tahun-tahun sebelumnya, John mengetahui bahwa permintaan pelanggan terhadap produk tersebut tergolong stabil dan dapat diperkirakan setiap tahunnya. Tugas John sebenarnya terlihat sederhana: ia hanya perlu memesan barang dari pemasok (*supplier*) agar stok di tokonya selalu tersedia saat pelanggan datang membeli.

Namun, begitu John mulai menghitung biaya operasional, muncul sebuah dilema yang tidak jarang membuat para pengelola usaha bingung dalam mengambil keputusan: **berapa banyak unit barang yang sebaiknya dipesan setiap kali John melakukan pemesanan?**

### Dua Pilihan Ekstrem yang Sama-Sama Merugikan

Jika kita berada di posisi John, setidaknya ada dua pendekatan ekstrem yang bisa terlintas di pikiran kita:

- **Pilihan Pertama: Memesan dalam jumlah sedikit, tetapi sangat sering.** Dengan cara ini, gudang John tidak perlu menampung terlalu banyak barang. Ruang penyimpanan menjadi lega, modal tidak banyak tertahan dalam bentuk stok barang, dan risiko barang rusak atau kedaluwarsa pun kecil. Akan tetapi, konsekuensinya muncul di sisi lain: setiap kali melakukan pemesanan, John harus menanggung biaya administrasi serta biaya pengiriman (*transportasi*) yang bersifat tetap. Jika ia memesan terlalu sering, total ongkos kirim dalam setahun akan membengkak.
- **Pilihan Kedua: Memesan dalam jumlah sangat besar sekaligus, tetapi jarang.** Dengan memesan stok untuk kebutuhan enam bulan atau satu tahun penuh dalam satu kali pengiriman, John memang bisa menghemat biaya transportasi secara signifikan. Namun, sebagai gantinya, ia membutuhkan ruang gudang yang jauh lebih luas, harus membayar biaya listrik, perawatan, serta asuransi penyimpanan yang lebih tinggi, dan dana tunainya akan mengendap lama di gudang.

Di sinilah kita kembali bertemu dengan esensi optimasi yang kita bahas di hari pertama. Memesan terlalu sedikit membuat **biaya pemesanan** melambung, sedangkan memesan terlalu banyak membuat **biaya penyimpanan** membengkak. Tugas kita adalah mencari titik tengah yang paling seimbang agar **total keseluruhan biaya** berada pada level paling rendah.

### Mengenal Model *Economic Order Quantity* (EOQ)

Dalam Teknik Industri, pendekatan matematis untuk menjawab dilema John dikenal dengan nama model **EOQ (*Economic Order Quantity*)** atau Kuantitas Pesanan Ekonomis. Model klasik ini pertama kali diperkenalkan oleh Ford W. Harris pada tahun 1913 dan tetap menjadi fondasi utama dalam manajemen persediaan hingga hari ini karena kesederhanaannya yang sangat intuitif.

Untuk membangun model ini tanpa perlu terjebak pada penurunan rumus yang rumit, kita cukup mengenali empat huruf (parameter) sederhana:

1. **$$D$$ (*Annual Demand*):** Total kebutuhan atau permintaan barang selama satu tahun (dalam satuan unit).
2. **$$S$$ (*Ordering / Setup Cost*):** Biaya tetap setiap kali kita melakukan satu kali pemesanan dan pengiriman, terlepas dari berapa banyak unit yang diangkut.
3. **$$H$$ (*Holding Cost*):** Biaya untuk menyimpan satu unit barang di gudang selama satu tahun penuh (mencakup sewa ruang, listrik, asuransi, dan biaya modal).
4. **$$Q$$ (*Order Quantity*):** Jumlah unit barang yang kita pesan setiap kali melakukan pemesanan. Nilai $$Q$$ inilah yang menjadi **variabel keputusan** kita.

Jika kita perhatikan pergerakan stok barang di gudang John dari waktu ke waktu, polanya akan menyerupai **gigi gergaji (*sawtooth pattern*)**. Saat barang kiriman datang, jumlah stok di gudang berada di titik tertinggi sebesar $$Q$$. Seiring berjalannya waktu, barang terjual secara bertahap hingga stok menyentuh angka $$0$$, tepat saat kiriman berikutnya tiba. Karena stok bergerak turun secara teratur dari $$Q$$ ke $$0$$, maka rata-rata jumlah barang yang tersimpan di gudang setiap harinya adalah setengah dari ukuran pesanan, atau dapat ditulis sebagai $$\frac{Q}{2}$$.

Dari logika sederhana tersebut, total biaya persediaan tahunan yang dipengaruhi oleh keputusan kita terdiri dari dua komponen utama yang saling tarik-menarik:

- **Biaya Pemesanan Tahunan:** Diperoleh dari seberapa sering kita memesan dalam setahun ($$\frac{D}{Q}$$) dikalikan dengan biaya per satu kali pesan ($$S$$), sehingga menjadi $$\frac{D}{Q} \cdot S$$. Semakin besar nilai $$Q$$, biaya ini akan **semakin turun**.
- **Biaya Penyimpanan Tahunan:** Diperoleh dari rata-rata stok di gudang ($$\frac{Q}{2}$$) dikalikan dengan biaya simpan per unit per tahun ($$H$$), sehingga menjadi $$\frac{Q}{2} \cdot H$$. Semakin besar nilai $$Q$$, biaya ini justru **semakin naik**.

Ketika kedua kurva biaya tersebut digabungkan menjadi fungsi tujuan total biaya $$TC(Q) = \frac{D}{Q}S + \frac{Q}{2}H$$, kita akan melihat sebuah kurva berbentuk huruf **U**. Titik terendah pada dasar huruf U tersebut ternyata terjadi tepat pada saat **biaya pemesanan tahunan sama besar dengan biaya penyimpanan tahunan**. Secara matematis, kuantitas pesanan paling optimal ($$Q^*$$) dapat langsung kita hitung menggunakan rumus:

$$Q^* = \sqrt{\frac{2DS}{H}}$$

### Simulasi Angka Sederhana untuk Toko John

Agar terasa lebih nyata, mari kita masukkan angka ke dalam persoalan John. Misalkan toko John memiliki data operasional sebagai berikut:

- Permintaan tahunan ($$D$$) = 1.000 unit per tahun.
- Biaya pemesanan dan pengiriman ($$S$$) = USD 50 setiap kali pesan.
- Biaya penyimpanan ($$H$$) = USD 4 per unit per tahun.

Dengan menggunakan rumus EOQ di atas, kita dapat menemukan ukuran pesanan paling ekonomis bagi John:

$$Q^* = \sqrt{\frac{2 \times 1000 \times 50}{4}} = \sqrt{\frac{100000}{4}} = \sqrt{25000} \approx 158 \text{ unit}$$

Mari kita bandingkan seberapa besar penghematan yang didapatkan John jika ia mengikuti hasil optimasi ini dibandingkan dengan menebak-nebak jumlah pesanan:

| Skenario Keputusan | Jumlah Pesan (Q) | Frekuensi Pesan/Tahun | Biaya Pemesanan Tahunan | Biaya Simpan Tahunan | **Total Biaya Variabel** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Terlalu sedikit (sering pesan) | 50 unit | 20 kali | USD 1.000 | USD 100 | **USD 1.100** |
| **Optimal (Model EOQ)** | **158 unit** | **≈ 6,3 kali** | **USD 316** | **USD 316** | **USD 632** |
| Terlalu banyak (jarang pesan) | 500 unit | 2 kali | USD 100 | USD 1.000 | **USD 1.100** |

Dari tabel perbandingan di atas, kita bisa melihat sebuah temuan yang menarik. Jika John memesan terlalu sedikit (50 unit) atau terlalu banyak (500 unit), ia harus mengeluarkan biaya logistik dan penyimpanan sebesar USD 1.100 per tahun. Namun, dengan memesan sekitar 158 unit setiap kali pesan, total biayanya turun drastis menjadi USD 632 per tahun, sebuah penghematan lebih dari 40% hanya dengan mengatur ritme pemesanan secara tepat.

### Menjembatani Teori Klasik ke Dunia Nyata

Melalui Masalah John, kita dapat melihat secara utuh bagaimana kerangka pemodelan optimasi bekerja: kita memiliki **variabel keputusan** berupa jumlah pesanan ($$Q$$) dan **fungsi tujuan** untuk meminimalkan total biaya persediaan.

Tentu saja, di dunia industri yang sesungguhnya, persoalan John bisa berkembang menjadi jauh lebih menantang. Bagaimana jika pemasok menawarkan **diskon harga** apabila John bersedia membeli dalam jumlah sangat besar (*volume discounts*)? Atau bagaimana jika luas gudang John memiliki **batasan kapasitas** maksimal yang tidak boleh dilanggar?

Pada kondisi yang lebih kompleks seperti itu, rumus aljabar sederhana seperti EOQ klasik sering kali tidak lagi cukup untuk langsung memberikan jawaban akhir. Di titik itulah kita akan mulai membutuhkan bantuan metode pencarian numerik dan algoritma optimasi modern, yang akan kita pelajari secara bertahap pada tulisan-tulisan berikutnya.

---

### Referensi

Cuevas, E., Rosas Caro, J. C., Alejo Reyes, A., González Ayala, P., & Rodriguez, A. (2025). *Optimization in Industrial Engineering: From Classical Methods to Modern Metaheuristics with MATLAB Applications* (Chapter 1, Section 1.2: John's Problem, Introduction to the EOQ, pp. 3–7). Springer Nature.

---
layout: post
lang: id
title: "Anatomi Model Optimasi: Membedah Variabel, Tujuan, dan Batasan"
date: 2026-11-19 12:00:00 +0300
description: "Optimasi di Teknik Industri, Hari #3: bagaimana mengubah masalah nyata menjadi model matematis?"
og_image: /assets/img/blog/optimization-day-3-id.png
permalink: /id/tulisan/2026/anatomi-model-optimasi/
tags: optimasi pemodelan-matematika decision-variables teknik-industri operations-research
categories: seri-optimasi
giscus_comments: false
related_posts: false
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=14">

<script src="{{ '/assets/js/lang-switch.js' | relative_url }}?v=1" data-lang="id" defer></script>

<script src="{{ '/assets/js/img-zoom.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/post-edit.js' | relative_url }}?v=1" data-src="{{ page.path }}" defer></script>
<script src="{{ '/assets/js/series-nav.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/share-buttons.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/code-view.js' | relative_url }}?v=1" defer></script>

<script src="{{ '/assets/js/lang-nav-id.js' | relative_url }}" defer></script>

*Seri: Optimasi di Teknik Industri, Hari #3. Topik: General Formulation of an Optimization Problem* · [Read in English]({{ '/blog/2026/anatomy-of-an-optimization-model/' | relative_url }})

Setelah melihat bagaimana konsep keseimbangan biaya bekerja pada pengelolaan stok toko di pembahasan sebelumnya, muncul satu pertanyaan praktis: **bagaimana cara mengubah permasalahan di dunia nyata menjadi susunan rumus yang bisa dihitung secara sistematis?**

Dalam Teknik Industri, langkah menerjemahkan situasi lapangan ke dalam bahasa simbolik ini disebut sebagai **pemodelan matematis**. Bagi pemula, deretan huruf $$x$$, $$y$$, atau tanda pertidaksamaan di buku teks sering kali terlihat mengintimidasi. Padahal, simbol-simbol tersebut hanyalah cara singkat untuk menuliskan cerita yang sebenarnya sangat logis.

### Tiga Komponen Utama di Balik Setiap Model

Terlepas dari seberapa rumit sebuah sistem industri, mulai dari pengaturan jadwal penerbangan hingga perancangan rantai pasok global, setiap model optimasi pada dasarnya selalu tersusun dari tiga bagian yang saling terhubung: **variabel keputusan** sebagai tuas kendali, **batasan** sebagai aturan main di lapangan, dan **fungsi tujuan** sebagai target akhir yang ingin dicapai.

<img src="{{ '/assets/img/blog/optimization-day-3-id.svg' | relative_url }}" alt="Diagram anatomi model optimasi: hubungan antara variabel keputusan, batasan, dan fungsi tujuan" style="max-width: 100%; height: auto; display: block; margin: 1rem auto 0.25rem;">
<p style="text-align: center;"><em>Gambar 1. Alur kerja tiga komponen utama dalam menyusun model optimasi matematis.</em></p>

Seperti terlihat pada diagram di atas, proses pengambilan keputusan selalu bergerak dari pemilihan nilai pada variabel yang dapat diatur, lalu disaring oleh berbagai keterbatasan sumber daya, hingga menghasilkan nilai kinerja pada fungsi tujuan.

### Analogi Nyata: Menyusun Paket Usaha Katering Rumahan

Agar hubungan ketiga komponen tersebut terasa lebih membumi, sebagai contoh, seorang pengelola usaha katering rumahan sedang merencanakan produksi menu makan siang untuk besok. Dapur katering tersebut menawarkan dua pilihan menu utama: **Paket Hemat** dan **Paket Spesial**.

Setiap malam, pengelola usaha ini harus memutuskan berapa porsi masing-masing paket yang akan dimasak keesokan harinya agar keuntungan harian yang didapat bisa maksimal, tanpa melanggar keterbatasan modal dan waktu kerja di dapur. Jika cerita sederhana ini dibedah ke dalam anatomi model optimasi, susunannya menjadi sangat jelas:

1. **Variabel Keputusan (*Decision Variables*): "Apa yang Bisa Diatur?"**

   Variabel keputusan adalah besaran yang nilainya bebas ditentukan oleh pengambil keputusan. Pada kasus katering ini, hal yang bisa diatur adalah jumlah porsi yang akan diproduksi untuk setiap menu:

   - $$x_1$$ = jumlah porsi **Paket Hemat** yang dimasak.
   - $$x_2$$ = jumlah porsi **Paket Spesial** yang dimasak.

2. **Fungsi Tujuan (*Objective Function*): "Apa Target Utamanya?"**

   Fungsi tujuan merupakan ukuran keberhasilan yang ingin **dimaksimalkan** (seperti keuntungan atau efisiensi) atau **diminimalkan** (seperti biaya produksi atau waktu tunggu). Misalkan keuntungan bersih dari setiap porsi Paket Hemat adalah Rp10.000 dan Paket Spesial adalah Rp18.000. Total keuntungan harian ($$Z$$) dapat dituliskan sebagai:

   $$\max Z = 10.000x_1 + 18.000x_2$$

3. **Batasan (*Constraints*): "Apa Saja Aturan Main dan Keterbatasannya?"**

   Jika tidak ada batasan apa pun, pengelola katering tentu akan memasak jutaan porsi Paket Spesial agar keuntungannya tak terhingga. Namun di dunia nyata, selalu ada keterbatasan sumber daya yang memagari ruang gerak keputusan:

   - **Batasan modal bahan baku:** Biaya bahan baku Paket Hemat adalah Rp15.000 per porsi dan Paket Spesial Rp25.000 per porsi, sementara modal belanja harian yang tersedia maksimal Rp1.500.000:

     $$15.000x_1 + 25.000x_2 \le 1.500.000$$

   - **Batasan kapasitas waktu dapur:** Menyiapkan Paket Hemat butuh waktu 4 menit dan Paket Spesial 12 menit, sedangkan total waktu kerja efektif di dapur hanya 8 jam (480 menit):

     $$4x_1 + 12x_2 \le 480$$

   - **Batasan non-negatif (*non-negativity*):** Jumlah porsi makanan tidak mungkin bernilai negatif, sehingga secara matematis ditulis $$x_1 \ge 0$$ dan $$x_2 \ge 0$$.

### Membaca Bentuk Umum di Buku Teks dengan Mudah

Ketika membuka literatur optimasi, ketiga bagian di atas biasanya dirangkum dalam satu format baku yang ringkas:

$$\begin{aligned} \text{Optimize} \quad & f(\mathbf{x}) \\ \text{Subject to} \quad & g_i(\mathbf{x}) \le b_i, \quad i = 1, 2, \dots, m \\ & \mathbf{x} \in \mathcal{S} \end{aligned}$$

Notasi $$\mathbf{x}$$ bercetak tebal hanyalah singkatan untuk sekumpulan variabel keputusan ($$x_1, x_2, \dots, x_n$$), fungsi $$f(\mathbf{x})$$ mewakili target yang ingin dimaksimalkan atau diminimalkan, sedangkan $$g_i(\mathbf{x}) \le b_i$$ adalah daftar seluruh aturan batas yang wajib dipatuhi. Sementara itu, $$\mathcal{S}$$ menunjukkan *feasible region*, yakni seluruh kombinasi angka yang tidak melanggar satu pun aturan batasan.

Dengan memahami anatomi dasar ini, setiap persoalan optimasi, sekompleks apa pun bentuknya, dapat selalu dikenali polanya. Pada contoh katering di atas, semua persamaan kebetulan berbentuk perkalian angka sederhana tanpa pangkat atau lengkungan. Namun di lapangan, hubungan antarvariabel sering kali tidak sesederhana garis lurus. Perbedaan karakteristik inilah yang akan kita bahas pada pertemuan berikutnya mengenai masalah **Linear vs. Non-Linear**.

---

### Script Python

Model katering pada tulisan ini dapat diselesaikan dan digambar dengan script Python berikut. Script ini mencari seluruh titik sudut *feasible region*, mencetak tabel keuntungan harian di setiap titik, menunjukkan batasan mana yang aktif (*binding*) pada solusi optimum, lalu menggambar *feasible region* beserta garis keuntungan terbaik. Jalankan dengan `--idr` untuk memakai angka rupiah seperti pada tulisan ini. Script memerlukan Python 3.9+ dengan `numpy` dan `matplotlib`. Script memuat pernyataan hak cipta penulis (© 2026 Galih Prakoso, lisensi MIT) yang wajib dipertahankan pada setiap salinan atau modifikasi.

<div class="code-view" data-src="{{ '/assets/code/day-3-catering-model.py' | relative_url }}"><a href="{{ '/assets/code/day-3-catering-model.py' | relative_url }}">day-3-catering-model.py</a></div>

---

### Referensi

Cuevas, E., Rosas Caro, J. C., Alejo Reyes, A., González Ayala, P., & Rodriguez, A. (2025). *Optimization in Industrial Engineering: From Classical Methods to Modern Metaheuristics with MATLAB Applications* (Chapter 1, Section 1.1: What and Where Do We Optimize, pp. 2–3). Springer Nature.

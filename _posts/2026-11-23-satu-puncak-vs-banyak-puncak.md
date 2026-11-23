---
layout: post
lang: id
title: "Satu Puncak atau Banyak Puncak? Mengenal Masalah Unimodal dan Multimodal"
date: 2026-11-23 12:00:00 +0300
description: "Optimasi di Teknik Industri, Hari #5: mengapa jumlah puncak pada fungsi tujuan menentukan apakah metode sederhana cukup atau tidak?"
og_image: /assets/img/blog/optimization-day-5-id.png
permalink: /id/tulisan/2026/satu-puncak-vs-banyak-puncak/
tags: optimasi unimodal multimodal local-optimum teknik-industri
categories: seri-optimasi
giscus_comments: false
related_posts: false
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=16">

<script src="{{ '/assets/js/lang-switch.js' | relative_url }}?v=1" data-lang="id" defer></script>

<script src="{{ '/assets/js/img-zoom.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/post-edit.js' | relative_url }}?v=1" data-src="{{ page.path }}" defer></script>
<script src="{{ '/assets/js/series-nav.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/share-buttons.js' | relative_url }}?v=3" defer></script>
<script src="{{ '/assets/js/code-view.js' | relative_url }}?v=1" defer></script>

<script src="{{ '/assets/js/lang-nav-id.js' | relative_url }}" defer></script>
<script src="{{ '/assets/js/tag-links.js' | relative_url }}?v=1" defer></script>

*Seri: Optimasi di Teknik Industri, Hari #5. Topik: Modality (Unimodal vs. Multimodal)* · [Read in English]({{ '/blog/2026/unimodal-vs-multimodal/' | relative_url }})

Pembahasan sebelumnya menunjukkan bahwa lanskap nilai fungsi tujuan bisa bergelombang ketika hubungan antarvariabel berbentuk kurva. Pertanyaan berikutnya yang lebih spesifik: **berapa banyak puncak (atau lembah) yang ada di lanskap tersebut?** Jawaban atas pertanyaan ini akan menentukan apakah metode sederhana sudah cukup, atau kita perlu alat yang lebih cerdik.

---

### Mendaki Satu Bukit vs. Menjelajah Pegunungan

Misalkan seorang pendaki diminta untuk mencapai puncak, tetapi kabut tebal menyebabkan pendaki hanya bisa melihat tanah tepat di bawah kakinya. Strategi sederhana yang bisa dia lakukan adalah selalu melangkah ke arah yang menanjak, dan berhenti ketika tidak ada lagi arah yang lebih tinggi.

- Jika mendaki **bukit tunggal**, strategi ini selalu berhasil. Dari sisi mana pun pendaki memulai, setiap tanjakan akan membawa pendaki ke satu-satunya puncak, yang pasti merupakan puncak tertinggi.
- Jika mendaki **pegunungan dengan puncak yang banyak**, strategi yang sama bisa menipu. Pendaki bisa berhenti di puncak bukit kecil karena di sekitarnya semua arah menurun, padahal puncak yang jauh lebih tinggi berada di balik lembah berikutnya.

Strategi "selalu menanjak" ini persis dengan cara kerja metode gradien (*gradient ascent* untuk maksimasi, *gradient descent* untuk minimasi). Di setiap titik, metode ini menghitung arah tanjakan paling curam, lalu melangkah ke arah tersebut. Metode ini sempat disinggung pada Hari #4.

---

### Definisi: Unimodal dan Multimodal

Dalam optimasi, sebuah masalah disebut **multimodal** bila fungsi tujuannya memiliki lebih dari satu solusi optimal lokal (*local optima*). Yang terbaik di antara semuanya didefinisikan dengan **global optimum**. Sebaliknya, masalah **unimodal** hanya memiliki satu puncak (untuk maksimasi) atau satu lembah (untuk minimasi), sehingga optimum lokal sekaligus menjadi optimum global.

Buku rujukan seri ini menghubungkan unimodal dengan fungsi yang **convex**. Hubungan tersebut perlu dibaca dengan hati-hati: fungsi convex memang selalu unimodal, tetapi tidak semua fungsi unimodal itu convex. Sebuah kurva bisa memiliki satu puncak namun bentuknya tidak seperti mangkuk yang mulus. Perbedaan convex dan non-convex akan dibahas tersendiri pada ulasan berikutnya.

<img src="{{ '/assets/img/blog/optimization-day-5-id.svg' | relative_url }}" alt="Perbandingan lanskap unimodal dengan satu puncak dan lanskap multimodal dengan puncak lokal yang menjebak metode gradien" style="max-width: 100%; height: auto; display: block; margin: 1rem auto 0.25rem;">
<p style="text-align: center;"><em>Gambar 1. Lanskap unimodal: setiap jalur menanjak berakhir di puncak yang sama (kiri). Lanskap multimodal: hasil pencarian bergantung pada titik awal, dan pendaki bisa berhenti di puncak lokal (kanan).</em></p>

---

### Contoh Nyata: Fungsi Peaks

Buku rujukan memakai fungsi **Peaks**, fungsi dua variabel yang sering dipakai untuk menguji algoritma optimasi. Fungsi ini memiliki tiga puncak di dalam rentang $$-3 \le x_1, x_2 \le 3$$. Hasil perhitungan numerik untuk tulisan ini:

| Puncak | Lokasi $$(x_1, x_2)$$ | Tinggi $$f(x_1, x_2)$$ |
| :--- | :--- | :--- |
| Global optimum | $$(-0{,}009;\ 1{,}581)$$ | 8,11 |
| Local optimum 1 | $$(-0{,}460;\ -0{,}629)$$ | 3,78 |
| Local optimum 2 | $$(1{,}286;\ -0{,}005)$$ | 3,59 |

Mengikuti gagasan buku tentang menjalankan metode gradien dari titik awal yang berbeda, kita coba dua titik pada fungsi Peaks (dihitung dengan script di akhir tulisan ini). Dari titik $$(-1, 1)$$, pencarian berhasil mencapai puncak tertinggi. Dari titik $$(0, 0)$$, pencarian justru berhenti di puncak lokal, yang tingginya kurang dari separuh puncak global. Algoritmanya sama, fungsinya sama, hanya titik awalnya yang berbeda. Inilah ciri khas masalah multimodal: **hasil metode lokal bergantung pada titik awal pencarian.**

---

### Di Mana Multimodalitas Muncul di Teknik Industri?

Masalah multimodal tidak hanya muncul pada fungsi uji matematika. Buku rujukan mencatat bahwa model **EOQ** (*Economic Order Quantity*) yang kita bahas pada Hari #2 berubah menjadi multimodal ketika pemasok memberi **potongan harga berdasarkan volume** (*volume discounts*). Kurva biaya total tidak lagi mulus dengan satu lembah, melainkan patah di setiap batas jumlah pesanan yang mendapat harga baru, sehingga muncul beberapa lembah. Metode gradien yang mulai di dekat satu lembah bisa berhenti di lembah tersebut dan melewatkan jumlah pesanan yang sebenarnya lebih murah.

Contoh lain yang sering dijumpai adalah masalah kombinatorial seperti penjadwalan produksi atau penataan komponen di atas mesin. Pada kasus tersebut, menukar urutan dua pekerjaan bisa menaikkan atau menurunkan biaya secara tidak teratur, sehingga lanskap masalahnya penuh dengan "bukit kecil".

---

### Dimensi Menambah Tingkat Kesulitan

Selain jumlah puncak, buku rujukan juga menyoroti **dimensi**, yaitu jumlah variabel keputusan yang independen. Masalah EOQ John hanya punya satu variabel (jumlah pesanan $$Q$$), sedangkan fungsi Peaks punya dua. Ketika satu pemasok tidak mampu memenuhi seluruh permintaan sehingga pesanan harus dibagi ke beberapa pemasok, jumlah variabel bertambah. Semakin banyak dimensi, semakin luas ruang pencarian yang harus dijelajahi. Fenomena ini dikenal sebagai *curse of dimensionality*. Gabungan multimodal dan berdimensi tinggi adalah jenis masalah yang paling sulit bagi metode klasik.

---

### Lalu, Metode Apa yang Cocok?

| Jenis Masalah | Metode yang Masuk Akal | Catatan |
| :--- | :--- | :--- |
| Unimodal | Metode gradien (*gradient descent/ascent*) | Cepat dan andal, titik awal tidak terlalu berpengaruh. |
| Multimodal, dimensi rendah | Metode gradien dari banyak titik awal (*multi-start*) | Membantu, tetapi tidak menjamin global optimum. |
| Multimodal, dimensi tinggi | Metaheuristik: *Simulated Annealing*, *Particle Swarm Optimization*, algoritma evolusioner | Tidak menjamin optimum, tetapi jauh lebih jarang terjebak di puncak lokal. |

Buku rujukan menunjukkan bahwa metode berbasis probabilitas, seperti *random search* dan *Particle Swarm Optimization*, mampu menemukan puncak tertinggi fungsi Peaks tanpa bergantung pada titik awal. Metode-metode ini akan kita bahas satu per satu pada bagian akhir seri.

Sebelum memilih algoritma, mulailah dengan pertanyaan sederhana: apakah lanskap masalah ini kemungkinan hanya punya satu puncak, atau banyak? Jawaban atas pertanyaan tersebut sering kali sudah menentukan separuh keberhasilan.

---

### Script Python

Tabel puncak pada tulisan ini dapat direproduksi dengan script Python berikut. Script juga menjalankan gradient ascent sederhana dari beberapa titik awal dan menggambar hasilnya pada peta kontur. Dibutuhkan Python 3.9+ dengan `numpy` dan `matplotlib`. Script memuat pernyataan hak cipta penulis (© 2026 Galih Prakoso, MIT License) yang harus tetap disertakan pada setiap salinan atau modifikasi.

<div class="code-view" data-src="{{ '/assets/code/day-5-peaks.py' | relative_url }}"><a href="{{ '/assets/code/day-5-peaks.py' | relative_url }}">day-5-peaks.py</a></div>

---

### Referensi

Cuevas, E., Rosas Caro, J. C., Alejo Reyes, A., González Ayala, P., & Rodriguez, A. (2025). *Optimization in Industrial Engineering: From Classical Methods to Modern Metaheuristics with MATLAB Applications* (Chapter 2, Section 2.8: Modality and Dimensionality, pp. 39–41; Chapter 3, Section 3.4: Maximizing the Peaks Function, pp. 55–62). Springer Nature.

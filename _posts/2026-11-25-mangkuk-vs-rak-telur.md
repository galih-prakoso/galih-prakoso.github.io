---
layout: post
lang: id
title: "Mangkuk atau Rak Telur? Mengenal Masalah Convex dan Non-Convex"
date: 2026-11-25 12:00:00 +0300
description: "Optimasi di Teknik Industri, Hari #6: mengapa sifat convex membuat kita bisa memercayai optimum lokal sebagai optimum global."
og_image: /assets/img/blog/optimization-day-6-id.png
permalink: /id/tulisan/2026/convex-vs-non-convex/
tags: optimasi convex non-convex optimum-lokal teknik-industri
categories: seri-optimasi
giscus_comments: false
related_posts: false
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=16">

<script src="{{ '/assets/js/lang-switch.js' | relative_url }}?v=1" data-lang="id" defer></script>

<script src="{{ '/assets/js/img-zoom.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/post-edit.js' | relative_url }}?v=1" data-src="{{ page.path }}" defer></script>
<script src="{{ '/assets/js/series-nav.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/share-buttons.js' | relative_url }}?v=4" defer></script>
<script src="{{ '/assets/js/code-view.js' | relative_url }}?v=1" defer></script>

<script src="{{ '/assets/js/lang-nav-id.js' | relative_url }}" defer></script>
<script src="{{ '/assets/js/tag-links.js' | relative_url }}?v=1" defer></script>

*Seri: Optimasi di Teknik Industri, Hari #6. Topik: Convexity (Convex vs. Non-Convex)* · [Read in English]({{ '/blog/2026/convex-vs-non-convex/' | relative_url }})

Pada ulasan sebelumnya ([Hari #5]({{ '/id/tulisan/2026/satu-puncak-vs-banyak-puncak/' | relative_url }})), dapat kita lihat bahwa sebuah fungsi tujuan bisa memiliki banyak titik maksimum atau titik minimum lokal. Pertanyaan berikutnya: **apakah ada ciri-ciri yang dapat diidentifikasi sejak awal untuk memastikan suatu kurva hanya ada satu titik minimum?** Sifat atau ciri-ciri tersebut disebut sifat **convexity**. Hasil pemeriksaan tersebut menentukan apakah sebuah masalah optimasi bisa diselesaikan dengan pasti, atau harus ditangani dengan hati-hati.

---

### Kelereng di Mangkuk vs. Kelereng di Rak Telur

Misalkan sebuah kelereng dijatuhkan ke dalam mangkuk yang mulus. Pada posisi mana pun kelereng mendarat, kelereng akan menggelinding turun dan berhenti di dasar mangkuk. Tidak ada tempat lain untuk berhenti.

Sekarang kelereng yang sama dijatuhkan ke rak telur. Kelereng akan berhenti di cekungan terdekat dari tempat mendarat, padahal cekungan yang lebih dalam bisa berada beberapa sentimeter di sebelahnya.

Mangkuk adalah gambaran masalah **convex** (untuk minimasi), sedangkan rak telur adalah masalah **non-convex**. Kelereng yang menggelinding berperilaku seperti metode gradien: kelereng hanya tahu kemiringan tepat di bawahnya.

---

### Fungsi Convex

Menurut Hillier dan Lieberman, sebuah fungsi $$f(x)$$ disebut **convex** jika ruas garis yang menghubungkan dua titik mana pun pada grafiknya (disebut *chord*) berada **pada atau di atas** grafik tersebut. Dengan kata lain, kurva convex hanya melengkung ke atas, seperti mangkuk. Untuk fungsi yang memiliki turunan kedua, ada uji cepat:

| Syarat (untuk semua $$x$$) | Status $$f(x)$$ |
| :--- | :--- |
| $$f''(x) \ge 0$$ | Convex (melengkung ke atas atau tidak melengkung) |
| $$f''(x) \le 0$$ | Concave (melengkung ke bawah atau tidak melengkung) |
| Tanda $$f''(x)$$ berubah-ubah | Bukan convex dan bukan concave |

Fungsi linear memiliki $$f''(x) = 0$$ di semua titik, sehingga memenuhi kedua syarat pada tabel tersebut. Artinya, fungsi linear termasuk convex sekaligus concave: *chord*-nya tepat berimpit dengan garis fungsinya.

Fungsi convex juga memiliki dua sifat yang berguna dalam praktik. Pertama, **jumlah dari fungsi-fungsi convex juga convex**, sehingga total biaya yang tersusun dari beberapa komponen biaya convex tetap convex. Kedua, untuk maksimasi kita mencari fungsi tujuan yang **concave**, karena negatif dari fungsi convex adalah fungsi concave.

<img src="{{ '/assets/img/blog/optimization-day-6-id.svg' | relative_url }}" alt="Perbandingan mangkuk convex tempat setiap titik awal mencapai titik minimum yang sama dan kurva non-convex bergelombang tempat titik awal menentukan titik minimum yang dicapai" style="max-width: 100%; height: auto; display: block; margin: 1rem auto 0.25rem;">
<p style="text-align: center;"><em>Gambar 1. Fungsi convex: setiap titik awal menggelinding ke titik minimum yang sama, dan setiap chord berada di atas kurva (kiri). Fungsi non-convex: chord bisa memotong di bawah kurva, dan kelereng berhenti di cekungan terdekat (kanan).</em></p>

---

### Jika Ada Kendala, Maka Area Feasible Harus Convex

Sejauh ini kita hanya membahas fungsi tujuan. Padahal sebagian besar masalah industri memiliki kendala, dan kendala tersebut membentuk **area feasible** (*feasible region*), yaitu kumpulan semua keputusan yang boleh dipilih. Agar jaminan convex berlaku, area ini juga harus berupa **himpunan convex** (*convex set*): jika kita memilih dua keputusan feasible mana pun, semua keputusan di antara keduanya juga harus feasible. Area yang memiliki lekukan ke dalam tidak lolos uji ini, karena dua titik di tepi lekukan tersebut dihubungkan oleh garis yang sebagian keluar dari area. Ada dua fakta yang perlu diingat:

- Area feasible dari **setiap masalah linear programming adalah himpunan convex**. Inilah salah satu alasan masalah LP relatif mudah diselesaikan dengan hasil yang bisa dipercaya.
- Pada masalah non-linear dengan kendala $$g_i(x) \le b_i$$, area feasible merupakan himpunan convex apabila setiap $$g_i(x)$$ adalah fungsi convex.

Masalah yang fungsi tujuannya convex (untuk minimasi) dan area feasible-nya convex disebut **convex programming problem**. Pada golongan masalah convex programming ini, syarat optimalitas Kuhn–Tucker bukan hanya syarat perlu, tetapi juga syarat cukup untuk minimum global (Rao). Artinya, tidak ada minimum relatif atau *saddle point* yang bisa menjebak pencarian.

---

### Contoh: Jika Area Feasible Berupa Lengkungan (Kurva)

Hillier dan Lieberman memodifikasi masalah dua produk klasik mereka menjadi seperti berikut. Tujuannya memaksimalkan $$Z = 3x_1 + 5x_2$$ dengan kendala:

- $$x_1 \le 4$$
- $$2x_2 \le 14$$
- $$8x_1 - x_1^2 + 14x_2 - x_2^2 \le 49$$ (non-linear)
- $$x_1, x_2 \ge 0$$

Kendala non-linear tersebut membuat area feasible tidak lagi convex. Sebagai uji, ambil dua titik feasible, yaitu $$(0, 7)$$ dan $$(4, 3)$$. Titik tengah keduanya adalah $$(2, 5)$$, dan titik ini melanggar kendala karena $$8(2) - 2^2 + 14(5) - 5^2 = 57 > 49$$, sehingga berada di luar area feasible.

Akibatnya, masalah ini memiliki **dua titik maksimum lokal**:

| Titik $$(x_1, x_2)$$ | $$Z = 3x_1 + 5x_2$$ | Status |
| :--- | :--- | :--- |
| $$(0,\ 7)$$ | 35 | Maksimum global |
| $$(4,\ 3)$$ | 27 | Hanya maksimum lokal |

Fungsi tujuannya linear, jadi sangat sederhana, tetapi satu kendala yang berupa lengkungan sudah cukup untuk menciptakan jebakan. Pencarian lokal yang tiba di $$(4, 3)$$ tidak menemukan solusi terdekat (*neighbor*) yang lebih baik lalu berhenti, padahal Z masih kurang 8 dari jawaban terbaik.

---

### Pada Kondisi Seperti Apa Masalah Ini Muncul di Teknik Industri

Model dasar **EOQ** pada [Hari #2]({{ '/id/tulisan/2026/masalah-john-model-eoq/' | relative_url }}) adalah contoh convex yang baik. Total biayanya berupa kurva convex dengan satu titik minimum, sehingga gradient descent menemukan jumlah pesanan terbaik dari titik awal mana pun. Begitu diskon volume ditambahkan (seperti pada [Hari #5]({{ '/id/tulisan/2026/satu-puncak-vs-banyak-puncak/' | relative_url }})), kurva biaya patah dan sifat convex hilang. Script di akhir tulisan ini menguji kedua kasus tersebut dengan uji *chord* (angka diskonnya hanya ilustrasi).

Sumber non-convexity lain yang sering muncul dalam masalah industri adalah biaya setup tetap, skala ekonomi, keputusan bilangan bulat (2,4 truk bukan pilihan yang mungkin), dan keputusan yang bergantung pada urutan, seperti urutan pekerjaan di sebuah mesin.

---

### Lalu Apa Gunanya?

| | Masalah convex | Masalah non-convex |
| :--- | :--- | :--- |
| Optimum lokal | Selalu optimum global | Bisa hanya lokal |
| Titik awal | Hampir tidak berpengaruh | Bisa menentukan hasil |
| Metode umum | Metode gradien, syarat KKT, solver LP | Multi-start, branch-and-bound, metaheuristik |
| Bukti optimalitas | Tersedia | Umumnya tidak ada, atau sangat mahal |

Pada kondisi sebenarnya, sering kali sulit memastikan apakah seluruh fungsi tujuan dan kendala bersifat convex. Pendekatan yang terbaik adalah dengan membiasakan memeriksa setiap komponen penyusunnya, yaitu setiap suku biaya dan setiap kendala. Jika semuanya convex, seluruh masalah juga convex dan metode sederhana bisa digunakan. Jika satu saja melengkung ke arah yang salah, perlakukan jawaban metode lokal sebagai alternatif kandidat penyelesaian, bukan kepastian.

---

### Script Python

Uji *chord* dan contoh Hillier dan Lieberman pada tulisan ini dapat direproduksi dengan script Python berikut. Script mencetak tabel hasil uji untuk tiga fungsi satu variabel (termasuk EOQ), mencari titik maksimum lokal pada contoh dua produk, dan menggambar keduanya. Dibutuhkan Python 3.9+ dengan `numpy` dan `matplotlib`. Script memuat pernyataan hak cipta penulis (© 2026 Galih Prakoso, MIT License) yang harus tetap disertakan pada setiap salinan atau modifikasi.

<div class="code-view" data-src="{{ '/assets/code/day-6-convexity.py' | relative_url }}"><a href="{{ '/assets/code/day-6-convexity.py' | relative_url }}">day-6-convexity.py</a></div>

---

### Referensi

Cuevas, E., Rosas Caro, J. C., Alejo Reyes, A., González Ayala, P., & Rodriguez, A. (2025). *Optimization in Industrial Engineering: From Classical Methods to Modern Metaheuristics with MATLAB Applications* (Chapter 1, Section 1.1: What and Where Do We Optimize, p. 3; Chapter 2, Section 2.5: Plotting Partial Costs and the Total Cost, p. 28). Springer Nature.

Hillier, F. S., & Lieberman, G. J. (2010). *Introduction to Operations Research* (9th ed.; Chapter 12, Section 12.2: Graphical Illustration of Nonlinear Programming Problems, pp. 542–547; Appendix 2: Convexity, pp. 993–996). McGraw-Hill.

Rao, S. S. (2009). *Engineering Optimization: Theory and Practice* (4th ed.; Chapter 2, Section 2.6: Convex Programming Problem, p. 104). John Wiley & Sons.

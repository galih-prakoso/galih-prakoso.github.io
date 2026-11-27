---
layout: post
lang: id
title: "Bulat atau Pecahan? Mengenal Integer Programming"
date: 2026-11-27 12:00:00 +0300
description: "Optimasi di Teknik Industri, Hari #7: mengapa pembulatan jawaban LP dapat melebihi batasan sumber daya atau jauh dari optimum."
og_image: /assets/img/blog/optimization-day-7-id.png
permalink: /id/tulisan/2026/integer-programming/
tags: optimasi integer-programming branch-and-bound lp-relaxation teknik-industri
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

*Seri: Optimasi di Teknik Industri, Hari #7. Topik: Integer Programming* · [Read in English]({{ '/blog/2026/integer-programming/' | relative_url }})

Pada ulasan sebelumnya ([Hari #6]({{ '/id/tulisan/2026/convex-vs-non-convex/' | relative_url }})), kita membahas kapan sebuah masalah aman diselesaikan dengan metode lokal. Kali ini kita melihat hambatan yang berbeda: **variabel keputusan yang harus berupa bilangan bulat**. Suatu pengrajin mebel tidak bisa membuat 2,25 lemari, dan sebuah pabrik tidak bisa membeli 3,75 mesin. Masalah seperti ini disebut **Integer Programming (IP)**.

### Apa Itu Integer Programming?

IP adalah masalah linear programming dengan tambahan syarat bahwa sebagian atau seluruh variabel harus bernilai bilangan bulat. Ada tiga bentuk yang sering ditemui:

| Bentuk | Aturan variabel | Contoh keputusan |
| :--- | :--- | :--- |
| Pure IP | Semua variabel bilangan bulat | Jumlah mesin yang dibeli |
| Mixed IP | Sebagian bulat, sebagian boleh pecahan | Jumlah truk (bulat) dan liter bahan bakar (pecahan) |
| Binary IP | Variabel hanya bernilai 0 atau 1 | Membangun pabrik di kota tertentu atau tidak |

Model katering pada [Hari #3]({{ '/id/tulisan/2026/anatomi-model-optimasi/' | relative_url }}) juga memakai variabel bulat (jumlah porsi), dan optimumnya kebetulan jatuh di titik bulat $$(75,\ 15)$$. Hal itu tidak selalu terjadi, seperti terlihat pada contoh berikut.

### Contoh: Pengrajin Furnitur

Misalkan suatu usaha pengrajin furniture membuat dua produk. Setiap lemari (x₁) memberi keuntungan Rp5 juta dan setiap meja (x₂) memberi Rp8 juta. Usaha tersebut memiliki 6 pekerja dan 45 lembar papan. Setiap produk menghabiskan 1 pekerja. Setiap lemari memakai 5 lembar papan, dan setiap meja memakai 9 lembar. Model ini bisa ditulis sebagai berikut:

$$\max\; Z = 5x_1 + 8x_2 \quad \text{dengan}\quad x_1 + x_2 \le 6,\;\; 5x_1 + 9x_2 \le 45,\;\; x_1, x_2 \ge 0\text{ dan bulat}$$

Jika syarat bulat dihapus, LP memberi optimum pada sudut $$(2{,}25;\ 3{,}75)$$ dengan $$Z = 41{,}25$$. Jawaban tersebut tidak bisa dikerjakan. Lalu bagaimana jika dibulatkan?

<img src="{{ '/assets/img/blog/optimization-day-7-id.svg' | relative_url }}" alt="Perbandingan optimum LP yang pecahan dengan titik-titik bulat pada area feasible usaha pengrajin furnitur" style="max-width: 100%; height: auto; display: block; margin: 1rem auto 0.25rem;">
<p style="text-align: center;"><em>Gambar 1. Kiri: LP mencapai sudut area feasible. Kanan: hanya titik bulat yang boleh dipilih.</em></p>

| Cara | Titik | Status | Z |
| :--- | :--- | :--- | ---: |
| Dibulatkan ke terdekat | (2, 4) | Melebihi batas papan (5·2 + 9·4 = 46 > 45) | - |
| Dibulatkan ke bawah | (2, 3) | Feasible | 34 |
| Optimum bulat sebenarnya | (0, 5) | Feasible | 40 |

Pembulatan ke terdekat menghasilkan jawaban yang tidak feasible, dan pembulatan ke bawah menyisakan Z = 34, padahal Z = 40 bisa dicapai. Optimum bulat bahkan berada di titik yang jauh dari optimum LP. Karena itu, **membulatkan jawaban LP bukan metode yang bisa diandalkan**.

Hillier dan Lieberman menyebut dua jebakan ini: jawaban LP yang dibulatkan belum tentu feasible, dan jika pun feasible, belum tentu optimum. Pembulatan masih cukup baik pada masalah satu variabel yang mulus, seperti kasus John pada Cuevas dkk. ketika 44,72 galon dibulatkan menjadi 45. Pada masalah dengan beberapa variabel dan kendala, aturan tersebut tidak bisa dipercaya.

### Cara Menemukan Optimum Bulat: Branch and Bound

Metode yang paling umum adalah **branch and bound**. Idenya sederhana:

1. Selesaikan LP tanpa syarat bulat (disebut **LP relaxation**). Nilainya menjadi batas atas: jawaban bulat tidak mungkin lebih baik dari 41,25.
2. Jika ada variabel pecahan, misalnya x₁ = 2,25, bagi masalah menjadi dua cabang: x₁ ≤ 2 dan x₁ ≥ 3. Tidak ada titik bulat yang hilang karena tidak ada bilangan bulat di antara 2 dan 3.
3. Selesaikan LP pada setiap cabang, lalu ulangi pembagian.
4. Setiap kali ditemukan jawaban bulat, simpan sebagai yang terbaik sementara. Cabang yang batas LP-nya tidak lebih baik dari jawaban tersebut dihentikan (di-*prune*).

Pada contoh ini, script Python menyelesaikannya dalam 9 simpul. Jawaban bulat pertama (2, 3) bernilai 34, kemudian muncul (1, 4) bernilai 37, dan akhirnya (0, 5) bernilai 40. Cabang x₁ ≥ 3 dihentikan karena batas LP-nya hanya 39.

### Di Mana Ini Muncul dalam Teknik Industri?

Keputusan yang menggunakan bilangan bulat sangat umum di industri: jumlah mesin, jumlah operator, lokasi fasilitas (ya atau tidak), urutan pekerjaan, dan ukuran lot produksi. Sebagian di antaranya termasuk sumber sifat non-convex yang disebut pada [Hari #6]({{ '/id/tulisan/2026/convex-vs-non-convex/' | relative_url }}), karena kumpulan titik bulat bukan himpunan convex. Akibatnya, IP umumnya jauh lebih sulit diselesaikan daripada LP dengan ukuran yang sama. Kesulitan tersebut menjadi salah satu alasan metode metaheuristik dibahas pada seri berikutnya.

### Lalu Apa Gunanya?

Ada tiga pelajaran praktis. Pertama, selalu periksa apakah variabel keputusan harus berupa bilangan bulat sebelum memercayai jawaban LP. Kedua, nilai LP relaxation tetap berguna sebagai batas: selisih antara 41,25 dan 40 memberi tahu seberapa jauh jawaban bulat dari batas terbaik. Ketiga, jangan membulatkan jawaban begitu saja. Gunakan solver IP atau branch and bound agar jawabannya terjamin feasible dan optimum.

---

### Script Python

Contoh pengrajin furnitur pada tulisan ini dapat direproduksi dengan script Python berikut. Script mencetak LP relaxation, hasil pembulatan, optimum bulat hasil pencarian menyeluruh, dan seluruh simpul branch and bound, lalu menggambar titik-titik bulat. Dibutuhkan Python 3.9+ dengan `numpy`, `scipy`, dan `matplotlib`. Script memuat pernyataan hak cipta penulis (© 2026 Galih Prakoso, MIT License) yang harus tetap disertakan pada setiap salinan atau modifikasi.

<div class="code-view" data-src="{{ '/assets/code/day-7-integer-programming.py' | relative_url }}"><a href="{{ '/assets/code/day-7-integer-programming.py' | relative_url }}">day-7-integer-programming.py</a></div>

---

### Referensi

Cuevas, E., Rosas Caro, J. C., Alejo Reyes, A., González Ayala, P., & Rodriguez, A. (2025). *Optimization in Industrial Engineering: From Classical Methods to Modern Metaheuristics with MATLAB Applications* (Chapter 1, Section 1.4: Solving John's Problem Using the Gradient Descent Method with Matlab, pp. 10 dan 12). Springer Nature.

Hillier, F. S., & Lieberman, G. J. (2010). *Introduction to Operations Research* (9th ed.; Chapter 11: Integer Programming, pp. 464–465; Section 11.5: Some Perspectives on Solving Integer Programming Problems, pp. 487–490; Section 11.6: The Branch-and-Bound Technique and Its Application to Binary Integer Programming, p. 491). McGraw-Hill.

---
layout: post
lang: id
title: "Garis Lurus dan Kurva Mengubah Cara Kita Menyelesaikan Masalah: Optimasi Linear vs. Non-Linear"
date: 2026-11-21 12:00:00 +0300
description: "Optimasi di Teknik Industri, Hari #4: bagaimana perbedaan garis lurus dan kurva mengubah cara kita menyelesaikan masalah?"
permalink: /id/tulisan/2026/optimasi-linear-vs-non-linear/
tags: optimasi linear-programming non-linear-programming teknik-industri algoritma
categories: seri-optimasi
giscus_comments: false
related_posts: false
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=11">

<script src="{{ '/assets/js/lang-switch.js' | relative_url }}?v=1" data-lang="id" defer></script>

<script src="{{ '/assets/js/img-zoom.js' | relative_url }}?v=1" defer></script>
<script src="{{ '/assets/js/post-edit.js' | relative_url }}?v=1" data-src="{{ page.path }}" defer></script>
<script src="{{ '/assets/js/series-nav.js' | relative_url }}?v=1" defer></script>

<script src="{{ '/assets/js/lang-nav-id.js' | relative_url }}" defer></script>

*Seri: Optimasi di Teknik Industri, Hari #4. Topik 1.4: Linear vs. Non-Linear Optimization* · [Read in English]({{ '/blog/2026/linear-vs-non-linear-optimization/' | relative_url }})

Pembahasan sebelumnya mengulas bagaimana variabel keputusan, fungsi tujuan, dan batasan (*constraints*) membentuk struktur dasar suatu masalah optimasi. Namun, ketika masuk lebih jauh ke dunia nyata, muncul pertanyaan krusial berikutnya: **apa bentuk hubungan antarvariabel dalam masalah tersebut?** Apakah berupa garis lurus (linear) atau tidak lurus (non-linear) seperti kurva?

Perbedaan sederhana antara garis lurus dan kurva ini ternyata mengubah secara mendasar tingkat kesulitan matematis, jenis algoritma yang dibutuhkan, serta jaminan keberhasilan dalam menemukan solusi terbaik.

---

### Optimasi Linear (Linear Programming / LP)

Suatu masalah optimasi dikategorikan sebagai **Linear Programming (LP)** apabila fungsi tujuan dan seluruh batasannya memenuhi dua sifat utama:

1. **Proporsionalitas (*Proportionality*):** Perubahan pada nilai variabel keputusan menghasilkan perubahan yang sebanding secara konstan pada fungsi tujuan maupun batasan. Sebagai contoh, jika membuat 1 unit produk memerlukan biaya Rp10.000, maka membuat 100 unit produk memerlukan biaya tepat Rp1.000.000.
2. **Additivitas (*Additivity*):** Total kontribusi dari seluruh variabel merupakan penjumlahan langsung dari kontribusi masing-masing variabel, tanpa adanya interaksi saling mengalikan.

#### Sifat Geometris dan Solusi LP

Secara geometris, batasan-batasan linear membentuk **feasible region** berupa poligon konveks di ruang dua dimensi, atau polihedron di ruang berdimensi lebih tinggi. Batas-batas daerah ini berupa garis lurus yang tegas.

Sifat paling istimewa dari optimasi linear adalah **titik optimal selalu terletak pada salah satu titik sudut (*vertex* atau *corner point*) dari feasible region tersebut**. Kerapian struktur geometris ini memungkinkan algoritma klasik seperti *Simplex Method* atau *Interior Point Method* menemukan solusi optimal global secara pasti dan efisien, bahkan untuk masalah dengan jutaan variabel keputusan.

Misalkan sebuah pabrik memproduksi dua jenis barang, $$x_1$$ dan $$x_2$$, dengan keuntungan masing-masing Rp50.000 dan Rp40.000 per unit. Jika kapasitas mesin dan ketersediaan bahan baku dibatasi oleh persamaan linear $$2x_1 + x_2 \le 100$$ dan $$x_1 + 2x_2 \le 80$$, maka fungsi tujuannya dituliskan sebagai:

$$\text{Maximize } Z = 50.000\,x_1 + 40.000\,x_2$$

Masalah ini dapat diselesaikan dengan menelusuri titik-titik sudut feasible region untuk menjamin ditemukannya solusi terbaik mutlak. Di sini, titik sudut $$(0,0)$$, $$(50,0)$$, $$(40,20)$$, dan $$(0,40)$$ menghasilkan $$Z$$ berturut-turut sebesar Rp0, Rp2.500.000, Rp2.800.000, dan Rp1.600.000, sehingga solusi optimalnya adalah memproduksi 40 unit $$x_1$$ dan 20 unit $$x_2$$.

---

### Optimasi Non-Linear (Non-Linear Programming / NLP)

Sebaliknya, sebuah masalah dikategorikan sebagai **Non-Linear Programming (NLP)** apabila fungsi tujuan, atau minimal salah satu batasannya, mengandung hubungan non-linear. Hubungan ini muncul dari berbagai fenomena nyata seperti kuadrat jarak, eksponensial, logaritma, fungsi pangkat, atau perkalian antarvariabel keputusan.

Sebagai contoh, dalam menentukan lokasi fasilitas pabrik baru, jarak Euclidean antara pabrik dan konsumen dihitung menggunakan rumus akar kuadrat $$\sqrt{(x_1 - a_i)^2 + (x_2 - b_i)^2}$$. Kehadiran pangkat dua dan akar kuadrat ini secara otomatis mengubah masalah menjadi non-linear.

#### Perangkap Local Optimum pada NLP

Perubahan dari garis lurus menjadi kurva menciptakan lanskap nilai yang sangat berbeda. Feasible region pada NLP tidak lagi terbatas pada poligon bersudut tegas. Daerah ini dapat memiliki batas melengkung, daerah yang terpisah, atau permukaan bergelombang dengan banyak puncak dan lembah.

Kondisi ini menimbulkan tantangan terbesar dalam optimasi non-linear:

- **Local Optimum:** Titik terbaik di lingkungan sekitarnya, tetapi bukan nilai terbaik dari keseluruhan lanskap.
- **Global Optimum:** Titik terbaik secara mutlak di seluruh feasible region.

Algoritma berbasis turunan (*gradient-based methods*) seperti *Gradient Descent* atau *Sequential Quadratic Programming* (SQP) sering kali terjebak pada puncak lokal dan menghentikan pencarian karena menganggap puncak tersebut sebagai titik tertinggi.

<img src="{{ '/assets/img/blog/optimization-day-4-id.svg' | relative_url }}" alt="Perbandingan optimasi linear dan non-linear: feasible region konveks dengan optimum di titik sudut, versus lanskap banyak puncak dengan perangkap local optimum" style="max-width: 100%; height: auto; display: block; margin: 1rem auto 0.25rem;">
<p style="text-align: center;"><em>Gambar 1. Feasible region optimasi linear berbentuk poligon konveks (kiri) dibandingkan lanskap bergelombang optimasi non-linear dengan perangkap local optimum (kanan).</em></p>

---

### Perbandingan Kasus di Teknik Industri

Untuk memahami dampaknya secara praktis, tabel berikut memperlihatkan bagaimana perbedaan asumsi linearitas memengaruhi pemodelan sistem nyata:

| Dimensi Perbandingan | Optimasi Linear (LP) | Optimasi Non-Linear (NLP) |
| :--- | :--- | :--- |
| **Bentuk Matematika** | Seluruh fungsi $$f(x)$$ dan $$g(x)$$ berderajat satu ($$ax_1 + bx_2$$). | Mengandung $$x^2$$, $$\sqrt{x}$$, $$\log(x)$$, $$x_1 \cdot x_2$$, atau eksponensial. |
| **Bentuk Feasible Region** | Poligon atau polihedron konveks dengan batas garis lurus. | Batas melengkung, permukaan tidak rata, atau daerah terpisah. |
| **Lokasi Solusi Optimal** | Selalu berada di titik sudut (*vertex* / *corner point*). | Dapat berada di mana saja: di dalam area, pada batas kurva, atau di puncak gelombang. |
| **Jaminan Solusi** | Solusi optimal global dijamin selalu ditemukan. | Berisiko terjebak pada local optimum. |
| **Contoh Aplikasi TI** | Perencanaan produksi harian, *blending problem*, pengalokasian tenaga kerja. | Lokasi fasilitas (jarak Euclidean), optimasi portofolio risiko, *chemical process control*. |

---

### Menghubungkan Model dengan Metode Penyelesaian

Klasifikasi antara LP dan NLP menentukan jalur algoritma yang dipilih oleh seorang insinyur Teknik Industri:

1. Jika model dapat dirumuskan secara linear (LP), *solver* komersial seperti CPLEX, Gurobi, atau GLPK mampu menyelesaikan masalah dengan jutaan variabel dalam hitungan detik.
2. Jika model bersifat non-linear tetapi konveks, metode *Interior Point* atau *SQP* masih dapat memberikan solusi optimal global secara efisien.
3. Jika model bersifat non-linear dan non-konveks (*multimodal*), pendekatan metaheuristik seperti *Genetic Algorithm* (GA), *Particle Swarm Optimization* (PSO), atau *Simulated Annealing* (SA) menjadi pilihan utama untuk mengeksplorasi lanskap dan menghindari perangkap local optimum.
4. Jika masalahnya sangat besar atau bersifat kombinatorial (misalnya masalah scheduling, routing, atau nesting yang *NP-hard*) sehingga metode eksak tidak selesai dalam waktu wajar, digunakan *heuristic*. Metode ini tidak menjamin global optimum, tetapi cepat menghasilkan solusi feasible yang baik, dan inilah trade-off yang sering dipilih dalam praktik industri.

Pemahaman mengenai struktur LP dan NLP ini merupakan langkah kunci sebelum masuk ke teknik formulasi dan pemilihan algoritma pada pembahasan selanjutnya.

---

### Referensi

Cuevas, E., Rosas Caro, J. C., Alejo Reyes, A., González Ayala, P., & Rodriguez, A. (2025). *Optimization in Industrial Engineering: From Classical Methods to Modern Metaheuristics with MATLAB Applications* (Chapter 1, Section 1.4: Linear vs. Non-Linear Optimization, pp. 12–18). Springer Nature.

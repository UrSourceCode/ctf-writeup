## Web - Vision

di challange ini kita diberikan ip sebuah website untuk kita kunjungi.

![web](assets/vision-web.jpg)

selanjutnya langsung kita lihat `page source` nya

![html](assets/sc-web.jpg)

Terlihat cara pengecekan sistem login web tersebut agar mendapatkan secret code nya dan dapat mengakses web lebih jauh lagi. dengan memasukkan secret code nya yaitu `mantapujiwa`

![congrats](assets/congrats-web.jpg)

Setelah berhasil memasukkan secret code kita diarahkan ke page selanjutnya.

![next](assets/nextpage-web.jpg)

Terlihat page selanjutnya hanya kosong dan pertanyaan. Lalu kita juga lihat page source nya apakah ada petunjuk.

![visible](assets/visible-web.jpg)

Ternyata pada codenya terlihat ada elemen html yang disengaja dihidden menggunakkan styling css. Lalu langsung saja kita nonaktifkan stylingnya.

![flag](assets/flag-web.jpg)

Lalu muncul flag nya yaitu `JCTF2023{s0_e4sy_w3b_3xPl0itation}`

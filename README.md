# Kantor Virtual 3D — Humas UIN Walisongo

Kantor virtual 3D interaktif untuk tim Humas UIN Walisongo Semarang.

**Buka kantor:** https://neinareno.github.io/kantor-virtual-3d/

Bisa juga membuka `index.html` langsung di browser (perlu internet untuk memuat Three.js dan font).

## Kontrol

- **WASD** atau panah: berjalan
- **Shift**: berjalan cepat
- **Mouse**: melihat sekeliling (klik untuk mengunci kursor, Esc untuk melepas)
- **V**: ganti sudut pandang (orang ketiga / orang pertama)
- Klik meja atau staf, isi formulir **Beri Tugas**, lalu **Kirim**
- Satu klik mengirim tugas ke Klaus setelah token GitHub disimpan di **Pengaturan**
- **Riwayat Tugas**: lihat tugas yang sudah dikirim, plus **Cek status** jika issue sudah diteruskan

## Token GitHub (satu kali)

1. Buka [tautan buat token fine-grained](https://github.com/settings/personal-access-tokens/new?name=Kantor%20Virtual%203D&description=Kirim%20tugas%20dari%20kantor&target_name=Neinareno&expires_in=none&issues=write) (nama, deskripsi, pemilik, masa berlaku, dan izin Issues sudah terisi).
2. **Repository access** → **Only select repositories** → pilih **kantor-virtual-3d** (tidak bisa diisi otomatis dari tautan).
3. **Permissions** → **Issues: Read and write**, lalu **Generate** dan salin token.
4. Tempel di Pengaturan kantor, **Simpan**, lalu **Tes token**.

Token hanya tersimpan di peramban, tidak masuk repositori. Secret Actions **`GROK_WEBHOOK_AUTH`** tetap diperlukan agar workflow meneruskan issue ke Klaus.

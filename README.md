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
- Tab GitHub akan terbuka; klik **Create issue** (masuk sebagai Neinareno) agar tugas diteruskan ke Klaus
- Daftar staf atau peta: pindah ke meja
- **Riwayat Tugas**: lihat tugas yang sudah dibuka dari kantor ini

## Secret webhook

GitHub Actions meneruskan issue berlabel `tugas` (dibuat oleh Neinareno) ke webhook Klaus. Buat secret repositori bernama **`GROK_WEBHOOK_AUTH`** berisi Authorization header (boleh dengan atau tanpa awalan `Bearer `).

-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 04 Jun 2022 pada 23.10
-- Versi server: 10.4.24-MariaDB
-- Versi PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `week12pbo`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `barang`
--

CREATE TABLE `barang` (
  `kode_brg` varchar(3) NOT NULL,
  `nama_brg` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `barang`
--

INSERT INTO `barang` (`kode_brg`, `nama_brg`) VALUES
('001', 'Indomie');

-- --------------------------------------------------------

--
-- Struktur dari tabel `cabang_bank`
--

CREATE TABLE `cabang_bank` (
  `kode_cabang` varchar(3) NOT NULL,
  `nama_cabang` varchar(30) NOT NULL,
  `alamat_cabang` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `dosen`
--

CREATE TABLE `dosen` (
  `kode_dos` varchar(10) NOT NULL,
  `nama_dos` varchar(30) NOT NULL,
  `alamat_dos` varchar(30) NOT NULL,
  `no_tlp` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `dosen`
--

INSERT INTO `dosen` (`kode_dos`, `nama_dos`, `alamat_dos`, `no_tlp`) VALUES
('C3', 'Endang', 'Yogyakarta', '082167845321'),
('D2', 'Sutarman', 'Mlati', '084536789765'),
('E3', 'Ali Romli', 'Sleman', '087892345678');

-- --------------------------------------------------------

--
-- Struktur dari tabel `gaji`
--

CREATE TABLE `gaji` (
  `bulan` varchar(20) NOT NULL,
  `nip` varchar(20) NOT NULL,
  `masuk` int(5) NOT NULL,
  `sakit` int(5) NOT NULL,
  `izin` int(5) NOT NULL,
  `alfa` int(5) NOT NULL,
  `lembur` int(5) NOT NULL,
  `potongan` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `gaji`
--

INSERT INTO `gaji` (`bulan`, `nip`, `masuk`, `sakit`, `izin`, `alfa`, `lembur`, `potongan`) VALUES
('February', '5210411203', 12, 0, 0, 0, 6, 2500);

-- --------------------------------------------------------

--
-- Struktur dari tabel `golongan`
--

CREATE TABLE `golongan` (
  `kode_golongan` varchar(3) NOT NULL,
  `nama_golongan` varchar(10) NOT NULL,
  `tunjangan_suami` int(10) NOT NULL,
  `tunjangan_anak` int(10) NOT NULL,
  `uang_makan` int(10) NOT NULL,
  `uang_lembur` int(10) NOT NULL,
  `askes` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `golongan`
--

INSERT INTO `golongan` (`kode_golongan`, `nama_golongan`, `tunjangan_suami`, `tunjangan_anak`, `uang_makan`, `uang_lembur`, `askes`) VALUES
('03', '3A', 3000, 1500, 350, 100, 5);

-- --------------------------------------------------------

--
-- Struktur dari tabel `jabatan`
--

CREATE TABLE `jabatan` (
  `kode_jabatan` varchar(3) NOT NULL,
  `nama_jabatan` varchar(40) NOT NULL,
  `gapok` int(10) NOT NULL,
  `tunjangan_jabatan` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `jabatan`
--

INSERT INTO `jabatan` (`kode_jabatan`, `nama_jabatan`, `gapok`, `tunjangan_jabatan`) VALUES
('01', 'Pegawai', 30, 7500);

-- --------------------------------------------------------

--
-- Struktur dari tabel `kuliah`
--

CREATE TABLE `kuliah` (
  `kode_mk` varchar(10) NOT NULL,
  `kode_dos` varchar(10) NOT NULL,
  `waktu` varchar(30) NOT NULL,
  `tempat` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `kuliah`
--

INSERT INTO `kuliah` (`kode_mk`, `kode_dos`, `waktu`, `tempat`) VALUES
('001', 'E3', '14.40', 'E3.4'),
('002', 'D2', '12.50', 'D2.2'),
('003', 'C3', '16.30', 'LC3.2');

-- --------------------------------------------------------

--
-- Struktur dari tabel `mata kuliah`
--

CREATE TABLE `mata kuliah` (
  `kode_mk` varchar(3) NOT NULL,
  `nama_mk` varchar(30) NOT NULL,
  `sks` varchar(3) NOT NULL,
  `semester` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `mata kuliah`
--

INSERT INTO `mata kuliah` (`kode_mk`, `nama_mk`, `sks`, `semester`) VALUES
('001', 'Rekayasa Web', '2', '2'),
('002', 'Sistem Komputer', '3', '2'),
('003', 'Pbo Praktik', '2', '2');

-- --------------------------------------------------------

--
-- Struktur dari tabel `nasabah`
--

CREATE TABLE `nasabah` (
  `id_nasabah` varchar(3) NOT NULL,
  `nama_nasabah` varchar(30) NOT NULL,
  `alamat_nasabah` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `nota`
--

CREATE TABLE `nota` (
  `no_nota` varchar(3) NOT NULL,
  `tanggal` varchar(30) NOT NULL,
  `tempo` varchar(30) NOT NULL,
  `total` int(11) NOT NULL,
  `kode_sup` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `pegawai`
--

CREATE TABLE `pegawai` (
  `nip` varchar(20) NOT NULL,
  `nama_pegawai` varchar(40) NOT NULL,
  `kode_jabatan` varchar(3) NOT NULL,
  `kode_golongan` varchar(3) NOT NULL,
  `status` varchar(15) NOT NULL,
  `jumlah_anak` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `pegawai`
--

INSERT INTO `pegawai` (`nip`, `nama_pegawai`, `kode_jabatan`, `kode_golongan`, `status`, `jumlah_anak`) VALUES
('5210411203', 'Febriyan', '03', '2A', 'Belum Menikah', 0);

-- --------------------------------------------------------

--
-- Struktur dari tabel `rekening`
--

CREATE TABLE `rekening` (
  `no_rekening` varchar(3) NOT NULL,
  `pin` int(11) NOT NULL,
  `saldo` int(11) NOT NULL,
  `id_nasabah` varchar(3) NOT NULL,
  `kode_cabang` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `supplier`
--

CREATE TABLE `supplier` (
  `kode_sup` varchar(3) NOT NULL,
  `nama_sup` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi`
--

CREATE TABLE `transaksi` (
  `no_transaksi` varchar(3) NOT NULL,
  `jenis_nasabah` varchar(30) NOT NULL,
  `tanggal` varchar(30) NOT NULL,
  `jumlah` int(11) NOT NULL,
  `id_nasabah` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi_brg`
--

CREATE TABLE `transaksi_brg` (
  `no_nota` varchar(3) NOT NULL,
  `kode_brg` varchar(3) NOT NULL,
  `qty` int(3) NOT NULL,
  `harga` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `barang`
--
ALTER TABLE `barang`
  ADD PRIMARY KEY (`kode_brg`);

--
-- Indeks untuk tabel `cabang_bank`
--
ALTER TABLE `cabang_bank`
  ADD PRIMARY KEY (`kode_cabang`);

--
-- Indeks untuk tabel `dosen`
--
ALTER TABLE `dosen`
  ADD PRIMARY KEY (`kode_dos`);

--
-- Indeks untuk tabel `kuliah`
--
ALTER TABLE `kuliah`
  ADD PRIMARY KEY (`kode_mk`);

--
-- Indeks untuk tabel `nasabah`
--
ALTER TABLE `nasabah`
  ADD PRIMARY KEY (`id_nasabah`);

--
-- Indeks untuk tabel `nota`
--
ALTER TABLE `nota`
  ADD PRIMARY KEY (`no_nota`);

--
-- Indeks untuk tabel `rekening`
--
ALTER TABLE `rekening`
  ADD PRIMARY KEY (`no_rekening`);

--
-- Indeks untuk tabel `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`kode_sup`);

--
-- Indeks untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`no_transaksi`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
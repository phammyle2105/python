const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use(express.static("public"));

const db = new sqlite3.Database("./database.db");

// ===== TẠO BẢNG =====
db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS MatHang(
    MaMH TEXT PRIMARY KEY,
    TenMH TEXT,
    NguonGoc TEXT,
    DonGia REAL
  )`);

  db.run(`CREATE TABLE IF NOT EXISTS KhachHang(
    MaKH TEXT PRIMARY KEY,
    TenKH TEXT,
    DiaChi TEXT,
    SoDienThoai TEXT
  )`);

  db.run(`CREATE TABLE IF NOT EXISTS DonHang(
    MaDH TEXT PRIMARY KEY,
    MaKH TEXT,
    NgayLap TEXT
  )`);

  db.run(`CREATE TABLE IF NOT EXISTS ChiTietDonHang(
    MaDH TEXT,
    MaMH TEXT,
    SoLuong INTEGER,
    DonGia REAL
  )`);
});

// ===== API MẶT HÀNG =====
app.get("/mathang", (req, res) => {
  db.all("SELECT * FROM MatHang", [], (err, rows) => {
    res.json(rows);
  });
});

app.post("/mathang", (req, res) => {
  const { MaMH, TenMH, NguonGoc, DonGia } = req.body;
  db.run(
    "INSERT INTO MatHang VALUES (?, ?, ?, ?)",
    [MaMH, TenMH, NguonGoc, DonGia],
    () => res.send("OK")
  );
});

app.delete("/mathang/:id", (req, res) => {
  db.run("DELETE FROM MatHang WHERE MaMH = ?", [req.params.id], () =>
    res.send("Deleted")
  );
});

// ===== API KHÁCH HÀNG =====
app.get("/khachhang", (req, res) => {
  db.all("SELECT * FROM KhachHang", [], (err, rows) => {
    res.json(rows);
  });
});

app.post("/khachhang", (req, res) => {
  const { MaKH, TenKH, DiaChi, SoDienThoai } = req.body;
  db.run(
    "INSERT INTO KhachHang VALUES (?, ?, ?, ?)",
    [MaKH, TenKH, DiaChi, SoDienThoai],
    () => res.send("OK")
  );
});

// ===== API ĐƠN HÀNG =====
app.get("/donhang", (req, res) => {
  db.all(
    `SELECT DH.*, 
     IFNULL(SUM(CT.SoLuong * CT.DonGia),0) AS TongTien
     FROM DonHang DH
     LEFT JOIN ChiTietDonHang CT ON DH.MaDH = CT.MaDH
     GROUP BY DH.MaDH`,
    [],
    (err, rows) => {
      res.json(rows);
    }
  );
});

// thêm đơn hàng + chi tiết
app.post("/donhang", (req, res) => {
  const { MaDH, MaKH, NgayLap, items } = req.body;

  db.run(
    "INSERT INTO DonHang VALUES (?, ?, ?)",
    [MaDH, MaKH, NgayLap]
  );

  items.forEach((item) => {
    db.run(
      "INSERT INTO ChiTietDonHang VALUES (?, ?, ?, ?)",
      [MaDH, item.MaMH, item.SoLuong, item.DonGia]
    );
  });

  res.send("OK");
});

// chi tiết đơn
app.get("/donhang/:id", (req, res) => {
  db.all(
    `SELECT * FROM ChiTietDonHang WHERE MaDH = ?`,
    [req.params.id],
    (err, rows) => res.json(rows)
  );
});

// ===== RUN SERVER =====
app.listen(3000, () => {
  console.log("Server running at http://localhost:3000");
});
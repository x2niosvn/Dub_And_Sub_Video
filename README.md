# X2NSoft VDub

**Lồng tiếng Việt cho video nước ngoài — tự động, chạy trên máy bạn, miễn phí.**

Ứng dụng desktop cho Windows. Dán link YouTube / TikTok / Douyin / Bilibili (hoặc chọn file trên máy), chọn giọng đọc, bấm chạy — nhận về video đã lồng tiếng Việt, **giữ nguyên nhạc nền và hiệu ứng âm thanh gốc**, kèm phụ đề và trình chỉnh sửa từng câu.

Nghe-chép, lồng tiếng, phụ đề, xuất video đều **chạy offline trên máy bạn**, không cần gửi video hay âm thanh đi đâu.

```
Link / File video
   ├─► Tải về  ──►  Tách âm thanh  ──►  Tách nhạc nền (Demucs)
   │                       │
   │                       └──►  Nghe-chép lời gốc (Whisper / Paraformer)
   │                                     │
   │                                     └──►  Dịch sang tiếng Việt
   │                                                  │
   │                                                  └──►  Đọc thành giọng Việt (VieNeu / CapCut)
   │                                                              │
   │                                                              └───►  Khớp thời gian  ┘
   │                                                                           │
   └───────────────────────────────────────────────────────────────────────────►  Trộn nhạc nền + phụ đề + che chữ gốc
                                                                               │
                                                                         dubbed_video.mp4
```

---

## Mục lục

1. [Cài đặt tự động](#1-cài-đặt-tự-động)
2. [Chạy video đầu tiên](#2-chạy-video-đầu-tiên)
3. [Quy trình dịch thuật](#3-quy-trình-dịch-thuật)
4. [Hướng dẫn các chức năng chính](#4-hướng-dẫn-các-chức-năng-chính)
5. [Kết quả đầu ra nằm ở đâu](#5-kết-quả-đầu-ra-nằm-ở-đâu)
6. [Câu hỏi thường gặp](#6-câu-hỏi-thường-gặp)
7. [Dành cho lập trình viên](#7-dành-cho-lập-trình-viên)

---

## 1. Cài đặt tự động

### Chuẩn bị môi trường hệ thống

| Yêu cầu | Tải về | Lưu ý |
|---|---|---|
| **Python 3.10 trở lên** | <https://www.python.org/downloads/> | Khi cài đặt **BẮT BUỘC tích chọn ô "Add Python to PATH"** |
| **ffmpeg (bản full)** | <https://www.gyan.dev/ffmpeg/builds/> — chọn `ffmpeg-release-full.7z` | Giải nén ra ví dụ `C:\ffmpeg`, rồi thêm thư mục `C:\ffmpeg\bin` vào **PATH** của hệ thống |

<details>
<summary><b>Cách thêm ffmpeg vào PATH (bấm để xem)</b></summary>

1. Giải nén file `.7z` vừa tải về.
2. Đổi tên thư mục vừa giải nén thành `ffmpeg` và sao chép vào ổ `C:\` → đường dẫn sẽ là `C:\ffmpeg\bin\ffmpeg.exe`
3. Nhấp phím Windows, gõ **"environment variables"** → mở **"Edit the system environment variables"**
4. Bấm **Environment Variables…** → tại khung phía dưới chọn dòng **Path** → **Edit** → **New** → dán đường dẫn `C:\ffmpeg\bin` → nhấn **OK** cho tất cả các hộp thoại.
5. Mở Command Prompt (cmd) mới, gõ `ffmpeg -version`. Nếu hiện thông tin phiên bản là thành công.

</details>

### Cài đặt và Khởi chạy chỉ với 2 file `.bat`

Dự án được tối ưu hóa tối đa và quản lý thông qua đúng **2 file thực thi duy nhất** ở thư mục gốc:

1. **Cài đặt tự động hoàn toàn**:
   > Đúp chuột vào **`cai_dat.bat`**
   
   Script này sẽ chạy tự động 100% không cần can thiệp:
   * Kiểm tra phiên bản Python và cài đặt ffmpeg.
   * Tạo môi trường ảo dùng chung duy nhất (`.venv`).
   * Tự động cấu hình file `.env`.
   * Tự động cài đặt Whisper (bộ nghe-chép), Paraformer (bộ nghe tiếng Trung), VieNeu (bộ giọng đọc offline) và nạp sẵn 120 giọng đọc mẫu vào hệ thống.
   
2. **Khởi chạy ứng dụng**:
   > Đúp chuột vào **`chay_app.bat`** để mở giao diện GUI được thiết kế hiện đại (Premium Obsidian Dark Theme).

---

## 2. Chạy video đầu tiên

1. Mở ứng dụng → chọn trang **Tạo dự án** ở menu bên trái.
2. **Dán link video** (YouTube, Douyin, TikTok...) hoặc chọn file video `.mp4` có sẵn trên máy của bạn.
3. Chọn **ngôn ngữ gốc** của video và lựa chọn **giọng đọc** muốn sử dụng (có thể bấm nghe thử trước).
4. Nhấp nút **Bắt đầu lồng tiếng** và chờ hệ thống xử lý.

> **Nếu bị ngắt quãng giữa chừng**: Mọi tiến độ đều được tự động lưu theo thời gian thực. Bạn chỉ cần mở lại trang **Dự án**, chọn dự án đó để tiếp tục chạy từ bước bị dừng mà không phải làm lại từ đầu.

---

## 3. Quy trình dịch thuật

Mọi bước trong quy trình đều chạy offline trên máy của bạn. Riêng bước dịch thuật, ứng dụng hỗ trợ dịch bằng trí tuệ nhân tạo (AI) thông qua file trung gian:

### Quy trình dịch thủ công bằng AI (Mặc định)
1. Khi đến bước dịch, ứng dụng sẽ dừng lại và tạo file `TRANSLATE_PENDING.txt` trong thư mục dự án.
2. Bạn nhấp nút **Mở hướng dẫn** trên giao diện ứng dụng để lấy lời nhắc dịch (prompt) được soạn sẵn.
3. Sao chép nội dung lời thoại gốc trong `data/transcript_original.json`, dán vào **ChatGPT, Gemini hoặc Claude** kèm theo prompt để dịch sang tiếng Việt.
4. Lưu kết quả trả về từ AI thành file `data/transcript_vi.json` rồi quay lại ứng dụng nhấp **Đã dịch xong, tiếp tục**.

### Tối ưu hóa ngữ cảnh bản dịch
Tại trang **Dịch thuật** ở thanh menu bên trái, bạn có thể thiết lập thêm thông tin để AI dịch chuẩn xác hơn:
* **Chủ đề**: ví dụ `review công nghệ`, `vlog ẩm thực`, `phim cổ trang`.
* **Xưng hô**: ví dụ `mình - các bạn`, `tôi - anh em`, `huynh - muội`.
* **Thuật ngữ cố định**: quy định cách dịch cụ thể cho các từ khóa chuyên ngành.
* **Văn phong**: ví dụ `giọng trẻ trung, hài hước, nhiều từ lóng`.

---

## 4. Hướng dẫn các chức năng chính

### Tạo dự án & Cấu hình video
* **Tách nhạc nền**: Sử dụng mô hình `Demucs` để tách giọng nói gốc ra khỏi âm nhạc và hiệu ứng (cho chất lượng tốt nhất) hoặc dùng `Duck` tự động hạ nhỏ âm lượng gốc khi có giọng thuyết minh chèn vào (tốc độ xử lý nhanh hơn).
* **Hiển thị phụ đề**: Tùy chọn xuất phụ đề rời dạng `.srt` hoặc ghi thẳng cứng (hardsub) vào video.
* **Che chữ gốc & Xem trước**: Hỗ trợ kéo thả vùng phụ đề trực tiếp trên màn hình xem trước và vẽ vùng chọn để che/blur chữ/logo gốc (như chữ Trung Quốc).

### Xử lý hàng loạt (Batch Processing)
* Dán danh sách link video cần xử lý (mỗi dòng một video).
* Có thể chỉ định riêng giọng đọc cho từng video bằng cách thêm ký tự `| nam` hoặc `| nữ` ở cuối dòng link.
* Trạng thái tiến độ được lưu tự động, tự động bỏ qua các video đã hoàn thành nếu chạy lại.

### Trình chỉnh sửa từng câu (Editor)
* Hiển thị bảng song ngữ trực quan (lời gốc bên trái, lời dịch bên phải).
* Nhấp đúp vào ô lời dịch để sửa lại nội dung văn bản.
* Nhấp nút nghe thử từng câu, sau khi sửa xong chỉ cần nhấp **Lưu tất cả và đọc lại** để cập nhật âm thanh cho riêng các câu đã sửa.
* Xuất file video hoàn chỉnh, hoặc tải riêng file âm thanh lồng tiếng độc lập.

### Thư viện giọng đọc AI
* Tích hợp sẵn bộ lọc tìm kiếm theo giới tính, vùng miền, phong cách.
* Cho phép **tự thêm giọng nói của riêng bạn**: Chỉ cần tải lên 1 đoạn ghi âm mẫu sạch (không nhạc nền) dài khoảng 5–10 giây, gõ lại nội dung văn bản nói trong đó, ứng dụng sẽ tự động học giọng (clone) và đưa vào danh sách giọng đọc ngoại tuyến.

---

## 5. Kết quả đầu ra nằm ở đâu

Mỗi dự án sau khi hoàn thành sẽ được tạo một thư mục riêng trong thư mục `output/`:

```
output/VN/20260809103000_vi/
├── dubbed_video.mp4            ← VIDEO ĐÃ LỒNG TIẾNG HOÀN CHỈNH
├── transcript_vi.srt           ← Phụ đề tiếng Việt rời
├── youtube/                    ← Tiêu đề, mô tả và gợi ý hình thu nhỏ gợi ý cho YouTube
└── data/                       ← Dữ liệu kỹ thuật phục vụ cho việc chỉnh sửa câu
    ├── transcript_original.json/.srt   ← Kết quả nghe-chép âm thanh gốc
    ├── transcript_vi.json              ← Bản dịch tiếng Việt được định dạng cấu trúc
    ├── original_audio.wav, vocals.wav, no_vocals.wav
    ├── audio_vi_full.wav               ← File âm thanh lồng tiếng Việt đã khớp thời gian
    ├── segments/                       ← Thư mục lưu file âm thanh của từng câu thoại
    └── quality_report.json             ← Báo cáo chất lượng khớp thời gian âm thanh
```

---

## 6. Câu hỏi thường gặp

**Tại sao lần đầu chạy lồng tiếng lại rất lâu?**
Trong lần chạy đầu tiên, hệ thống cần tải các mô hình AI (Whisper, Demucs) về máy để xử lý offline (khoảng vài GB). Các lần chạy tiếp theo sẽ diễn ra cực kỳ nhanh chóng.

**Ứng dụng có cần card đồ họa rời (GPU) không?**
Không bắt buộc. Hệ thống có thể chạy hoàn toàn trên CPU thông thường. Nếu máy bạn có card đồ họa rời NVIDIA, ứng dụng sẽ tự động kích hoạt chế độ tăng tốc phần cứng để xử lý nhanh hơn gấp nhiều lần.

**Giọng đọc bị nhanh hoặc chồng lên nhau?**
Do tiếng Việt dịch ra thường dài hơn tiếng Anh/Trung khoảng 20%, bạn có thể tinh chỉnh bằng các cách sau:
1. Vào **Trình chỉnh sửa**, viết lại câu dịch ngắn gọn, súc tích hơn.
2. Giảm chỉ số `TRANSLATE_CPS_BUDGET` trong phần cài đặt xuống khoảng `11.0` - `12.0`.
3. Tăng nhẹ tốc độ đọc hoặc chọn chế độ làm chậm nhẹ tốc độ video (`VIDEO_SPEED=0.9`) để có thêm khoảng trống phát âm thanh.

---

## 7. Dành cho lập trình viên

### Cấu trúc mã nguồn

* `autodub/`: Phần lõi xử lý thuật toán và pipeline lồng tiếng (không phụ thuộc vào giao diện).
* `autodub_gui/`: Giao diện đồ họa viết bằng thư viện PySide6 sử dụng hệ thống màu thiết kế Obsidian Dark.
* `scripts/`: Tập hợp các script cài đặt, kiểm tra môi trường và đóng gói ứng dụng.
* `voices/preset_voices_vn/`: Thư mục lưu trữ 120 giọng đọc mẫu đi kèm.
* `tests/`: Bộ kiểm thử tự động (tests) cho toàn bộ pipeline.

### Nguyên tắc kiến trúc

* **Môi trường ảo hợp nhất**: Dự án sử dụng một thư mục `.venv` duy nhất để chứa mọi thư viện Python (PySide6, PyTorch, faster-whisper, vieneu), giúp tối ưu hóa dung lượng đĩa và tránh xung đột phiên bản giữa các module.
* **Trạng thái lưu trên file**: Mọi bước trung gian đều được lưu trực tiếp xuống đĩa cứng thành các file dữ liệu dạng JSON, WAV, nhờ đó pipeline có thể phục hồi trạng thái sau khi lỗi hoặc tắt ứng dụng.

### Chạy kiểm thử tự động

```bash
.venv\Scripts\activate
pytest -q
```

### Đóng gói ứng dụng sang `.exe`

```bash
.venv\Scripts\python scripts/build_exe.py
```


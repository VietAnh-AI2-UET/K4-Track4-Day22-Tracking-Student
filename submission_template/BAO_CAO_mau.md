# Báo cáo lab: chọn tracker cho 5 video

**Nhóm:** FrostyAshe **Thành viên:** Bùi Việt Anh - 2A202602611

Detector cố định: `yolo26n.pt`, ảnh 640 px, Re-ID `osnet_x0_25_msmt17`. Không đổi các mục này trong bài nộp chính.

## 1. Cấu hình đã chọn

Mỗi video: tracker bạn nộp, `conf`, `iou`, điều bạn **nhìn thấy** trên video, và một cấu hình đã thử rồi loại.

| Video | Tracker | conf | iou | Quan sát khi xem video | Đã thử nhưng loại |
|---|---|---|---|---|---|
| video_1 (quảng trường, tĩnh, ban ngày) | botsort | 0.3 | 0.5 |  |  |
| video_2 (phố đêm, tĩnh, rất đông) | bytetrack | 0.3 | 0.5 |  |  |
| video_3 (camera di động, ảnh nhỏ) | bytetrack | 0.3 | 0.5 |  |  |
| video_4 (trong nhà, camera di chuyển) | bytetrack | 0.3 | 0.5 |  |  |
| video_5 (trên xe bus, giao lộ đông) | bytetrack | 0.3 | 0.5 |  |  |

## 2. Số liệu video_1

| Video | Tracker | conf | iou | HOTA | MOTA | IDF1 |
|---|---|---|---|---|---|---|
| video_1 | botsort | 0.3 | 0.5 | 26.424 | 14.122 | 22.794 |

```text
HOTA:      HOTA    DetA    AssA    DetRe   DetPr   AssRe   AssPr   LocA
video_1    26.424  12.570  55.551  12.709  85.619  59.644  83.876  87.005

CLEAR:     MOTA    MOTP    MODA    CLR_Re  CLR_Pr  CLR_TP  CLR_FN  CLR_FP  IDSW
video_1    14.122  85.414  14.165  14.504  97.716  2695    15886   63      8

Identity:  IDF1    IDR     IDP     IDTP    IDFN    IDFP
video_1    22.794  13.089  88.180  2432    16149   326
```

Output đầy đủ: `runs/nhat_ky/evaluate_video1.log`. Cấu hình chấm dùng tên thư mục nội bộ `LAB21`, `split=train`

File cấu hình bổ sung được lưu tại `submission_template/eval_config.json`

## 3. Phân tích

**video_1:** Trên cùng 600 frame, ByteTrack (`conf=0.3`, `iou=0.5`) đạt HOTA 25.488, MOTA 15.564 và IDF1 22.997; BoT-SORT đạt tương ứng 26.424, 14.122 và 22.794. BoT-SORT được chọn theo HOTA cao nhất trong ba cấu hình đã chấm đủ frame, với điểm liên kết danh tính AssA tăng từ 48.284 lên 55.551 và số lần đổi ID giảm từ 10 xuống 8. Trong cảnh camera tĩnh, ngoại hình người là thông tin bổ sung hữu ích bên cạnh vị trí và chuyển động; kết quả đo phù hợp với lợi ích này. Tuy nhiên, MOTA và IDF1 của BoT-SORT không cao hơn ByteTrack, và số lần bỏ sót vẫn lớn (15.886), nên không kết luận BoT-SORT tốt hơn ở mọi mặt.

**video_4:** Đã đối chiếu ByteTrack và BoT-SORT ở frame 31, 81 và 141 của đoạn thử 150 frame; cả hai đều giữ ID 2 cho người áo đỏ ở các khung này. Camera tiến về phía trước làm vị trí và kích thước người trong ảnh thay đổi, nên thông tin ngoại hình của BoT-SORT có thể hữu ích khi người bị che khuất, nhưng các khung đã xem chưa cho thấy lợi thế rõ. ByteTrack được giữ làm cấu hình nộp cho video này vì chưa có bằng chứng quan sát đủ mạnh để đổi tracker. Video không có nhãn chấm trong gói lab; các khung mẫu không đủ để kết luận ID được giữ đúng trên toàn bộ video.

## 4. Nếu có thêm thời gian

Một hoặc hai câu: bạn sẽ thử tiếp điều gì (Re-ID khác, quét `conf` mịn hơn, xem frame gây lỗi…).

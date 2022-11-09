# Thông tin:

- Họ tên: Nguyễn Phúc Thuần
- MSSV: 20120380

# Thuật toán earley

## Cài đặt

### Các tham số để thiết lập văn phạm (Grammar):

#### Terminal word:

- a: tính từ (adjective)
- n: danh từ (noun)
- v: động từ (verb)
- d: hạn định từ (determinant)
- p: giới từ (preposition)

Các từ thuộc tập các loại từ này nằm trong các file tương ứng:

- adjective.dat
- noun.dat
- verb.dat
- determinant.dat
- preposition.dat

#### Non-terminal:

- S: start
- NP: noun phrase
- NP2: noun phrase (level 2)
- NP3: noun phrase (level 3)
- VP: verb phrase
- PP: preposition phrase

#### Lưu ý:

Có thể định nghĩa tùy ý cho các non-terminal, nhưng

- Luật sinh của mỗi phần tử phải chứa {a, n, v, d, p} tương ứng nếu có.
- Luật sinh của mỗi phần tử phải chứa các phần tử đã được định nghĩa khác.

ví dụ:

- Đúng:

```php
'S': [['NP', 'Verb-Phrase'], ['NP', 'Verb-Phrase', 'PP']]
'NP': {['d', 'NP3']}
'Verb-Phrase': [['v']]
```

- Sai:

```php
'S': [['NP', 'VP'], ['NP', 'VP', 'PP']]
-> sai VP vì nó chưa được định nghĩa
'NP': [['d', 'NP3']]
'Verb-Phrase': [['v']]
```

```php
'S': [['NP', 'VP'], ['NP', 'VP', 'PP']]
'NP': [['det', 'NP3']]
-> sai det vì nó nằm ngoài terminal đã được định nghĩa
'Verb-Phrase': [['v']]
```

### Thiết lập văn phạm (Grammar):

- Mỗi luật chứa 1 gốc sinh và các tập sản phẩm, theo như lưu ý ở trên
- Luư trữ trong các file json, mặc định là sample-grammar.json

### Thiết lập bộ test:

- Sử dụng 1 câu tiếng Anh, lưu trong 1 file văn bản thuần bất kì (ví dụ txt, dat, ...)
- Do hạn chế trong nguồn ngữ liệu cũng như tiền xử lí, các từ chỉ nên ở dạng nguyên mẫu của chúng.

Ví dụ:

- does, did -> do
- kicks, kicked -> kick

### Tiến hành chạy:

- B1: Tải thư mục về từ github:

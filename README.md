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
'NP': [['d', 'NP3']]
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
- Lưu trữ trong các file json, mặc định là sample-grammar.json

### Thiết lập bộ test:

- Sử dụng 1 câu tiếng Anh, lưu trong 1 file văn bản thuần bất kì (ví dụ txt, dat,...)
- Do hạn chế trong nguồn ngữ liệu cũng như tiền xử lí, các từ chỉ nên ở dạng nguyên mẫu của chúng.

Ví dụ:

- does, did -> do
- kicks, kicked -> kick

### Tiến hành chạy:

Nếu chưa tải, clone repository về từ github: [Earley Algorithms](https://github.com/phucthuan1st/EarleyAlgorithms.git)
Nếu rồi có thể bỏ qua bước 1

- B1: clone repository về từ GitHub

```shell
mkdir Earley
cd Earley
git clone https://github.com/phucthuan1st/EarleyAlgorithms.git
```

- B2: Vào thư mục làm việc

```shell
cd EarleyAlgorithms/src
```

- B3: Tiến hành chạy với cú pháp:

```shell
python main.py [đường dẫn file document] [đường dẫn file JSON grammar]
```

Ví dụ:

```shell
python main.py sample-document.txt grammar.json
```

Khi chạy mà không kèm tham số, mặc định chương trình sẽ lấy dữ liệu từ các file sample-document.txt và sample-grammar.json

Kết quả sẽ tương tự dưới đây:

```c
Table[0]
S0 gamma -> S - operation: dummy start state
S1 S -> NP VP - operation: predictor
S2 S -> NP VP PP - operation: predictor
S3 NP -> d NP3 - operation: predictor

Table[1]
S4 d -> an - operation: scanner
S5 NP -> d NP3 - operation: completer
S6 NP3 -> a NP3 - operation: predictor
S7 NP3 -> n - operation: predictor
S8 NP3 -> n PP - operation: predictor

Table[2]
S9 a -> old - operation: scanner
S10 NP3 -> a NP3 - operation: completer
S11 NP3 -> a NP3 - operation: predictor
S12 NP3 -> n - operation: predictor
S13 NP3 -> n PP - operation: predictor

...

Table[11]
S64 a -> new - operation: scanner
S65 NP3 -> a NP3 - operation: completer
S66 NP3 -> a NP3 - operation: predictor
S67 NP3 -> n - operation: predictor
S68 NP3 -> n PP - operation: predictor

Table[12]
S69 n -> house - operation: scanner
S70 NP3 -> n - operation: completer
S71 NP3 -> n PP - operation: completer
S72 NP3 -> a NP3 - operation: completer
S73 PP -> p NP2 - operation: predictor
S74 NP2 -> d NP3 - operation: completer
S75 NP3 -> n PP - operation: completer
S76 PP -> p NP2 - operation: completer
S77 NP3 -> n PP - operation: completer
S78 NP3 -> a NP3 - operation: completer
S79 NP2 -> d NP3 - operation: completer
S80 PP -> p NP2 - operation: completer
S81 S -> NP VP PP - operation: completer

                 S
      ___________|_______
     |           |       PP
     |           |    ___|___
     |           |   |      NP2
     |           |   |    ___|_________
     |           |   |   |            NP3
     |           |   |   |    _________|___
     |           |   |   |   |            NP3
     |           |   |   |   |     ________|___
     |           |   |   |   |    |            PP
     |           |   |   |   |    |     _______|___
     NP          |   |   |   |    |    |          NP2
  ___|___        |   |   |   |    |    |    _______|___
 |      NP3      |   |   |   |    |    |   |          NP3
 |    ___|___    |   |   |   |    |    |   |        ___|____
 |   |      NP3  VP  |   |   |    |    |   |       |       NP3
 |   |       |   |   |   |   |    |    |   |       |        |
 d   a       n   v   p   d   a    n    p   d       a        n
 |   |       |   |   |   |   |    |    |   |       |        |
 an old     man sit  on the red chair  in the     new     house
```

Trường hợp dữ liệu đưa vào không đúng với văn phạm đã đề ra, sẽ in ra thông báo lỗi:

```php
Invalid state with provided grammar
```

### Requirements

python==3.9.0
nltk==3.6.3

# Framework for testing

## Overview
Mọi người có thể copy framework này về và dùng cho việc test của mình
Xóa những dòng chú thích và những hàm test thừa, đồng thời đổi tên hàm test cho phù hợp công việc cần test để đạt được hiệu quả tốt nhất 

## Installation
```
pip install -r requirements.txt
```

### Run test 
```
python -m pytest --cov=src/ tests/ --cov-branch --cov-report html
```

### Run performance test
```
mprof run tests/performance.py
mprof plot
```
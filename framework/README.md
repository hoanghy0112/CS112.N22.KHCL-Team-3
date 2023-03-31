# Framework for testing

## Overview

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
# Find next day example

## Overview

## Installation
```
pip install -r requirements.txt
```

## Guide

### Run test 
```
python -m pytest --cov=src/ tests/ --cov-branch --cov-report html
```

### Run performance test
```
mprof run tests/performance.py
mprof plot
```
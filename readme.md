
# 🚀 Mastering `pandas.read_csv()` – From Beginner to Data Engineer

## 📌 Why `read_csv()` Matters

Every Data Analyst, Data Scientist, ML Engineer, and Data Engineer starts with one thing:

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

But behind this simple line are powerful parameters that can:

* Reduce memory usage by 80%
* Load million-row datasets
* Handle corrupted files
* Parse dates automatically
* Improve ETL performance
* Optimize Data Engineering pipelines

---

# 🏗 Real-World Workflow

```text
CSV File
    ↓
read_csv()
    ↓
Data Cleaning
    ↓
Feature Engineering
    ↓
Machine Learning
    ↓
Database / Dashboard
```

---

# 1️⃣ Basic CSV Loading

```python
import pandas as pd

df = pd.read_csv("employees.csv")
```

### When to Use

* Small datasets
* Initial exploration
* Kaggle projects

---

# 2️⃣ Reading Data From APIs & URLs

```python
import requests
from io import StringIO

url = "https://example.com/data.csv"

response = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"}
)

data = StringIO(response.text)

df = pd.read_csv(data)
```

## Why Headers?

Without:

```python
requests.get(url)
```

Some servers block requests.

With:

```python
headers={"User-Agent":"Mozilla/5.0"}
```

Server thinks you're a browser.

### Interview Question

**Why do we pass headers?**

Answer:

> Headers provide metadata about the request such as authentication, content type, accepted response format, and client information.

---

# 3️⃣ `usecols` = Performance Hack

```python
df = pd.read_csv(
    "big_data.csv",
    usecols=["name","salary"]
)
```

Instead of loading:

```text
100 columns
```

Load:

```text
2 columns
```

### Benefits

✅ Faster

✅ Less RAM

✅ Better for Production

---

# 4️⃣ `dtype` = Data Engineer Trick

```python
df = pd.read_csv(
    "data.csv",
    dtype={
        "target":"int8"
    }
)
```

### Why?

Default:

```text
int64
```

Memory:

```text
8 Bytes
```

Optimized:

```text
int8
```

Memory:

```text
1 Byte
```

### Impact

For:

```text
10 Million Rows
```

Can save hundreds of MB.

---

# 5️⃣ Parse Dates Automatically

```python
df = pd.read_csv(
    "sales.csv",
    parse_dates=["date"]
)
```

Without:

```text
object
```

With:

```text
datetime64
```

Now you can:

```python
df["date"].dt.year
df["date"].dt.month
```

---

# 6️⃣ Working With Huge Datasets

```python
chunks = pd.read_csv(
    "large.csv",
    chunksize=5000
)
```

```python
for chunk in chunks:
    process(chunk)
```

### Why?

Instead of:

```text
1 GB file
```

Load:

```text
5000 rows at a time
```

### Used In

* ETL Pipelines
* Data Warehouses
* Big Data Processing

---

# 7️⃣ Handling Bad Data

```python
pd.read_csv(
    "books.csv",
    on_bad_lines="skip"
)
```

### Useful When

* Corrupt rows
* Extra delimiters
* Broken CSV exports

---

# 8️⃣ Custom Data Cleaning During Load

```python
def rename(team):
    if team == "Royal Challengers Bangalore":
        return "RCB"
    return team
```

```python
df = pd.read_csv(
    "ipl.csv",
    converters={
        "team1":rename
    }
)
```

### Advantage

Cleaning happens while loading.

No extra processing step.

---

# 9️⃣ Reading TSV Files

```python
pd.read_csv(
    "movies.tsv",
    sep="\t"
)
```

Other separators:

```python
sep=","
sep=";"
sep="|"
sep="\t"
```

---

# 🔥 Most Important Parameters

| Parameter   | Data Engineer Importance |
| ----------- | ------------------------ |
| usecols     | ⭐⭐⭐⭐⭐                    |
| dtype       | ⭐⭐⭐⭐⭐                    |
| parse_dates | ⭐⭐⭐⭐⭐                    |
| chunksize   | ⭐⭐⭐⭐⭐                    |
| converters  | ⭐⭐⭐⭐                     |
| na_values   | ⭐⭐⭐⭐                     |
| encoding    | ⭐⭐⭐⭐                     |
| sep         | ⭐⭐⭐                      |
| header      | ⭐⭐⭐                      |
| index_col   | ⭐⭐⭐                      |

---

# 💼 Interview Questions

### Difference between `nrows` and `chunksize`?

**nrows**

```python
pd.read_csv("data.csv", nrows=1000)
```

Loads only first 1000 rows.

**chunksize**

```python
pd.read_csv("data.csv", chunksize=1000)
```

Loads entire dataset in pieces.

---

### Why use `dtype`?

* Reduce memory
* Faster execution
* Better performance

---

### Why use `parse_dates`?

* Time-series analysis
* Date filtering
* Monthly/Yearly aggregations

---

# 🎯 Key Takeaway

A beginner uses:

```python
pd.read_csv("data.csv")
```

A Data Engineer uses:

```python
pd.read_csv(
    "data.csv",
    usecols=["id","date","sales"],
    dtype={"sales":"float32"},
    parse_dates=["date"],
    chunksize=5000
)
```

The difference is **performance, scalability, and production readiness**. That's what recruiters and interviewers look for. 🚀

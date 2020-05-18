# DPERN - Describe PERsian Numbers

## Installation

```bash
pip install dpern
```

## Usage

If you want to use it in a module, you need to import it like this:

```python
from dpern import dpern
```

And use it like this:

```python
print(dpern.describe(53523))
# پنجاه و سه هزار و پانصد و بیست و سه

print(dpern.describe("35"))
# سی و پنج

print(dpern.describe("۹۹۹"))
# نهصد و نود و نه
```

If you want to use it in the command line, make sure to install it
with `--user` flag:

```bash
pip install dpern --user
```

Then you can run it like this:

```bash
$ python -m dpern 10
ده

$ python -m dpern ۱۲۸
صد و بیست و هشت
```

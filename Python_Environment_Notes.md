# Python Environment Notes for VS Code / Terminal

## 1. Enter the project folder

```bash
cd /Users/zhaozhan/GitHub/genotype-pca-tsne
```

After entering the project folder, run the script with:

```bash
/opt/anaconda3/bin/python vcf_to_matrix.py
```

Instead of writing the full file path every time:

```bash
/opt/anaconda3/bin/python /Users/zhaozhan/GitHub/genotype-pca-tsne/vcf_to_matrix.py
```

---

## 2. Check which Python is used by default

```bash
which python3
```

Example output:

```bash
/opt/anaconda3/bin/python3
```

This means when you type `python3`, the terminal actually uses the Anaconda Python executable.

You can also check all Python paths available in your terminal:

```bash
which -a python3
```

Example output:

```bash
/opt/anaconda3/bin/python3
/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
/usr/local/bin/python3
/usr/bin/python3
```

In this case:

```text
/opt/anaconda3/bin/python3 = Anaconda Python
/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 = Python.org installation
/usr/local/bin/python3 = shortcut/link to Python.org Python 3.13
/usr/bin/python3 = macOS system Python, do not delete or modify
```

---

## 3. Check Python versions

Check the default `python3` version:

```bash
python3 --version
```

Check the Anaconda Python version directly:

```bash
/opt/anaconda3/bin/python --version
```

Example output:

```bash
Python 3.x.x
```

Different Python paths may have the same version but still be different environments.

---

## 4. Check which pip belongs to which Python

Use:

```bash
python3 -m pip --version
```

Or check the Anaconda Python pip directly:

```bash
/opt/anaconda3/bin/python -m pip --version
```

This shows which Python environment the `pip` command belongs to.

---

## 5. Install packages correctly

Do not rely only on:

```bash
pip install pysam
```

Because `pip` may belong to a different Python.

For this project, use the Anaconda Python directly:

```bash
/opt/anaconda3/bin/python -m pip install pysam numpy pandas scikit-learn
```

This means:

```text
Use the pip connected to /opt/anaconda3/bin/python to install packages.
```

If your default `python3` is already Anaconda, this also works:

```bash
python3 -m pip install pysam numpy pandas scikit-learn
```

---

## 6. Run the Python script

After entering the project folder:

```bash
cd /Users/zhaozhan/GitHub/genotype-pca-tsne
```

Run:

```bash
/opt/anaconda3/bin/python vcf_to_matrix.py
```

Or, if your default Python is already Anaconda:

```bash
python3 vcf_to_matrix.py
```

---

## 7. Check which Python is running inside the script

Add this temporarily to the Python file:

```python
import sys
print(sys.executable)
print(sys.version)
```

Then run:

```bash
/opt/anaconda3/bin/python vcf_to_matrix.py
```

Example output:

```bash
/opt/anaconda3/bin/python
Python 3.x.x
```

This confirms exactly which Python is running your script.

---

## 8. Select Python interpreter in VS Code

In VS Code, open the Command Palette:

```text
Command + Shift + P
```

Search:

```text
Python: Select Interpreter
```

Then choose the Anaconda Python interpreter:

```text
/opt/anaconda3/bin/python
```

or:

```text
/opt/anaconda3/bin/python3
```

After selecting it, VS Code should use Anaconda Python to run your `.py` files.

---

## 9. If the VS Code Run button uses the wrong Python

If VS Code runs something like:

```bash
/usr/local/bin/python3 /Users/zhaozhan/GitHub/genotype-pca-tsne/vcf_to_matrix.py
```

That means VS Code is still using the old Python.org Python shortcut.

To change it:

```text
Command + Shift + P
→ Python: Select Interpreter
→ choose /opt/anaconda3/bin/python
```

Then run the file again.

A correct Anaconda run should look like:

```bash
/opt/anaconda3/bin/python /Users/zhaozhan/GitHub/genotype-pca-tsne/vcf_to_matrix.py
```

---

## 10. Recommended setup for this project

Since this project already worked with:

```bash
/opt/anaconda3/bin/python vcf_to_matrix.py
```

Use Anaconda Python consistently for this project.

Install packages with:

```bash
/opt/anaconda3/bin/python -m pip install pysam numpy pandas scikit-learn
```

Run scripts with:

```bash
/opt/anaconda3/bin/python vcf_to_matrix.py
```

Select this interpreter in VS Code:

```text
/opt/anaconda3/bin/python
```

---

## 11. Most important rule

Use the same Python for running code and installing packages.

Example:

```bash
/opt/anaconda3/bin/python vcf_to_matrix.py
```

should match:

```bash
/opt/anaconda3/bin/python -m pip install pysam numpy pandas scikit-learn
```

If you run with:

```bash
python3 vcf_to_matrix.py
```

then install with:

```bash
python3 -m pip install pysam numpy pandas scikit-learn
```

Do not mix different Python environments.

---

## 12. Simple mental model

```text
VS Code = code editor
Python interpreter = program that runs the code
pip = package installer for one specific Python
package = external tool/library, such as pysam, numpy, pandas, scikit-learn
```

The key is:

```text
The Python interpreter and pip must belong to the same environment.
```

---

## 13. Current setup summary

Current project Python:

```bash
/opt/anaconda3/bin/python
```

Current project run command:

```bash
cd /Users/zhaozhan/GitHub/genotype-pca-tsne
/opt/anaconda3/bin/python vcf_to_matrix.py
```

Current package install command:

```bash
/opt/anaconda3/bin/python -m pip install pysam numpy pandas scikit-learn
```

Test command:

```bash
/opt/anaconda3/bin/python -c "from pysam import VariantFile; import numpy as np; import pandas as pd; from sklearn import decomposition; print('Anaconda Python works')"
```

Expected output:

```text
Anaconda Python works
```

Do not delete or modify:

```bash
/usr/bin/python3
```

This is the macOS system Python.
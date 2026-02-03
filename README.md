# Package Description
_This package is built as a submission to_ [Assignment 1](https://github.com/psrana/Assignment-Topsis)

_Submitted by:_ **Shivam Kumar (102303881), 3C63**

*Definition:* TOPSIS, acronym for Technique for Order Preference by Similarity to Ideal Solution, is a multi-criteria decision-making (MCDM) method used to rank alternatives by selecting the option that is closest to the ideal solution and farthest from the worst (negative ideal) solution.

### Use this package as a [WebApp](https://shivamkmr.pythonanywhere.com/) here.

<br>

## ✅ **Installation**
Use the package manager pip to install topsis-shivam-102303881
```bash
pip install topsis-shivam-102303881
```

## ⚙️ **Usage**
```bash
topsis data.csv 1,1,1,2,1 +,+,+,-,+ result.csv
```
where,
- **data.csv** is your input file  
- Weights to be assigned to each feature  
- Impacts to optimize each feature (`'+'`: Maximize, `'-'`: Minimize)  
- Output file path to save the results  

<br>

## 🪴**Example**

weights = [1,1,1,2,1]  
impacts = [+,+,+,-,+]

<table>
<tr>
  <th>Input Dataset</th>
  <th>TOPSIS Output</th>
</tr>
<tr>
<td>

📄 **data.csv**

| Fund Name | P1  | P2  | P3 | P4  | P5   |
|----------|-----|-----|----|-----|------|
| M1 | 0.82 | 0.67 | 5.8 | 61.9 | 17.3 |
| M2 | 0.73 | 0.53 | 3.5 | 35.8 | 10.14 |
| M3 | 0.64 | 0.41 | 5.7 | 45.1 | 12.96 |
| M4 | 0.81 | 0.66 | 6.3 | 54.6 | 15.59 |
| M5 | 0.7 | 0.49 | 6.9 | 63.6 | 17.92 |
| M6 | 0.78 | 0.61 | 3.3 | 64.4 | 17.27 |
| M7 | 0.62 | 0.38 | 5.8 | 68.3 | 18.78 |
| M8 | 0.69 | 0.48 | 6.6 | 37.8 | 11.39 |

</td>
<td>

📊 **result.csv**
  
| Fund Name | P1  | P2  | P3 | P4  | P5   | Topsis Score | Rank |
|----------|-----|-----|----|-----|------|--------------|------|
| M1 | 0.82 | 0.67 | 5.8 | 61.9 | 17.3 | 0.4845 | 5 |
| M2 | 0.73 | 0.53 | 3.5 | 35.8 | 10.14 | 0.5832 | 2 |
| M3 | 0.64 | 0.41 | 5.7 | 45.1 | 12.96 | 0.5549 | 4 |
| M4 | 0.81 | 0.66 | 6.3 | 54.6 | 15.59 | 0.5806 | 3 |
| M5 | 0.7 | 0.49 | 6.9 | 63.6 | 17.92 | 0.4453 | 6 |
| M6 | 0.78 | 0.61 | 3.3 | 64.4 | 17.27 | 0.3568 | 7 |
| M7 | 0.62 | 0.38 | 5.8 | 68.3 | 18.78 | 0.3479 | 8 |
| M8 | 0.69 | 0.48 | 6.6 | 37.8 | 11.39 | 0.6696 | 1 |  

</td>
</tr>
</table>

<br>

## 🗒️ **Notes**

### The package handles the following:

- Correct number of parameters (inputFileName, Weights, Impacts, resultFileName).
- Show the appropriate message for wrong inputs.
- Handling of "File not Found" exception
- The input file must contain three or more columns.
- From 2nd to last columns must contain numeric values only (Handling of non-numeric values)
- The number of weights, number of impacts and number of columns (from 2nd to last columns) must be the same.
- Impacts must be either +ve or -ve.
- Impacts and weights must be separated by ',' (comma).

## **License**

[MIT Licence](https://github.com/shivamkumar/Assignment-1-L1/blob/main/LICENSE.txt)

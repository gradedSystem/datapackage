# Part II: Data Packages
# Data Cleaning and Preparation Checklist

Before starting any data analysis or modeling, it's essential to ensure that your data is clean and well-prepared. Follow this checklist to make sure your data is in the right shape for analysis.

## 1. Remove Comments from Data Files

- Check your data files for any comments or non-data information.
- Move any comments you find into a separate README file or document.

## 2. Eliminate Empty Rows

- Scan your data files for empty rows.
- Remove any empty rows to avoid skewing your analysis.

## 3. Unpivot Tables

Pivoting and unpivoting are data transformation techniques used to restructure tabular data. Here's a brief explanation:

- **Pivot:** Pivoting involves converting rows into columns to create a summary table. It's useful for aggregating data.
- **Unpivot:** Unpivoting is the reverse process, where you convert columns back into rows, making the data more suitable for analysis.

Depending on your analysis needs, decide whether to pivot or unpivot your data tables.

## 4. Use Periods (.) as Decimal Separators

- Ensure that decimal values in your data are represented using periods (.) rather than commas (,).
- This standardizes the format and prevents issues during analysis.

## 5. Handle Missing Data

- If data is missing, decide on an appropriate way to handle it:
  - You can mark missing cells as '0' if it makes sense in the context of your analysis.
  - Alternatively, use 'NaN' (Not-a-Number) to indicate missing or undefined values.

## 6. Data Package and Resource Naming Convention

- When naming your data package and resources (data files), use hyphens (-) instead of spaces.
  - For example: `gold-prices/data/prices.csv` is preferred over `gold prices/data/prices.csv`.

By following this checklist, you'll ensure that your data is clean, organized, and ready for analysis, setting the foundation for meaningful insights and accurate modeling.

## 7. Validating the data and pushing it to the datahub.io
- Validating the `datapackage.json` is done succesfully in the local repository, however facing the issues with pushing and validating the datapackage due to the given problem:
  - Here is the issue of packaging: Updating from 0.9.5 -> 0.10.1 [data-cli-issue-380](https://github.com/datopian/data-cli/issues/380)
### Output: 
  <div style="text-align:center">
    <img src="https://raw.githubusercontent.com/gradedSystem/datapackage/main/images/img.png" alt="Image Description" />
  </div>


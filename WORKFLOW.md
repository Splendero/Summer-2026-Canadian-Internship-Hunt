# Data Pipeline Workflow

This repository now uses a data pipeline to automatically generate the README.md from a CSV file, making it much easier to update and maintain.

## Files Overview

- `internships.csv` - Source data file containing all internship listings
- `generate_readme.py` - Python script that converts CSV to README.md
- `update_readme.bat` - Windows batch file for easy updates
- `README.md` - Generated file (DO NOT EDIT MANUALLY)
- `WORKFLOW.md` - This documentation file

## How to Update the README

### Method 1: Using the Batch Script (Recommended for Windows)
1. Edit `internships.csv` with your new data
2. Double-click `update_readme.bat`
3. The README will be automatically updated

### Method 2: Using Python Directly
1. Edit `internships.csv` with your new data
2. Run: `python generate_readme.py`
3. The README will be automatically updated

## CSV File Format

The `internships.csv` file should have the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| Company | Company name | "RBC Amplify" |
| Role | Job title/role | "Software Engineering Intern" |
| Location | City/office location | "Toronto" |
| Application URL | Direct link to application | "https://company.com/job/123" |
| Date Posted | When the job was posted | "2025-09-17" |
| Status | Current status | "Open", "Applied", "Closed", etc. |
| Applied | Whether you've applied | "Yes", "No" |

## Adding New Internships

1. Open `internships.csv` in Excel, Google Sheets, or any text editor
2. Add a new row with the internship details
3. Run the update script to regenerate the README

## Updating Existing Internships

1. Find the row in `internships.csv` for the internship you want to update
2. Modify the relevant fields (e.g., change Status from "Open" to "Applied")
3. Update the "Applied" column to "Yes" when you submit an application
4. Run the update script to regenerate the README

### Applied Column Values
- **"Yes"** - You have applied to this position (displays as ✅ Yes)
- **"No"** - You have not applied yet (displays as ❌ No)
- The script recognizes various formats: "Yes", "Y", "True", "1" for applied status

## Benefits of This Approach

- ✅ **Easy Updates**: Just edit the CSV file and run one command
- ✅ **Consistent Formatting**: The README is always properly formatted
- ✅ **No Manual HTML**: No need to write HTML table markup
- ✅ **Version Control Friendly**: CSV is easier to track changes in Git
- ✅ **Bulk Operations**: Easy to add/remove multiple entries
- ✅ **Data Validation**: Can add validation rules in the Python script
- ✅ **Automation Ready**: Can be integrated with GitHub Actions or other CI/CD

## Advanced Usage

### Customizing the Output
You can modify `generate_readme.py` to:
- Add new columns to the table
- Change the table styling
- Add filters (e.g., only show "Open" positions)
- Sort by different criteria
- Add statistics (e.g., count by company)

### Adding Validation
The script can be extended to validate:
- Required fields are not empty
- URLs are properly formatted
- Dates are in correct format
- Status values are from a predefined list

## Troubleshooting

### Common Issues
1. **CSV not found**: Make sure `internships.csv` is in the same directory
2. **Python not found**: Install Python 3.6+ or use full path to python.exe
3. **Permission denied**: Make sure you have write permissions for README.md
4. **Encoding issues**: The script uses UTF-8 encoding for international characters

### Getting Help
- Check that all required columns exist in your CSV
- Ensure there are no special characters breaking the CSV format
- Verify that URLs are properly formatted

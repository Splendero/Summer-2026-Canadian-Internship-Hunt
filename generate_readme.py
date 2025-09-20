#!/usr/bin/env python3
"""
Data Pipeline Script for Summer 2026 Internship Hunt
Generates README.md from internships.csv data
"""

import csv
import os
from datetime import datetime

def read_internships_data(csv_file='internships.csv'):
    """Read internship data from CSV file"""
    internships = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                internships.append(row)
    except FileNotFoundError:
        print(f"Error: {csv_file} not found!")
        return []
    except Exception as e:
        print(f"Error reading {csv_file}: {e}")
        return []
    
    return internships

def generate_markdown_table(internships):
    """Generate markdown table from internship data"""
    if not internships:
        return "No internship data available."
    
    # Table header
    markdown = """<table>
<thead>
<tr>
<th>Company</th>
<th>Role</th>
<th>Location</th>
<th>Application</th>
<th>Date Posted</th>
<th>Status</th>
<th>Applied</th>
</tr>
</thead>
<tbody>
"""
    
    # Table rows
    for internship in internships:
        company = internship.get('Company', '').strip()
        role = internship.get('Role', '').strip()
        location = internship.get('Location', '').strip()
        application_url = internship.get('Application URL', '').strip()
        date_posted = internship.get('Date Posted', '').strip()
        status = internship.get('Status', '').strip()
        applied = internship.get('Applied', '').strip()
        
        # Create application button if URL exists
        if application_url:
            application_cell = f'<a href="{application_url}"><button>Apply</button></a>'
        else:
            application_cell = 'N/A'
        
        # Format applied status with emoji for better visibility
        applied_display = "✅ Yes" if applied.lower() in ['yes', 'y', 'true', '1'] else "❌ No"
        
        # Add row to table
        markdown += f"""<tr>
<td><strong>{company}</strong></td>
<td>{role}</td>
<td>{location}</td>
<td>{application_cell}</td>
<td>{date_posted}</td>
<td>{status}</td>
<td>{applied_display}</td>
</tr>
"""
    
    markdown += """</tbody>
</table>"""
    
    return markdown

def generate_readme(internships):
    """Generate complete README content"""
    table_content = generate_markdown_table(internships)
    
    readme_content = f"""# Summer-2026-Internship-Hunt

{table_content}

---
*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*Generated from internships.csv*
"""
    
    return readme_content

def main():
    """Main function to generate README from CSV"""
    print("🔄 Generating README from internships.csv...")
    
    # Read data from CSV
    internships = read_internships_data()
    
    if not internships:
        print("❌ No data found. Please check internships.csv file.")
        return
    
    print(f"📊 Found {len(internships)} internship listings")
    
    # Generate README content
    readme_content = generate_readme(internships)
    
    # Write to README.md
    try:
        with open('README.md', 'w', encoding='utf-8') as file:
            file.write(readme_content)
        print("✅ README.md updated successfully!")
    except Exception as e:
        print(f"❌ Error writing README.md: {e}")

if __name__ == "__main__":
    main()

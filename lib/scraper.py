from bs4 import BeautifulSoup
import requests

# Set headers to avoid 403 Forbidden errors
headers = {'user-agent': 'my-app/0.0.1'}

# Fetch the HTML content from Flatiron School's website
html = requests.get("https://flatironschool.com/", headers=headers)

# Create a Beautiful Soup object to parse the HTML
doc = BeautifulSoup(html.text, 'html.parser')

# Example 1: Select elements with a specific class
# This selects the heading with class 'heading-financier'
heading_elements = doc.select('.heading-financier')

if heading_elements:
    print("Example 1 - Heading with class 'heading-financier':")
    print(heading_elements[0].contents[0].strip())
    print()

# Example 2: Scraping course information from the courses page
html_courses = requests.get("https://flatironschool.com/our-courses/", headers=headers)
doc_courses = BeautifulSoup(html_courses.text, 'html.parser')

# Select course titles
courses = doc_courses.select('.heading-60-black.color-black.mb-20')

if courses:
    print("Example 2 - Course Listings:")
    for course in courses:
        print(course.contents[0].strip())
    print()

# Example 3: Demonstrating tag attributes
if courses:
    print("Example 3 - Element Properties:")
    first_course = courses[0]
    print(f"Tag name: {first_course.name}")
    print(f"Tag attributes: {first_course.attrs}")
    print()

print("Web scraping examples completed!")

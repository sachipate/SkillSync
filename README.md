# SkillSync

#### Video Demo: 

## Description

SkillSync is a tool that I’ve built to help people see how well their resume matches their desired job description. I wrote the entire project in Python. SkillSync looks at both the resume and the job description to find the skills that are the same. Then it gives a report that shows the skills that match and the ones that do not. The goal of SkillSync is to make it easy for people to understand what skills they already have and what skills they need to learn or add to their resume.

When I was making SkillSync, I wanted to make sure it could work with different types of resume files.I wanted to have a system where it can read text files as well as PDF files. So, I made a program where the text is read using Python, whereas the PDF files are read by extracting the text using a special library called pypdf. This way the program can work with either type of file. After extraction of the text from the pdf, both the pdf and text go through the same pipeline and give the same results.

First the program asks the user for their resume file and the job description file. Then it reads the files. Another function then makes the text cleaner by making everything lowercase and removing extra punctuation. This helped the program match skills more accurately because it did not get confused by capitalization or formatting.

Once the text has been cleaned, SkillSync compares it against a list of skills stored in the skills.txt file. It checks both the resume and the job description to see which of those skills are present. To do this, I used regular expressions, as they allow the program to accurately identify both single-word skills and multi-word skills such as "Power BI". I chose this approach because it reduces incorrect matches while still keeping the skill extraction process simple and reliable.

Once the program finds the skills in both documents it compares them to see which skills are in the resume and which are missing. It calculates a percentage to show how well the resume matches the job description. Finally, it gives a report that shows the matched skills, the missing skills and the percentage match.


## Files

### `project.py`

This file has all the code for the program. It can read text and PDF files, clean the text, find the skills, calculate the match percentage and give the report. Each part of the program is in its section to make it easier to understand.

### `test_project.py`

This file has tests to make sure the program works correctly. It checks that the text cleaning, the skill finding, and it also checks for word and multi-word skills and whether the match calculation is correct. These tests help make sure that changes to one part of the program do not break another part.

### `skills.txt`

The ‘skills.txt’ file has a list of skills that the programmer has stored. It is very convenient to add skills to this file without changing the program code. The program loads this file when it starts.

### `requirements.txt`

This file lists the libraries that the program needs to run. This project needs pypdf to read PDF files and pytest to run the tests.


## Design Choices

One of the decisions I made was how to store the skills inside the program. I used the Python sets because it automatically removes duplicates and makes comparisons faster. This makes it easy to compare the skills in the resume with the skills in the job description.

Another important decision I took was to support skills with multiple words. At first I just split the resume into words and compared each word to the skills list. This did not work for skills like "Power BI" and “Machine learning” because they have multiple words. So, I changed the program to use expressions to search for the skills. Using this, the program can find both word and multi-word skills.

I also thought about putting the list of skills in the program code. But then I decided to put it in a separate file called `skills.txt` instead. This makes it easy to add skills without changing the  core program code. It also helps to keep the code cleaner as it separates the data from the program logic.

Finally, I decided to add support for PDF files because most resumes are in PDF format and this made the program more useful for real-world application or use. By keeping the file-reading code separate, the rest of the program can work with text regardless of the original file format.

Overall, SkillSync demonstrates file handling, text processing, regular expressions, error handling, third-party libraries, unit testing, and modular program design. It provides a simple and effective way to compare resumes against job descriptions using Python.

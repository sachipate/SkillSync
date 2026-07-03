import sys
import string
from pypdf import PdfReader
import re

def main():
    resume=input("Upload your Resume: ")
    if resume.endswith(".txt"):
        resume_text=get_file(resume)
    elif resume.endswith(".pdf"):
        resume_text=get_text_from_pdf(resume)
    else:
        sys.exit("Invalid file format")
    resume_text=clean_text(resume_text)

    job_description=input("Upload the Job Description: ")
    if job_description.endswith(".txt"):
        job_text=get_file(job_description)
    elif job_description.endswith(".pdf"):
        job_text=get_text_from_pdf(job_description)
    else:
        sys.exit("Invalid file format")
    job_text=clean_text(job_text)

    skills=get_skills()

    resume_skills=extract_skills(resume_text,skills)
    job_skills=extract_skills(job_text,skills)

    try:
        matched_skills, missing_skills, match_percent = calculate_match(resume_skills, job_skills)
    except ValueError as e:
        sys.exit(str(e))

    generate_report(matched_skills,missing_skills,match_percent)

def get_file(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            text=f.read()
            return text

    except FileNotFoundError:
        sys.exit("File not found")

def get_text_from_pdf(pdf):
    reader=PdfReader(pdf)
    text=""
    page=reader.pages
    for p in page:
        text+=p.extract_text() or ""
    return text

def clean_text(text):
    text=text.lower()
    text=text.strip()
    cleaned_text=""
    special_characters=string.punctuation
    for ch in text:
        if ch not in special_characters or ch=="-" or ch==".":
            cleaned_text+=ch
    cleaned_text=cleaned_text.strip()
    cleaned_text=" ".join(cleaned_text.split())
    return cleaned_text

def get_skills():
    skills=set()
    try:
        with open("skills.txt") as file:
            for skill in file:
                skill=skill.strip()
                if skill:
                    skills.add(skill)
    except FileNotFoundError:
        sys.exit("No skills file found")
    return skills

def extract_skills(text,skills):
    matched_skills=set()
    for skill in skills:
        pattern=r"\b"+re.escape(skill)+r"\b"
        if re.search(pattern,text):
            matched_skills.add(skill)
    return matched_skills

def calculate_match(resume_skills, job_skills):
    matched_skills=set()
    missing_skills=set()
    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.add(skill)
        else:
            missing_skills.add(skill)
    match_percent=len(matched_skills)/len(job_skills)*100
    return matched_skills, missing_skills, match_percent

def generate_report(matched,missing,percent):
    print("Matched Skills")
    print("---------------")
    for skill in sorted(matched):
        print("✓",skill)
    print()

    print("Missing Skills")
    print("---------------")
    for skill in sorted(missing):
        print("✗",skill)
    print()

    print(f"Overall Match: {percent:.2f}%")

if __name__=="__main__":
    main()

from project import clean_text, extract_skills, calculate_match

def test_clean_text():
    assert clean_text("PYTHON!, Java")=="python java"
    assert clean_text("Node.js")=="node.js"
    assert clean_text("Front-end")=="front-end"

def test_extract_skills_single_word():
    text=clean_text("I learned python from CS50")
    skills={"python"}
    assert extract_skills(text,skills)=={"python"}

    text=clean_text("Requirements: HTML, CSS, Javascript")
    skills={"html", "css","javascript"}
    assert extract_skills(text,skills)=={"html", "css", "javascript"}

    text=clean_text("I have good Leadership and Communication skills")
    skills={"python", "java"}
    assert extract_skills(text,skills)==set()

def test_extract_skills_multiple_word():
    skills={"node.js", "front-end"}
    text=clean_text("I know node.js in front-end")
    assert extract_skills(text,skills)=={"node.js", "front-end"}

    skills={"power bi"}
    text=clean_text("Power bi is a necessary requirement for the job")
    assert extract_skills(text,skills)=={"power bi"}

def test_calculate_match():
    resume_skills={"python", "java"}
    job_skills={"python", "git", "docker", "java"}
    assert calculate_match(resume_skills, job_skills)==({"python", "java"}, {"git", "docker"}, 50.0)

    resume_skills={"html"}
    job_skills={"html", "css", "javascript", "node.js"}
    assert calculate_match(resume_skills, job_skills)==({"html"}, {"css", "javascript", "node.js"}, 25.0)

def test_calculate_match_no_match():
    resume_skills={"python", "c"}
    job_skills={"aws", "kubernetes", "flask", "django"}
    assert calculate_match(resume_skills, job_skills)==(set(), {"aws", "kubernetes", "flask", "django"}, 0.0)

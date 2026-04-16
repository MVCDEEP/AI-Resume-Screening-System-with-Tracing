print("Program started...")

from chains.extract_chain import extract_chain
from chains.match_chain import match_chain
from chains.score_chain import score_chain


def load_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def run_pipeline(resume, job):

    print("Running extraction...")
    extracted = extract_chain().invoke({
        "resume": resume
    })
    print("Extraction done")

    print("Running matching...")
    matched = match_chain().invoke({
        "resume_data": extracted,
        "job_description": job
    })
    print("Matching done")

    print("Running scoring...")
    scored = score_chain().invoke({
        "match_data": matched
    })
    print("Scoring done")

    return scored


if __name__ == "__main__":

    print("Loading files...")

    resume = load_file("data/strong_resume.txt")
    job = load_file("data/average_resume.txt")

    result = run_pipeline(resume, job)

    print("\nFINAL RESULT:")
    print(result)
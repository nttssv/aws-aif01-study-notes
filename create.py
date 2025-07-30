import os

# Root-level files
root_files = [
    "index.html",
    "README.md",
    ".gitignore"
]

# Top-level folders and any default files
subfolders = {
    "css": ["style.css"],
    "img": [],
    "practice-exams": ["exam1.html", "exam2.html", "answer-key.md"]
}

# AWS AIF-01 Domains with folders + files
domains = {
    "domain1-fundamentals-ai-ml": "Domain 1: Fundamentals of AI and ML of the AWS",
    "domain2-generative-ai": "Domain 2: Fundamentals of Generative AI of the AWS",
    "domain3-foundation-models": "Domain 3: Applications of Foundation Models of the AWS",
    "domain4-responsible-ai": "Domain 4: Guidelines for Responsible AI of the AWS",
    "domain5-security-governance": "Domain 5: Security, Compliance, and Governance for AI Solutions of the AWS"
}

# Create root-level files
for file in root_files:
    with open(file, "w") as f:
        f.write(f"<!-- {file} -->\n")

# Create subfolders and their files
for folder, files in subfolders.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        with open(os.path.join(folder, file), "w") as f:
            f.write(f"<!-- {file} -->\n")

# Create domain-specific folders
os.makedirs("domains", exist_ok=True)

for folder, title in domains.items():
    path = os.path.join("domains", folder)
    os.makedirs(path, exist_ok=True)

    with open(os.path.join(path, "review.html"), "w") as f:
        f.write(f"<!-- {title} - Review Notes -->\n")

    with open(os.path.join(path, "practice.html"), "w") as f:
        f.write(f"<!-- {title} - Flashcards & Practice Questions -->\n")

print("✅ Full AWS AIF-01 project structure created!")
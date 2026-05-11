import json
import random
from pathlib import Path


# =========================
# Load Domain Mapping JSON
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent
json_path = BASE_DIR / "data" / "domain_mapping.json"

with open(json_path, "r") as f:
    mapping = json.load(f)


# =========================
# Validate Mapping
# =========================

def validate_mapping(mapping_data):

    # Check empty mapping
    if not mapping_data:
        raise Exception("Empty mapping")

    for domain, topics in mapping_data.items():

        # Check empty topics
        if not topics:
            raise Exception(f"{domain} has no topics")

        for topic, subtopics in topics.items():

            # Check empty subtopics
            if not subtopics:
                raise Exception(f"{topic} has no subtopics")

            # Minimum subtopics validation
            if len(subtopics) < 3:
                raise Exception(f"{topic} needs minimum 3 subtopics")

    return True


# =========================
# Generate Question Context
# =========================

def generate_question_context(domain):

    # Unknown domain fallback
    if domain not in mapping:
        print(f"Unknown domain '{domain}' detected.")
        print("Fallback applied: DSA\n")
        domain = "DSA"

    # Select random topic
    topic = random.choice(list(mapping[domain].keys()))

    # Select random subtopic
    subtopic = random.choice(mapping[domain][topic])

    return {
        "domain": domain,
        "topic": topic,
        "subtopic": subtopic
    }


# =========================
# Generate Prompt
# =========================

def generate_prompt(context):

    prompt = f"""
Generate one interview question from:

Domain: {context['domain']}
Topic: {context['topic']}
Subtopic: {context['subtopic']}
"""

    return prompt


# =========================
# Main Execution
# =========================

try:

    # Validate JSON mapping
    validate_mapping(mapping)

    print("Mapping Validation Successful\n")

    # Test Domains
    domains_to_test = [
        "DSA",
        "Machine Learning",
        "Web Development",
        "Operating Systems",
        "Computer Networks",
        "Blockchain"   # Unknown domain test
    ]

    for domain in domains_to_test:

        print("=" * 50)

        # Generate hierarchy
        context = generate_question_context(domain)

        print("Generated Context:")
        print(context)

        print("\nGenerated Prompt:")

        # Generate prompt
        prompt = generate_prompt(context)

        print(prompt)

        print("=" * 50)
        print()

except Exception as e:

    print(f"Validation Error: {e}")
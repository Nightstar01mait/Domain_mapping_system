# Domain Mapping System

## Objective

The Domain Mapping System is designed to ensure that generated interview questions are domain-specific, structured, and logically categorized.

The system prevents unrelated or random question generation by using a hierarchical mapping structure.

---

## Hierarchy Structure

The system follows this hierarchy:

Domain → Topic → Subtopic

Example:

DSA → Trees → Binary Search Tree

Machine Learning → Supervised Learning → Random Forest

---

## Domains Included

The system currently supports the following domains:

1. DSA
2. Machine Learning
3. Web Development
4. Operating Systems
5. Computer Networks

---

## Features

- Structured domain hierarchy
- Random topic and subtopic selection
- Unknown domain fallback handling
- Validation system for hierarchy integrity
- Prompt generation support

---

## Validation Rules

The validator ensures:

- Mapping cannot be empty
- Every domain must contain topics
- Every topic must contain subtopics
- Minimum 3 subtopics are required per topic
- No undefined categories are generated

---

## Unknown Domain Handling

If an unknown domain is requested, the system automatically falls back to the default domain:

DSA

Example:

Input:
Blockchain

Output:
DSA → Linked Lists → List Reversal

---

## Question Generation Flow

1. Select Domain
2. Select Topic
3. Select Subtopic
4. Generate Prompt

Example Prompt:

Generate one interview question from:

Domain: DSA
Topic: Graphs
Subtopic: Shortest Path

---

## Project Structure
```text
project/
│
├── data/
│   └── domain_mapping.json
│
├── services/
│   └── question_generator.py
│
├── validators/
│   └── hierarchy_validator.py
│
└── docs/
    └── hierarchy_design.md
---

## Benefits

- Prevents unrelated question generation
- Maintains consistent categorization
- Improves scalability
- Simplifies prompt engineering
- Ensures valid hierarchy mapping
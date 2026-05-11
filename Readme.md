# Domain Mapping System

## Overview

The Domain Mapping System is designed to generate structured and domain-specific interview question contexts using a hierarchical mapping approach.

The system ensures that every generated question belongs to a valid:

- Domain
- Topic
- Subtopic

This prevents unrelated or random question generation.

---

# Objective

The main objective of this project is to:

- Maintain structured knowledge hierarchy
- Ensure domain relevance
- Prevent invalid category generation
- Support scalable question generation systems

---

# Hierarchy Structure

The system follows the hierarchy below:

```text
Domain → Topic → Subtopic
```

### Example

```text
DSA → Trees → Binary Search Tree
```

```text
Machine Learning → Supervised Learning → Random Forest
```

---

# Domains Included

The project currently supports:

1. DSA
2. Machine Learning
3. Web Development
4. Operating Systems
5. Computer Networks

---

# Features

- Structured domain hierarchy
- Random topic and subtopic generation
- Unknown domain fallback handling
- Validation system for hierarchy integrity
- Prompt generation support
- Scalable JSON-based architecture

---

# Project Structure

```text
Domain_Mapping_System/
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
```

---

# Components

## 1. domain_mapping.json

Contains the complete hierarchy structure.

Example:

```json
{
  "DSA": {
    "Arrays": [
      "Two Pointer",
      "Sliding Window",
      "Prefix Sum"
    ]
  }
}
```

---

## 2. question_generator.py

Responsible for:

- Selecting domain
- Selecting topic
- Selecting subtopic
- Generating prompt context

### Example Output

```python
{
  'domain': 'DSA',
  'topic': 'Graphs',
  'subtopic': 'Shortest Path'
}
```

---

## 3. hierarchy_validator.py

Validates:

- Empty mapping
- Missing topics
- Missing subtopics
- Minimum subtopic count

---

# Validation Rules

The validator ensures:

- Mapping cannot be empty
- Every domain must contain topics
- Every topic must contain subtopics
- Minimum 3 subtopics required
- No undefined categories generated

---

# Unknown Domain Handling

If an invalid domain is requested, the system automatically falls back to:

```text
DSA
```

### Example

Input:

```text
Blockchain
```

Output:

```text
DSA → Linked Lists → List Reversal
```

---

# Question Generation Flow

```text
Select Domain
        ↓
Select Topic
        ↓
Select Subtopic
        ↓
Generate Prompt
```

---

# Example Prompt

```text
Generate one interview question from:

Domain: DSA
Topic: Trees
Subtopic: Binary Search Tree
```

---

# How to Run

## Run Validator

```bash
python validators/hierarchy_validator.py
```

Expected Output:

```text
True
```

---

## Run Question Generator

```bash
python services/question_generator.py
```

---

# Benefits

- Prevents unrelated question generation
- Maintains consistent hierarchy
- Improves scalability
- Supports structured prompt engineering
- Ensures valid category mapping

---

# Future Improvements

- Difficulty levels
- Dynamic question generation
- Tag-based filtering
- CLI support
- Database integration
- AI-based question generation

---

# Author

Gaurav Raj
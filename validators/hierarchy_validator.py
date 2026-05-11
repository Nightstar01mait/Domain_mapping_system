import json

def validate_mapping(mapping):

    if not mapping:
        raise Exception("Empty mapping")

    for domain, topics in mapping.items():

        if not topics:
            raise Exception(f"{domain} has no topics")

        for topic, subtopics in topics.items():

            if not subtopics:
                raise Exception(f"{topic} has no subtopics")

            if len(subtopics) < 3:
                raise Exception(f"{topic} needs minimum 3 subtopics")

    return True


with open("../data/domain_mapping.json", "r") as f:
    mapping = json.load(f)

print(validate_mapping(mapping))
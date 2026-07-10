def search_knowledge(question):

    with open(
        "knowledge.txt",
        "r",
        encoding="utf-8"
    ) as file:

        text = file.read()

    sections = text.split("[")

    question = question.lower()

    keywords = {
        "kernel": "KERNEL",
        "flashcast": "FLASHCAST",
        "froben": "FROBEN",
        "fermah": "WHAT_IS_FERMAH"
    }

    for word, section_name in keywords.items():

        if word in question:

            for section in sections:

                if section_name in section.upper():

                    return section

    return "I could not find information about that topic."
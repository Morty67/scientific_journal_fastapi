def generate_content(author):
    author_initials = f"{author.name[0]}{author.surname[0]}"
    digits = "".join(str(item) for item in range(1, 10))
    content_identifier = f"{author_initials}{digits}"
    return content_identifier

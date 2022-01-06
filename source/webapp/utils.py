def article_validate(description, detailed_description, create_until, status):
    errors = {}
    if not description:
        errors['description'] = "The description field is required."
    elif len(description) > 200:
        errors['description'] = "Description's len must be less than 200!!!"
    if not detailed_description:
        errors['detailed_description'] = "Detailed description field is required"
    elif len(detailed_description) > 3000:
        errors['detailed_description'] = "Detailed description's len must be less than 3000!!!"
    if not create_until:
        errors['create_until'] = "Create until field is required."
    if not status:
        pass
    return errors
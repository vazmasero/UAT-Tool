def validate_bug_data(data):
    """Validates bug data."""
    if not data.get('title'):
        raise ValueError("Bug title is required.")
    # Add more validation rules as needed
    return True

def validate_requirement_data(data):
    """Validates requirement data."""
    if not data.get('name'):
        raise ValueError("Requirement name is required.")
    # Add more validation rules as needed
    return True

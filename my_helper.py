def ensure_headers(sheet, expected_headers):
    """
    Ensures the sheet has the correct headers in the first row.
    Returns True if headers were added or correct, False if there's a mismatch.
    """
    current_headers = sheet.row_values(1) if sheet.get_all_values() else []
    
    # If sheet is empty, add headers
    if not current_headers:
        sheet.append_row(expected_headers)
        return True
        
    # If headers exist, verify they match
    if current_headers == expected_headers:
        return True
        
    # If headers exist but don't match, log the mismatch
    mismatched = set(current_headers) ^ set(expected_headers)
    print(f"Header mismatch found. Difference: {mismatched}")
    return False

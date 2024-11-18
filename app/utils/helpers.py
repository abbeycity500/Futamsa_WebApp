# utils/helpers.py

from flask import flash

def flash_errors(form):
    """Flashes form errors to the user."""
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Error in the {getattr(form, field).label.text} field - {error}", 'danger')

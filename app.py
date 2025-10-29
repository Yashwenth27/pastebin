import os
from flask import Flask, Response

# --- YOUR FIXED TEXT ---
# Place your entire fixed text file content inside the triple quotes.
# Make sure to handle any special characters (like backslashes) correctly.
# For example, if your text has a backslash, you might need to escape it (e.g., C:\\Users)
# or use a raw string by putting an 'r' before the quotes (e.g., r"""...""").
FIXED_TEXT_CONTENT = r"""
Hello, this is your hardcoded text.

You can paste any content you want here.
It will be returned as plain text when you
access the URL.

Special characters like \ and " are handled
because this is a raw string.

- Line 1
- Line 2
- Line 3

End of file.
"""

app = Flask(__name__)

@app.route('/')
def get_fixed_text():
    """
    This endpoint serves the hardcoded text file content.
    Setting mimetype to 'text/plain' ensures that browsers
    (and tools like curl) treat it as plain text, not HTML.
    """
    return Response(FIXED_TEXT_CONTENT, mimetype='text/plain')

if __name__ == "__main__":
    # Render sets the PORT environment variable.
    # We use '5000' as a default if running locally.
    port = int(os.environ.get('PORT', 5000))
    
    # '0.0.0.0' makes the app accessible from outside the container,
    # which is required by Render.
    app.run(host='0.0.0.0', port=port)

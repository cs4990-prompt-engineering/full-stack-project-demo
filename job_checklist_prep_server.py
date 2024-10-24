from flask import Flask, request, jsonify, render_template_string
from openai import OpenAI
import os

# Set your OpenAI API key globally (or read from environment variable)
api_key = "your key"

# Initialize the OpenAI client globally
client = OpenAI(api_key=api_key)

# Initialize the Flask app
app = Flask(__name__)

# Function to generate the job preparation checklist
def generate_job_preparation_checklist(job_description):
    """
    Generates a preparation checklist based on a given job description using the OpenAI API.

    Args:
    - job_description (str): The full job description for the position.

    Returns:
    - str: The generated preparation checklist.
    """
    # Define the prompt with the provided job description
    job_checklist_prompt = (
        "I will be providing a full job description. Please generate a checklist for me to learn and prepare for this job interview. "
        "This is for a college CS major student to use. Please keep the checklist simple and concise. For each item, please provide a reference or URL for the student to use and learn. \n"
        "-------------\n" + job_description
    )

    # Call the OpenAI API to generate the checklist
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": job_checklist_prompt}
        ]
    )

    # Extract and return the generated checklist from the API response
    return completion.choices[0].message.content

# Define the API route to receive the job description and return the checklist
@app.route('/generate-checklist', methods=['POST'])
def generate_checklist():
    # Get the job description from the POST request JSON data
    data = request.json
    job_description = data.get("job_description", "")

    if not job_description:
        return jsonify({"error": "Job description is required"}), 400

    # Generate the checklist using the function
    checklist = generate_job_preparation_checklist(job_description)

    # Return the generated checklist as a JSON response
    return jsonify({"checklist": checklist}), 200

# Serve the landing page with the form
@app.route('/')
def index():
    return render_template_string(open('templates/index.html').read())

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

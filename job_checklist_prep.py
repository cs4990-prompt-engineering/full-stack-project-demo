from openai import OpenAI
import os

# Set your OpenAI API key as a global variable (or read from environment variable)
api_key = "your key"

# Initialize the OpenAI client globally
client = OpenAI(api_key=api_key)

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

# Example usage:
job_description = """Full job description: this is a startup company that builds an AI-based solution for college career advisor"""  # Replace with the actual job description
checklist = generate_job_preparation_checklist(job_description)
print(checklist)

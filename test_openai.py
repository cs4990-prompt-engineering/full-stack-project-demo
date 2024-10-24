from openai import OpenAI

# Add your OpenAI API key here
api_key = "your key"

client = OpenAI(api_key=api_key)

job_description = """Full job description
Tapcart is the ultimate mobile commerce platform fueling the fastest growing brands. We power mobile apps for over 50 million consumers worldwide, processing over $6 billion in mobile commerce revenue.

Almost all ecommerce traffic comes from a mobile device; we turn these users into high retention growth for some of the largest brands, including BÉIS, Princess Polly, gorjana, LSKD, BYLT Basics, and many more. Tapcart is trusted by thousands of brands to power their mobile experience by building mobile apps in hours (not months).

As a Full Stack Engineer (React/ Node/ React Native) you will work closely with our small team to refactor, maintain and extend the functionality of our mobile ecommerce platform used by thousands of brands worldwide. The ideal candidate is passionate and experienced in developing pixel-perfect user interfaces with React, backed by clean and concise business logic. You will have the opportunity to influence our product by participating in design review and proposing technical solutions to novel problems.

Our engineering team is continuously looking for ways to better ourselves and our peers. We believe that taking the time to write great code is crucial to our long-term success and core to our values. We encourage this by pair programming, code reviews, demos, and pull requests.

Working at Tapcart means your code will reach millions of shoppers, and you have the exciting opportunity to make a big impact while learning from and teaching our team.
How You Will Make an Impact
Engaging in our development and release lifecycle process rituals (we use Scrum and Agile)
Contributing to our Consumer e-commerce app: our core white label app, which enables brands to have their own mobile application live within days. We're creating an experience that helps brands reach and retain their customers.
What Skills You'll Need
5+ years coding experience, primarily with web technologies (Javascript/Typescript)
3+ years of experience with mobile apps (native, cross-platform, or hybrid)
Understanding of React, React Native, HTML, Node.js, CSS, Modern Web Standards
Experience bringing a web app to production - familiarity with build processes, cloud hosting for single page applications, server-side rendering, caching, etc.
Experience developing and extending component libraries
Experience integrating with 3rd Party APIs and flexible interface design
Experience working cross functionally
A penchant for writing clean, reusable code
Eagerness to learn and teach"""

job_checklist_prompt = "I will be providing a full job description. Please generate a checklist for me to learn and prepare for this job interview. This is for a college CS major student to use. Please keep the checklist simple and concise. For each item, please provide a reference or URL for the student to use and learn. \n" \
"-------------" + job_description;

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": job_checklist_prompt
        }
    ]
)

print(completion.choices[0].message.content)
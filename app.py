from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# Homepage
@app.route("/")
def index():
    return render_template("index.html")

# Portfolio page: returns full page or partial update via HTMX
projects = [
    {
        "name": "AI Medical Assistant",
        "description": "Automating patient triage using AI.",
        "tech": ["Python", "TensorFlow", "FHIR API"],
        "category": "AI & Healthcare",
        "impact": "Reduced triage time by 40%",
        "details": "This project uses NLP to classify patient symptoms and automate patient triage, reducing the workload for doctors and nurses."
    },
    {
        "name": "EHR Optimization",
        "description": "Streamlining Electronic Health Records (EHR).",
        "tech": ["Python", "FastAPI", "HL7"],
        "category": "Automation",
        "impact": "Saved 300+ admin hours per month.",
        "details": "Developed an intelligent automation tool to extract, validate, and organize health records, reducing manual effort and errors."
    }
]
@app.route("/portfolio")
def portfolio():
    # If request comes from HTMX (partial load), render only the projects list.
    if request.headers.get("HX-Request"):
        return render_template("partials/portfolio_list.html", projects=projects)
    return render_template("portfolio.html", projects=projects)

@app.route("/portfolio/details/<int:index>")
def project_details(index):
    project = projects[index - 1] if index <= len(projects) else None
    if project:
        return render_template("partials/project_details.html", project=project)
    return "<p class='text-red-500'>Project not found.</p>", 404


# Blog page
@app.route("/blog")
def blog():
    posts = [
        {"title": "My First Post", "excerpt": "Welcome to my blog...", "url": "#"},
        {"title": "A Day in the Life", "excerpt": "Today I worked on...", "url": "#"},
        # add more posts as needed
    ]
    if request.headers.get("HX-Request"):
        return render_template("partials/blog_list.html", posts=posts)
    return render_template("blog.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    services = [
        {
            "title": "AI & Automation in Healthcare",
            "description": "Custom AI models for medical imaging (Object Detection, Image Segmentation). Automating repetitive tasks like report generation and data processing.",
            "icon": "💡",
        },
        {
            "title": "Healthcare Data & Analytics",
            "description": "Processing and visualizing medical data using Tableau, Pandas, and more. Optimizing databases for PACS, EHR, and healthcare APIs.",
            "icon": "📊",
        },
        {
            "title": "Web & API Development for Healthcare",
            "description": "Building secure web apps using Flask + HTMX. Integrating APIs like OpenFDA and Google Cloud Healthcare API.",
            "icon": "🖥️",
        },
    ]

    if request.headers.get("HX-Request"):
        return render_template("partials/service_list.html", services=services)

    return render_template("services.html", services=services)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Here, you can process the form (e.g., send an email)
        print(f"New Contact Request from {name} ({email}): {message}")

        return jsonify({"success": True, "message": "Your message has been sent!"})

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

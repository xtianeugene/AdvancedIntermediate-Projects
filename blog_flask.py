from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
posts = []

TEMPLATE = """
<h1>My Blog</h1>
{% for p in posts %}
<h2>{{ p.title }}</h2><p>{{ p.body }}</p>
{% endfor %}
<form method="post">
<input name="title" placeholder="Title"><br>
<textarea name="body" placeholder="Body"></textarea><br>
<button>Post</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        posts.append({"title": request.form["title"], "body": request.form["body"]})
        return redirect("/")
    return render_template_string(TEMPLATE, posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
# Personal Documentation Blog

![Repo Size](https://img.shields.io/github/repo-size/USERNAME/doc)
![Last Commit](https://img.shields.io/github/last-commit/USERNAME/doc)
![License](https://img.shields.io/github/license/USERNAME/doc)
![Markdown](https://img.shields.io/badge/content-markdown-blue)
![Python](https://img.shields.io/badge/tool-python-yellow)

A lightweight **static documentation/blog system** built using **Markdown, HTML, CSS, and Python**.

This repository acts as a **personal knowledge base and learning log**, where posts are written in Markdown and organized into structured categories.

The system keeps documentation simple while remaining fully **version controlled with Git**.

---

# Live Preview

If deployed using **GitHub Pages**, the documentation site can be accessed at:

```
https://USERNAME.github.io/doc
```

*(Replace USERNAME with your GitHub username.)*

---

# Screenshot

Example view of the documentation site:

![Documentation Screenshot](store/Area_screenshot.png)

---

# Features

* Markdown-based posts
* Organized content categories
* Lightweight static website
* Automatic post indexing
* Python post management script
* Clean HTML + CSS interface
* Easy GitHub Pages deployment
* Minimal dependencies

---

# Project Structure

```
.
├── favicon.jpeg
├── index.html
├── posts
│   ├── FastPaced
│   │   └── 1.md
│   └── Project_Learn
│       ├── Day1.md
│       ├── Day2.md
│       ├── Day3.md
│       ├── Day4.md
│       ├── Day5.md
│       ├── Day6.md
│       ├── Day7.md
│       ├── Day8.md
│       └── Day9.md
├── posts.json
├── python_post_manager.py
├── README.md
├── store
│   └── Area_screenshot.png
└── style.css
```

---

# How It Works

The project follows a simple workflow:

1. Write documentation in **Markdown**
2. Organize posts into categories
3. Register posts in `posts.json`
4. Render posts dynamically on the website

The **Python post manager** helps automate this workflow.

---

# Automatic Post Indexing

The script:

```
python_post_manager.py
```

is responsible for managing the blog post registry.

It updates the file:

```
posts.json
```

which acts as a **post index** for the website.

This allows `index.html` to dynamically display posts without manually editing HTML.

Typical workflow:

```
1. Create Markdown post
2. Run Python manager
3. Update posts.json
4. Commit changes
```

---

# Writing a New Post

Create a Markdown file inside the appropriate category.

Example:

```
posts/Project_Learn/Day10.md
```

After writing the post, update the post registry:

```
python python_post_manager.py
```

Then commit your changes:

```
git add .
git commit -m "Added Day10 learning log"
git push
```

---

# Local Development

To preview the site locally:

```
python -m http.server
```

Then open:

```
http://localhost:8000
```

---

# Deploying with GitHub Pages

1. Push repository to GitHub

2. Open repository **Settings**

3. Navigate to:

```
Pages → Source
```

4. Select:

```
Branch: main
Folder: /root
```

GitHub will publish the site automatically.

Your site will appear at:

```
https://USERNAME.github.io/doc
```

---

# Contribution Guidelines

Contributions are welcome.

If you want to improve the documentation system:

### Steps

1. Fork the repository
2. Create a new branch

```
git checkout -b feature-improvement
```

3. Make your changes
4. Commit your changes

```
git commit -m "Improved documentation system"
```

5. Push the branch

```
git push origin feature-improvement
```

6. Open a Pull Request

---

# Future Improvements

Planned enhancements:

* Markdown → HTML rendering pipeline
* Search functionality
* Post metadata (date, tags, summary)
* RSS feed
* Tagging system
* Dark mode
* Better UI layout
* Automatic deployment workflow

---

# Purpose of This Repository

This project is part of a **continuous learning and documentation workflow**.

The goal is to:

* track development progress
* maintain structured learning notes
* build a searchable knowledge base
* keep technical documentation organized

---

# License

This project is available for personal and educational use.

---

# Author

Maintained as part of an ongoing documentation and learning practice.

![Snake animation](https://github.com/middi870/middi870/blob/output/github-contribution-grid-snake.svg)
import os
import json
from datetime import date

POSTS_DIR = "posts"
POSTS_JSON = "posts.json"
AUTHOR = "You"

# 🔹 Manual keywords you control
KEYWORDS = [
    "python",
    "rust",
    "fastpaced",
    "project_learn",
    "day",
]

def generate_slug(filepath):
    # slug = os.path.relpath(filepath, POSTS_DIR)
    slug = filepath.replace(POSTS_DIR + os.sep, "")
    slug = os.path.splitext(slug)[0]
    return slug.replace(os.sep, "/")


def collect_markdown_files():
    md_files = []
    for root, _, files in os.walk(POSTS_DIR):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                md_files.append(full_path)
    return md_files


# def load_existing_posts():
#     if not os.path.exists(POSTS_JSON):
#         return {"posts": []}
#     with open(POSTS_JSON, "r") as f:
#         return json.load(f)

def load_existing_posts():
    if not os.path.exists(POSTS_JSON):
        return {"posts": []}

    if os.path.getsize(POSTS_JSON) == 0:
        return {"posts": []}

    try:
        with open(POSTS_JSON, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: posts.json is corrupted. Resetting.")
        return {"posts": []}

def infer_tags_from_path(slug):
    slug_lower = slug.lower()
    matched_tags = []

    for keyword in KEYWORDS:
        if keyword in slug_lower:
            matched_tags.append(keyword)

    return matched_tags


def main():
    data = load_existing_posts()
    existing_posts = {post["slug"]: post for post in data["posts"]}

    md_files = collect_markdown_files()

    for filepath in md_files:
        slug = generate_slug(filepath)

        inferred_tags = infer_tags_from_path(slug)

        if slug in existing_posts:
            # 🔹 Update tags if new ones detected
            existing = existing_posts[slug]
            existing_tags = set(existing.get("tags", []))
            combined_tags = sorted(existing_tags.union(inferred_tags))
            existing["tags"] = combined_tags
            continue

        new_post = {
            "slug": slug,
            "title": slug.split("/")[-1].replace("-", " ").title(),
            "date": str(date.today()),
            "author": AUTHOR,
            "description": f"Auto-generated post for {slug}",
            "tags": inferred_tags
        }

        data["posts"].append(new_post)
        print(f"Added: {slug}")

    data["posts"] = sorted(data["posts"], key=lambda x: x["date"], reverse=True)

    with open(POSTS_JSON, "w") as f:
        json.dump(data, f, indent=2)

    print("posts.json updated.")


if __name__ == "__main__":
    main()

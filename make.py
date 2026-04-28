# pylint: disable=missing-function-docstring, invalid-name

import os
import json
from pathlib import Path
from datetime import datetime
import shutil
import random

# NEW (for nbconvert without subprocess)
import nbformat
from nbconvert import MarkdownExporter

from git import Repo

# Get the current repository name dynamically
repo = Repo(os.getcwd())
FOLDER_NAME = os.path.basename(repo.working_dir)

# Directories
NOTEBOOK_DIR        = "./notebooks"
OUTPUT_DIR          = "./content"
DOCS_FOLDER         = "./docs"
GLOBAL_IMAGES_DIR   = os.path.join(OUTPUT_DIR, "images")


def is_recently_modified(source_file, target_file):
    if not target_file.exists():
        return True
    return source_file.stat().st_mtime > target_file.stat().st_mtime


# ✅ NEW: Direct conversion (NO subprocess)
def convert_notebook_direct(notebook_path, output_path):
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    exporter = MarkdownExporter()
    body, _ = exporter.from_notebook_node(nb)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(body)


def convert_notebooks_to_markdown(notebook_dir, output_dir, fresh=False):
    notebook_dir = Path(notebook_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    slugs = set()

    for notebook in notebook_dir.rglob("*.ipynb"):
        if any(part.startswith('.') for part in notebook.parts):
            continue

        print(f"Converting {notebook} to markdown...")
        relative_path = notebook.relative_to(notebook_dir)
        output_subdir = output_dir / relative_path.parent
        output_subdir.mkdir(parents=True, exist_ok=True)

        md_file = output_subdir / f"{notebook.stem}.md"

        # ✅ Convert using Python API
        convert_notebook_direct(notebook, md_file)

        if not fresh:
            if not is_recently_modified(notebook, md_file):
                continue

        new_md_file = ensure_unique_slug(md_file, slugs)

        cell_count = count_cells_in_notebook(notebook)
        score = calculate_score(cell_count)

        add_metadata_to_markdown(new_md_file, cell_count, score)
        update_image_references(new_md_file)


def ensure_unique_slug(md_file, slugs):
    slug = md_file.stem
    new_md_file = md_file

    while slug in slugs:
        slug = f"{md_file.stem}-{random.randint(1000, 9999)}"
        new_md_file = md_file.with_name(f"{slug}.md")

    if new_md_file != md_file:
        os.rename(md_file, new_md_file)
        print(f"Renamed {md_file.name} to {new_md_file.name}")

    slugs.add(slug)
    return new_md_file


def calculate_score(cell_count):
    if cell_count < 5:
        return 0
    return (cell_count // 5) * 5


def count_cells_in_notebook(notebook_path):
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook_data = json.load(f)
    return len(notebook_data.get("cells", []))


def add_metadata_to_markdown(markdown_file, cell_count, score):
    with open(markdown_file, "r", encoding="utf-8") as f:
        content = f.read()

    file_mtime = datetime.fromtimestamp(Path(markdown_file).stat().st_mtime)
    formatted_date = file_mtime.strftime("%Y-%m-%d")

    metadata = f"""---
title: {markdown_file.stem.replace('_', ' ').title()}
date: {formatted_date}
author: Your Name
cell_count: {cell_count}
score: {score}
---
"""

    score_info = f"\n\n---\n**Score: {score}**\n"

    print(f"Adding metadata to {markdown_file}...")
    with open(markdown_file, "w", encoding="utf-8") as f:
        f.write(metadata + "\n" + content + score_info)


def copy_images_to_global_folder(content_dir, global_images_dir):
    image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".bmp", ".webp"}
    global_images_dir = Path(global_images_dir)
    global_images_dir.mkdir(parents=True, exist_ok=True)

    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.lower().endswith(tuple(image_extensions)):
                source = Path(root) / file
                target = global_images_dir / file
                if not target.exists():
                    shutil.copy2(source, target)
                    print(f"Copied: {source} -> {target}")


def resolve_duplicate_slugs(content_dir):
    slugs = {}
    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                filepath = Path(root) / file
                slug = filepath.stem

                if slug in slugs:
                    new_slug = f"{slug}-{random.randint(1000, 9999)}"
                    new_filepath = filepath.parent / f"{new_slug}.md"
                    os.rename(filepath, new_filepath)
                    print(f"Renamed {file} → {new_slug}.md")
                else:
                    slugs[slug] = filepath


def update_image_references(markdown_file):
    with open(markdown_file, "r", encoding="utf-8") as f:
        content = f.read()

    updated_content = []
    for line in content.splitlines():
        if "![png](" in line:
            start_idx = line.find("![png](") + len("![png](")
            end_idx = line.find(")", start_idx)
            current_path = line[start_idx:end_idx]
            file_name = current_path.split("/")[-1]
            new_path = f"/{FOLDER_NAME}/images/{file_name}"
            line = line.replace(current_path, new_path)

        updated_content.append(line)

    with open(markdown_file, "w", encoding="utf-8") as f:
        f.write("\n".join(updated_content))


# ✅ FIXED Pelican call
def generate_site_with_pelican(content_dir):
    print("Generating site with Pelican...")
    os.system(f"python -m pelican {content_dir}")


def clean_output_dir(output_dir):
    output_path = Path(output_dir)
    if output_path.exists():
        shutil.rmtree(output_path)
        print(f"Deleted: {output_dir}")
    output_path.mkdir(parents=True, exist_ok=True)
    print(f"Recreated: {output_dir}")


if __name__ == "__main__":
    Path(NOTEBOOK_DIR).mkdir(parents=True, exist_ok=True)
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    fresh = True
    print(f'fresh: {fresh}')

    if fresh:
        clean_output_dir(OUTPUT_DIR)
        clean_output_dir(DOCS_FOLDER)

    convert_notebooks_to_markdown(NOTEBOOK_DIR, OUTPUT_DIR, fresh=fresh)

    resolve_duplicate_slugs(OUTPUT_DIR)
    copy_images_to_global_folder(OUTPUT_DIR, GLOBAL_IMAGES_DIR)

    try:
        generate_site_with_pelican(OUTPUT_DIR)
        print("✅ Site generated successfully!")
    except Exception as e:
        print(f"❌ Error generating site: {e}")
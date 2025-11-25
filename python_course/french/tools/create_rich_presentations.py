#!/usr/bin/env python3
"""
Create comprehensive PowerPoint presentations from Jupyter notebooks
Extracts detailed content and creates information-rich slides
"""

import json
import sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import re

# Import comprehensive chapter content
from chapter_content import CHAPTERS

def remove_emojis(text):
    """Remove emojis from text"""
    # Remove emojis (Unicode ranges for emojis)
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub('', text).strip()

def parse_notebook(notebook_path):
    """Parse Jupyter notebook and extract structured content"""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    slides_data = []
    current_slide = None

    for cell in notebook['cells']:
        cell_type = cell['cell_type']
        source = ''.join(cell.get('source', []))

        if not source.strip():
            continue

        if cell_type == 'markdown':
            # Check for main headers (chapters)
            if source.startswith('# Chapter') and 'Practice Notebook' in source:
                # Title slide
                lines = source.split('\n')
                title = remove_emojis(lines[0].replace('# ', ''))
                current_slide = {
                    'type': 'title',
                    'title': title,
                    'content': []
                }
                slides_data.append(current_slide)

            # Section headers (## Part X)
            elif source.startswith('## Part'):
                if current_slide:
                    slides_data.append(current_slide)
                lines = source.split('\n')
                title = remove_emojis(lines[0].replace('## ', '').replace('Part ', 'Part '))
                current_slide = {
                    'type': 'section',
                    'title': title,
                    'content': []
                }
                # Add description
                if len(lines) > 1:
                    desc = '\n'.join(lines[1:]).strip()
                    desc = remove_emojis(desc)
                    if desc:
                        current_slide['content'].append(desc)

            # Subsection (###)
            elif source.startswith('###'):
                # Don't create new slide for exercises, add to current
                title = remove_emojis(source.replace('###', '').strip())
                if current_slide and not title.startswith('Exercise') and not title.startswith('✏️'):
                    if current_slide:
                        slides_data.append(current_slide)
                    current_slide = {
                        'type': 'content',
                        'title': title,
                        'content': []
                    }

            # Example markers
            elif source.startswith('### Example'):
                if current_slide:
                    slides_data.append(current_slide)
                title = remove_emojis(source.replace('###', '').strip())
                current_slide = {
                    'type': 'example',
                    'title': title,
                    'content': []
                }

            # Regular markdown content
            elif current_slide:
                content = remove_emojis(source).strip()
                if content and not content.startswith('---') and not content.startswith('###'):
                    # Split by paragraphs
                    for line in content.split('\n'):
                        line = line.strip()
                        if line and len(line) > 5:
                            current_slide['content'].append(line)

        elif cell_type == 'code' and current_slide:
            # Add code examples
            code = source.strip()
            if code and not code.startswith('#') and len(code) < 200:
                # Only add short, meaningful code examples
                if 'print(' in code or '=' in code:
                    current_slide['content'].append(f"CODE: {code}")

    if current_slide:
        slides_data.append(current_slide)

    return slides_data

def create_comprehensive_slides(chapter_name, chapter_num):
    """Create comprehensive slides with rich content based on chapter"""
    # Return content from the imported CHAPTERS dictionary
    return CHAPTERS.get(chapter_num, {'slides': []})

def add_title_slide(prs, title, subtitle=""):
    """Add a title slide"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    # Background
    left = top = Inches(0)
    width = prs.slide_width
    height = prs.slide_height

    bg_shape = slide.shapes.add_shape(1, left, top, width, height)
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = RGBColor(240, 248, 255)
    bg_shape.line.fill.background()

    # Title
    title_box = slide.shapes.add_textbox(
        Inches(1), Inches(2.5), Inches(11.33), Inches(1.2)
    )
    title_frame = title_box.text_frame
    title_frame.text = title
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(48)
    title_para.font.bold = True
    title_para.font.color.rgb = RGBColor(0, 51, 102)
    title_para.alignment = PP_ALIGN.CENTER

    # Subtitle
    if subtitle:
        subtitle_box = slide.shapes.add_textbox(
            Inches(1), Inches(4), Inches(11.33), Inches(0.8)
        )
        subtitle_frame = subtitle_box.text_frame
        subtitle_frame.text = subtitle
        subtitle_para = subtitle_frame.paragraphs[0]
        subtitle_para.font.size = Pt(28)
        subtitle_para.font.color.rgb = RGBColor(70, 130, 180)
        subtitle_para.alignment = PP_ALIGN.CENTER

def add_content_slide(prs, title, content_items):
    """Add a content slide with title and bullet points"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    # White background
    left = top = Inches(0)
    width = prs.slide_width
    height = prs.slide_height

    bg_shape = slide.shapes.add_shape(1, left, top, width, height)
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = RGBColor(255, 255, 255)
    bg_shape.line.fill.background()

    # Blue header bar
    header_shape = slide.shapes.add_shape(
        1, Inches(0), Inches(0), prs.slide_width, Inches(0.15)
    )
    header_shape.fill.solid()
    header_shape.fill.fore_color.rgb = RGBColor(0, 102, 204)
    header_shape.line.fill.background()

    # Title
    title_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(0.35), Inches(12), Inches(0.7)
    )
    title_frame = title_box.text_frame
    title_frame.text = title
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(36)
    title_para.font.bold = True
    title_para.font.color.rgb = RGBColor(0, 51, 102)

    # Content
    if content_items:
        content_box = slide.shapes.add_textbox(
            Inches(0.7), Inches(1.3), Inches(11.8), Inches(5.8)
        )
        content_frame = content_box.text_frame
        content_frame.word_wrap = True

        for i, content in enumerate(content_items):
            if not content.strip():
                continue

            if i == 0:
                p = content_frame.paragraphs[0]
            else:
                p = content_frame.add_paragraph()

            # Handle code
            if content.startswith('CODE:'):
                code = content.replace('CODE:', '').strip()
                p.text = code
                p.font.name = 'Consolas'
                p.font.size = Pt(14)
                p.font.color.rgb = RGBColor(0, 100, 0)
                p.space_after = Pt(4)
                continue

            p.text = content

            # Determine formatting
            if content.startswith('•'):
                p.level = 1
                p.font.size = Pt(16)
                p.space_after = Pt(4)
            elif content.startswith('  •'):
                p.level = 2
                p.font.size = Pt(14)
                p.space_after = Pt(3)
            elif ':' in content and not content.startswith(' '):
                # Likely a heading
                p.level = 0
                p.font.bold = True
                p.font.size = Pt(20)
                p.space_after = Pt(6)
            else:
                p.level = 0
                p.font.size = Pt(16)
                p.space_after = Pt(6)

            p.font.color.rgb = RGBColor(51, 51, 51)

def create_rich_presentation(chapter_num, chapter_name, output_file):
    """Create a comprehensive presentation for a chapter"""
    print(f"Creating rich presentation for Chapter {chapter_num}: {chapter_name}")

    # Get comprehensive content
    chapter_data = create_comprehensive_slides(chapter_name, chapter_num)

    if not chapter_data.get('slides'):
        print(f"  No content defined for chapter {chapter_num} yet")
        return

    # Create presentation with 16:9 format
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Add title slide
    add_title_slide(prs, chapter_data['title'], chapter_data.get('subtitle', ''))

    # Add content slides
    for slide_data in chapter_data['slides']:
        add_content_slide(prs, slide_data['title'], slide_data['content'])

    # Save
    prs.save(output_file)
    print(f"  Saved to {output_file} ({len(chapter_data['slides']) + 1} slides)")

def main():
    """Create all rich presentations"""
    base_dir = Path('/home/user/courses/python_course')

    chapters = [
        (1, 'introduction', 'introduction_to_python'),
        (2, 'working_with_data', 'working_with_data'),
        (3, 'making_decisions', 'making_decisions'),
        (4, 'loops', 'loops'),
        (5, 'lists', 'lists'),
        (6, 'dictionaries', 'dictionaries'),
        (7, 'functions', 'functions'),
        (8, 'tuples_and_sets', 'tuples_and_sets'),
        (9, 'file_io', 'file_io'),
        (10, 'error_handling', 'error_handling'),
    ]

    print("Creating Rich, Comprehensive PowerPoint Presentations")
    print("=" * 70)
    print("Features:")
    print("  - Detailed content with explanations")
    print("  - Code examples")
    print("  - Best practices")
    print("  - Common mistakes")
    print("  - Real-world applications")
    print("  - No emojis (professional format)")
    print("=" * 70)
    print()

    for chapter_num, chapter_dir, pptx_filename in chapters:
        # Handle chapter 10 (2 digits) vs chapters 1-9 (1 digit)
        if chapter_num < 10:
            chapter_path = base_dir / f'chapter_0{chapter_num}_{chapter_dir}'
        else:
            chapter_path = base_dir / f'chapter_{chapter_num}_{chapter_dir}'

        output_file = chapter_path / f'{pptx_filename}.pptx'

        create_rich_presentation(chapter_num, chapter_dir, str(output_file))
        print()

    print("=" * 70)
    print("Rich presentations created successfully!")

if __name__ == '__main__':
    main()

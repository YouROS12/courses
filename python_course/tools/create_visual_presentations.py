#!/usr/bin/env python3
"""
Create visually impressive PowerPoint presentations with rich content
Uses colored blocks, multi-column layouts, and visual elements
"""

import sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# Import comprehensive chapter content
from chapter_content import CHAPTERS

def add_title_slide(prs, title, subtitle=""):
    """Add a visually impressive title slide with gradient-style background"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    # Add gradient-style background with two colors
    left = top = Inches(0)
    width = prs.slide_width
    height = prs.slide_height

    # Bottom layer - darker blue
    bg_shape = slide.shapes.add_shape(1, left, top, width, height)
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = RGBColor(20, 70, 140)
    bg_shape.line.fill.background()

    # Top accent bar - bright blue
    accent_shape = slide.shapes.add_shape(
        1, Inches(0), Inches(0), width, Inches(2)
    )
    accent_shape.fill.solid()
    accent_shape.fill.fore_color.rgb = RGBColor(0, 120, 215)
    accent_shape.line.fill.background()

    # Decorative side bar
    side_bar = slide.shapes.add_shape(
        1, Inches(0), Inches(2), Inches(0.3), Inches(5.5)
    )
    side_bar.fill.solid()
    side_bar.fill.fore_color.rgb = RGBColor(255, 187, 51)
    side_bar.line.fill.background()

    # Title with shadow effect (create shadow by adding duplicate slightly offset)
    title_box = slide.shapes.add_textbox(
        Inches(1.5), Inches(2.8), Inches(11), Inches(1.5)
    )
    title_frame = title_box.text_frame
    title_frame.text = title
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(52)
    title_para.font.bold = True
    title_para.font.color.rgb = RGBColor(255, 255, 255)
    title_para.alignment = PP_ALIGN.CENTER

    # Subtitle in a colored box
    if subtitle:
        # Background box for subtitle
        subtitle_bg = slide.shapes.add_shape(
            1, Inches(3), Inches(4.5), Inches(7.33), Inches(1.2)
        )
        subtitle_bg.fill.solid()
        subtitle_bg.fill.fore_color.rgb = RGBColor(0, 102, 204)
        subtitle_bg.line.fill.background()

        subtitle_box = slide.shapes.add_textbox(
            Inches(3.2), Inches(4.7), Inches(6.93), Inches(0.8)
        )
        subtitle_frame = subtitle_box.text_frame
        subtitle_frame.text = subtitle
        subtitle_para = subtitle_frame.paragraphs[0]
        subtitle_para.font.size = Pt(28)
        subtitle_para.font.color.rgb = RGBColor(255, 255, 255)
        subtitle_para.alignment = PP_ALIGN.CENTER

def add_section_slide(prs, title, description=""):
    """Add a colorful section divider slide"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    # Colorful background
    left = top = Inches(0)
    width = prs.slide_width
    height = prs.slide_height

    bg_shape = slide.shapes.add_shape(1, left, top, width, height)
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = RGBColor(0, 102, 204)
    bg_shape.line.fill.background()

    # Decorative accent bars
    accent1 = slide.shapes.add_shape(
        1, Inches(0), Inches(3), Inches(4), Inches(0.15)
    )
    accent1.fill.solid()
    accent1.fill.fore_color.rgb = RGBColor(255, 187, 51)
    accent1.line.fill.background()

    accent2 = slide.shapes.add_shape(
        1, Inches(9.33), Inches(4.5), Inches(4), Inches(0.15)
    )
    accent2.fill.solid()
    accent2.fill.fore_color.rgb = RGBColor(255, 187, 51)
    accent2.line.fill.background()

    # Title
    title_box = slide.shapes.add_textbox(
        Inches(1), Inches(2.8), Inches(11.33), Inches(1.5)
    )
    title_frame = title_box.text_frame
    title_frame.text = title
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(48)
    title_para.font.bold = True
    title_para.font.color.rgb = RGBColor(255, 255, 255)
    title_para.alignment = PP_ALIGN.CENTER

    if description:
        desc_box = slide.shapes.add_textbox(
            Inches(2), Inches(4.8), Inches(9.33), Inches(1)
        )
        desc_frame = desc_box.text_frame
        desc_frame.text = description
        desc_para = desc_frame.paragraphs[0]
        desc_para.font.size = Pt(24)
        desc_para.font.color.rgb = RGBColor(255, 255, 255)
        desc_para.alignment = PP_ALIGN.CENTER

def add_content_slide(prs, title, content_items):
    """Add a visually rich content slide with colored blocks"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    # White background
    left = top = Inches(0)
    width = prs.slide_width
    height = prs.slide_height

    bg_shape = slide.shapes.add_shape(1, left, top, width, height)
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = RGBColor(250, 250, 250)
    bg_shape.line.fill.background()

    # Colorful header section
    header_bg = slide.shapes.add_shape(
        1, Inches(0), Inches(0), width, Inches(1.2)
    )
    header_bg.fill.solid()
    header_bg.fill.fore_color.rgb = RGBColor(0, 102, 204)
    header_bg.line.fill.background()

    # Decorative accent bar
    accent_bar = slide.shapes.add_shape(
        1, Inches(0), Inches(1.2), Inches(0.15), Inches(6.3)
    )
    accent_bar.fill.solid()
    accent_bar.fill.fore_color.rgb = RGBColor(255, 187, 51)
    accent_bar.line.fill.background()

    # Title
    title_box = slide.shapes.add_textbox(
        Inches(0.4), Inches(0.3), Inches(12), Inches(0.7)
    )
    title_frame = title_box.text_frame
    title_frame.text = title
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(36)
    title_para.font.bold = True
    title_para.font.color.rgb = RGBColor(255, 255, 255)

    # Content area with smart layout
    if content_items:
        current_y = 1.5
        in_code_block = False
        code_lines = []

        for content in content_items:
            if not content.strip():
                continue

            # Detect code blocks
            is_code = (
                '=' in content and not content.startswith('•') and
                not ':' in content[:20] or
                content.startswith('    ') or
                any(keyword in content for keyword in ['def ', 'if ', 'for ', 'while ', 'import ', 'class '])
            )

            # Check if it's a section header
            is_header = (
                ':' in content and not content.startswith('•') and
                not '=' in content and len(content) < 60
            )

            if is_code:
                code_lines.append(content)
                in_code_block = True
                continue
            elif in_code_block and code_lines:
                # Render accumulated code block
                current_y = add_code_block(slide, code_lines, current_y)
                code_lines = []
                in_code_block = False

            if is_header:
                # Add colored box for headers
                header_height = 0.4
                header_bg = slide.shapes.add_shape(
                    1, Inches(0.4), Inches(current_y - 0.05),
                    Inches(12.5), Inches(header_height)
                )
                header_bg.fill.solid()
                header_bg.fill.fore_color.rgb = RGBColor(0, 120, 215)
                header_bg.line.fill.background()

                text_box = slide.shapes.add_textbox(
                    Inches(0.6), Inches(current_y),
                    Inches(12), Inches(header_height - 0.1)
                )
                text_frame = text_box.text_frame
                p = text_frame.paragraphs[0]
                p.text = content
                p.font.size = Pt(20)
                p.font.bold = True
                p.font.color.rgb = RGBColor(255, 255, 255)

                current_y += header_height + 0.1
            else:
                # Regular content
                text_box = slide.shapes.add_textbox(
                    Inches(0.5), Inches(current_y),
                    Inches(12.3), Inches(0.35)
                )
                text_frame = text_box.text_frame
                p = text_frame.paragraphs[0]
                p.text = content

                if content.startswith('•'):
                    p.level = 1
                    p.font.size = Pt(16)
                    # Add colored bullet
                    p.font.color.rgb = RGBColor(51, 51, 51)
                else:
                    p.font.size = Pt(17)
                    p.font.color.rgb = RGBColor(51, 51, 51)

                current_y += 0.30

            # Break if running out of space
            if current_y > 6.8:
                break

        # Render any remaining code block
        if code_lines:
            add_code_block(slide, code_lines, current_y)

def add_code_block(slide, code_lines, y_position):
    """Add a visually styled code block"""
    if y_position > 6.5:
        return y_position

    code_text = '\n'.join(code_lines)
    line_count = len(code_lines)
    block_height = min(line_count * 0.25 + 0.2, 2.5)

    # Code background box
    code_bg = slide.shapes.add_shape(
        1, Inches(0.7), Inches(y_position - 0.05),
        Inches(11.8), Inches(block_height)
    )
    code_bg.fill.solid()
    code_bg.fill.fore_color.rgb = RGBColor(40, 44, 52)
    code_bg.line.fill.background()

    # Decorative line on left
    code_accent = slide.shapes.add_shape(
        1, Inches(0.7), Inches(y_position - 0.05),
        Inches(0.08), Inches(block_height)
    )
    code_accent.fill.solid()
    code_accent.fill.fore_color.rgb = RGBColor(97, 175, 239)
    code_accent.line.fill.background()

    # Code text
    code_box = slide.shapes.add_textbox(
        Inches(1), Inches(y_position),
        Inches(11.2), Inches(block_height - 0.1)
    )
    code_frame = code_box.text_frame
    code_frame.text = code_text
    code_frame.word_wrap = False

    for para in code_frame.paragraphs:
        para.font.name = 'Consolas'
        para.font.size = Pt(14)
        para.font.color.rgb = RGBColor(171, 178, 191)
        para.space_after = Pt(2)

    return y_position + block_height + 0.15

def add_two_column_slide(prs, title, left_content, right_content):
    """Add a slide with two columns for better visual layout"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)

    # Background
    left = top = Inches(0)
    width = prs.slide_width
    height = prs.slide_height

    bg_shape = slide.shapes.add_shape(1, left, top, width, height)
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = RGBColor(250, 250, 250)
    bg_shape.line.fill.background()

    # Header
    header_bg = slide.shapes.add_shape(
        1, Inches(0), Inches(0), width, Inches(1.2)
    )
    header_bg.fill.solid()
    header_bg.fill.fore_color.rgb = RGBColor(0, 102, 204)
    header_bg.line.fill.background()

    # Title
    title_box = slide.shapes.add_textbox(
        Inches(0.4), Inches(0.3), Inches(12), Inches(0.7)
    )
    title_frame = title_box.text_frame
    title_frame.text = title
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(36)
    title_para.font.bold = True
    title_para.font.color.rgb = RGBColor(255, 255, 255)

    # Left column background
    left_bg = slide.shapes.add_shape(
        1, Inches(0.3), Inches(1.5), Inches(6), Inches(5.7)
    )
    left_bg.fill.solid()
    left_bg.fill.fore_color.rgb = RGBColor(240, 248, 255)
    left_bg.line.fill.background()

    # Right column background
    right_bg = slide.shapes.add_shape(
        1, Inches(6.8), Inches(1.5), Inches(6), Inches(5.7)
    )
    right_bg.fill.solid()
    right_bg.fill.fore_color.rgb = RGBColor(255, 250, 240)
    right_bg.line.fill.background()

    # Left content
    left_box = slide.shapes.add_textbox(
        Inches(0.5), Inches(1.7), Inches(5.6), Inches(5.3)
    )
    left_frame = left_box.text_frame
    left_frame.word_wrap = True

    for i, content in enumerate(left_content):
        if i == 0:
            p = left_frame.paragraphs[0]
        else:
            p = left_frame.add_paragraph()
        p.text = content
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(51, 51, 51)
        p.space_after = Pt(6)

    # Right content
    right_box = slide.shapes.add_textbox(
        Inches(7), Inches(1.7), Inches(5.6), Inches(5.3)
    )
    right_frame = right_box.text_frame
    right_frame.word_wrap = True

    for i, content in enumerate(right_content):
        if i == 0:
            p = right_frame.paragraphs[0]
        else:
            p = right_frame.add_paragraph()
        p.text = content
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(51, 51, 51)
        p.space_after = Pt(6)

def create_rich_presentation(chapter_num, chapter_name, output_file):
    """Create a visually impressive presentation for a chapter"""
    print(f"Creating visual presentation for Chapter {chapter_num}: {chapter_name}")

    # Get comprehensive content
    chapter_data = CHAPTERS.get(chapter_num, {'slides': []})

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
    slide_count = len(chapter_data['slides'])
    for idx, slide_data in enumerate(chapter_data['slides']):
        # Every few slides, add a section divider if it's a major topic
        if idx > 0 and idx % 4 == 0 and idx < slide_count - 1:
            add_section_slide(prs, slide_data['title'].split(':')[0] if ':' in slide_data['title'] else slide_data['title'])

        add_content_slide(prs, slide_data['title'], slide_data['content'])

    # Add final practice slide
    add_section_slide(prs, "Time to Practice!", f"Chapter {chapter_num} Exercises")

    # Save
    prs.save(output_file)
    print(f"  Saved to {output_file} ({len(chapter_data['slides']) + 2} slides)")

def main():
    """Create all visually impressive presentations"""
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

    print("Creating Visually Impressive PowerPoint Presentations")
    print("=" * 70)
    print("Visual Features:")
    print("  - Colored header sections and accent bars")
    print("  - Dark-themed code blocks with syntax coloring")
    print("  - Section divider slides with full backgrounds")
    print("  - Visual hierarchy with colored boxes")
    print("  - Professional gradient-style title slides")
    print("  - Information-rich content with visual appeal")
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
    print("Visually impressive presentations created successfully!")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Create visually impressive PowerPoint presentations with rich content
Uses colored blocks, multi-column layouts, and visual elements
Automatically splits long content across multiple slides
"""

import sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# Import comprehensive chapter content
from chapter_content import CHAPTERS

def add_slide_background(slide, prs):
    """Add background elements to a content slide"""
    left = top = Inches(0)
    width = prs.slide_width
    height = prs.slide_height

    # White background
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

def add_slide_title(slide, title):
    """Add title to a content slide"""
    title_box = slide.shapes.add_textbox(
        Inches(0.4), Inches(0.3), Inches(12), Inches(0.7)
    )
    title_frame = title_box.text_frame
    title_frame.text = title
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(36)
    title_para.font.bold = True
    title_para.font.color.rgb = RGBColor(255, 255, 255)

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

    # Title
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

def add_code_block(slide, code_lines, y_position):
    """Add a visually styled code block"""
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

def estimate_content_height(content, is_code=False, is_header=False):
    """Estimate how much vertical space content will take"""
    if is_code:
        return 0.25 * len(content.split('\n')) + 0.2
    elif is_header:
        return 0.5
    else:
        return 0.30

def add_content_to_slides(prs, title, content_items):
    """Add content, splitting across multiple slides as needed"""
    slides_created = []
    slide_num = 0

    i = 0
    while i < len(content_items):
        slide_num += 1

        # Create new slide
        slide_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(slide_layout)
        slides_created.append(slide)

        # Add background and title
        add_slide_background(slide, prs)
        slide_title = title if slide_num == 1 else f"{title} (continued)"
        add_slide_title(slide, slide_title)

        # Add content with overflow detection
        current_y = 1.5
        in_code_block = False
        code_lines = []

        while i < len(content_items):
            content = content_items[i]

            if not content.strip():
                i += 1
                continue

            # Detect content type
            is_code = (
                '=' in content and not content.startswith('•') and
                not ':' in content[:20] or
                content.startswith('    ') or
                any(keyword in content for keyword in ['def ', 'if ', 'for ', 'while ', 'import ', 'class '])
            )

            is_header = (
                ':' in content and not content.startswith('•') and
                not '=' in content and len(content) < 60
            )

            # Estimate space needed
            if is_code:
                code_lines.append(content)
                in_code_block = True
                i += 1
                continue
            elif in_code_block and code_lines:
                # Check if code block fits
                code_height = estimate_content_height('\n'.join(code_lines), is_code=True)
                if current_y + code_height > 6.8:
                    # Doesn't fit, break to new slide
                    break
                # Render code block
                current_y = add_code_block(slide, code_lines, current_y)
                code_lines = []
                in_code_block = False

            # Check if current content fits
            content_height = estimate_content_height(content, is_header=is_header)
            if current_y + content_height > 6.8:
                # Doesn't fit, break to new slide
                break

            # Add content to slide
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
                    p.font.color.rgb = RGBColor(51, 51, 51)
                else:
                    p.font.size = Pt(17)
                    p.font.color.rgb = RGBColor(51, 51, 51)

                current_y += 0.30

            i += 1

        # Render any remaining code block on this slide
        if code_lines and current_y < 6.8:
            current_y = add_code_block(slide, code_lines, current_y)
            code_lines = []
            in_code_block = False

    return len(slides_created)

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

    # Add content slides (with auto-splitting for overflow)
    total_slides = 1  # Start with title slide
    slide_count = len(chapter_data['slides'])

    for idx, slide_data in enumerate(chapter_data['slides']):
        # Every few slides, add a section divider if it's a major topic
        if idx > 0 and idx % 5 == 0 and idx < slide_count - 1:
            add_section_slide(prs, slide_data['title'].split(':')[0] if ':' in slide_data['title'] else slide_data['title'])
            total_slides += 1

        # Add content slides (may create multiple if content is long)
        slides_added = add_content_to_slides(prs, slide_data['title'], slide_data['content'])
        total_slides += slides_added

    # Add final practice slide
    add_section_slide(prs, "Time to Practice!", f"Chapter {chapter_num} Exercises")
    total_slides += 1

    # Save
    prs.save(output_file)
    print(f"  Saved to {output_file} ({total_slides} slides)")

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
    print("  - Auto-splits long content across multiple slides")
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

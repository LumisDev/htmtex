import re

def tex_to_html(tex_content):
    # Define regular expressions to match different TeX elements
    section_pattern = re.compile(r'\\section{(.+?)}')
    subsection_pattern = re.compile(r'\\subsection{(.+?)}')
    bold_pattern = re.compile(r'\\textbf{(.+?)}')
    italic_pattern = re.compile(r'\\textit{(.+?)}')

    # Convert TeX sections to HTML headers
    html_content = section_pattern.sub(r'<h1>\1</h1>', tex_content)
    html_content = subsection_pattern.sub(r'<h2>\1</h2>', html_content)

    # Convert bold and italic text
    html_content = bold_pattern.sub(r'<strong>\1</strong>', html_content)
    html_content = italic_pattern.sub(r'<em>\1</em>', html_content)

    return html_content

def convert_tex_file_to_html(tex_file_path, html_file_path):
    with open(tex_file_path, 'r') as tex_file:
        tex_content = tex_file.read()
        html_content = tex_to_html(tex_content)

    with open(html_file_path, 'w') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python tex_compiler.py input.tex output.html")
        sys.exit(1)

    input_tex_file = sys.argv[1]
    output_html_file = sys.argv[2]

    convert_tex_file_to_html(input_tex_file, output_html_file)

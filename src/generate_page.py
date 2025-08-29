from markdown_blocks import markdown_to_html_node
from extract_title import extract_title
from pathlib import Path
import os

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):
        print(f'Generating page from {from_path} to {dest_path} using {template_path}.')

        #read markdown file at from path and store contents to variable
        with open(from_path, 'r') as file:
            markdown_content = file.read()

        # read template file at template path and store contnets to var
        with open(template_path, 'r') as file:
            template_content = file.read()

        # use markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
        html_content = markdown_to_html_node(markdown_content).to_html()

        # use extract_title fx to grab title
        title = extract_title(markdown_content)

        # replace {{ Title }} and {{ Content }} placeholders in the template with the HTML and title generated
        replace_title = template_content.replace('{{ Title }}', f'{title}')
        result_html = replace_title.replace('{{ Content }}', f'{html_content}')

        # write the new full HTML page to a file at dest_path, create new directories if they don't FileExistsError
        destination = os.path.dirname(dest_path)
        if destination:
            os.makedirs(destination, exist_ok=True)

        with open(dest_path, "w") as f:
            f.write(result_html)

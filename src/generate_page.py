from markdown_blocks import markdown_to_html_node
from extract_title import extract_title

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
        result_html = template_content.replace('{{ Title }}', f'{title}')
        result_html = template_content.replace('{{ Content }}', f'{html_content}')

        # write the new full HTML page to a file at dest_path, create new directories if they don't FileExistsError

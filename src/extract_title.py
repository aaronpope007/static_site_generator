
def extract_title(markdown):
    markdown_array = markdown.split('\n')
    header = ''

    for line in markdown_array:
        if line.startswith('# '):
            return line.lstrip('# ').rstrip()

    if header == '':
        raise Exception('This document needs a header: #')

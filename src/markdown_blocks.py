import re
from enum import Enum
from htmlnode import HTMLNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    heading_pattern = r'^#{1,6}\s'
    if re.match(heading_pattern, block):
        return BlockType.HEADING

    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    if all(line.startswith('>') for line in block.split('\n')):
        return BlockType.QUOTE

    if all(line.startswith('- ') for line in block.split('\n')):
        return BlockType.UNORDERED_LIST

    if all(line.startswith('. ') for line in block.split('\n')):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []


    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            block = text_to_textnodes(block)
            child_nodes = []
            for text_node in block:
                child_nodes.append(text_node_to_html_node(text_node))
                #creates and appends paragraph node
            block_nodes.append(HTMLNode("p", None, child_nodes, None))

        elif block_type == BlockType.HEADING:
            heading_num = block.count('#')
            block = text_to_textnodes(block.lstrip('#').strip())
            child_nodes = []
            for text_node in block:
                child_nodes.append(text_node_to_html_node(text_node))
            block_nodes.append(HTMLNode(f'h{heading_num}', None, child_nodes, None))

        elif block_type == BlockType.CODE:
            block = block[3:-3]
            code_block = TextNode(block, 'text')
            code_to_html_node = text_node_to_html_node(code_block)
            code_node = HTMLNode("code", None, [code_to_html_node], None)
            block_nodes.append(HTMLNode("pre", None, [code_node], None))

        elif block_type == BlockType.QUOTE:
            cleaned_lines = [line.lstrip('> ').lstrip() for line in block.split('\n')]
            joined_text = ' '.join(cleaned_lines)  # or '\n'.join(cleaned_lines) if you want to preserve line breaks
            text_nodes = text_to_textnodes(joined_text)
            child_nodes = [text_node_to_html_node(tn) for tn in text_nodes]
            block_nodes.append(HTMLNode("blockquote", None, child_nodes, None))

        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split('\n')
            list_item_nodes = []
            for line in lines:
                item_text = line.lstrip('-').lstrip()
                if not item_text:
                    continue
                text_nodes = text_to_textnodes(item_text)
                li_children = [text_node_to_html_node(tn) for tn in text_nodes]
                li_node = HTMLNode('li', None, li_children, None)
                list_item_nodes.append(li_node)
            block_nodes.append(HTMLNode('ul', None, list_item_nodes, None))


    return HTMLNode("div", None, block_nodes, None)
    #need:  ordered list

import re
from enum import Enum
from htmlnode import HTMLNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

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
            for text_node in block:
                text_node = text_node_to_html_node(text_node)




    # 1. split markdown into blocks
    # 2. based on type of block, create a new HTMLNode w proper data
    # 3. assign proper child HTMLNode objects to the block node
    #   use text to children(text) function
    #   textnode ->htmlnode
    # 4. code block is special case - dont use text to children
    #
    # 5. make all block nodes children under a single
    # parent HTML node (which should just be a div) and return it
    # 6. make unit tests

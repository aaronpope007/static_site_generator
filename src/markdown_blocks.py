import re
from enum import Enum


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

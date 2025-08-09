from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text).to_html()
    if text_node.text_type == TextType.BOLD:
        return LeafNode('b', text_node.text).to_html()
    if text_node.text_type == TextType.ITALIC:
        return LeafNode('i', text_node.text).to_html()
    if text_node.text_type == TextType.CODE:
        return LeafNode('code', text_node.text).to_html()
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception('Not a handled type')



def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)


main()

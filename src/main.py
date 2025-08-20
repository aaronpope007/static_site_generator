from textnode import TextNode, TextType
from copystatic import copy_static


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    copy_static('static', 'public')

main()

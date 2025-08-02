from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "plain_text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEXT = "code_text"
    LINK_TEXT = "link_text"
    IMAGE_TEXT = "image_text"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        if self.text_type in (TextType.LINK_TEXT, TextType.IMAGE_TEXT):
            if not self.url or not self.url.startswith("http"):
                raise ValueError("A valid URL must be provided for links and images.")

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return self.text == other.text and self.text_type == other.text_type and self.url == other.url
            
        else:
            return False
            

        #Create an __eq__ method that returns True if all of the properties of 
        #two TextNode objects are equal. 
        #Our future unit tests will rely on this method to compare objects.
        
    def __repr__():
        #method returns a string representation of the TextNode object
        #should look like this: TextNode(TEXT, TEXT_TYPE, URL)



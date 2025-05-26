import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_dif_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)       
        self.assertNotEqual(node, node2)
    
    def test_url_None_input(self):
        node = TextNode("Click here", TextType.LINKS)
        node2 = TextNode("Click here", TextType.LINKS, None)
        self.assertEqual(node.url, node2.url)



if __name__ == "__main__":
    unittest.main()

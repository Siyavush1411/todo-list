
import os

class TextMarkupBuilder:

    def text_aligner_print(text, align):
        def __init__(self, text):
            self.text = text
            
        def __getattr__(self, justify):
            positions = {
                
            }
        
        width = os.get_terminal_size().columns
        if align == 'left':
            print(text.ljust(width))
        elif align == "right":
            print(text.rjust(width))
        else:
            print(text.center(width))
        

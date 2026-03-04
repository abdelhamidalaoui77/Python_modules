"""
means code under that if name bla bla will only run WHEN that script is run 
directly.
NOT when it's called as an import.
(when importing all the code will run.. UNLESS it's under one of them 
if __name__ blocks)
"""
me = "NERD"

if __name__ == "__main__":
    me = "NOT A NERD"
    print(me)

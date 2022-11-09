from EarleyParser import parse
import argparse
import json

def main():
    arg_parser = argparse.ArgumentParser()
    
    arg_parser.add_argument("document_file", help = "File path to the sample document", nargs = '?', const = 1, type = str, default = "sample-document.txt")
    arg_parser.add_argument("grammar_file_json", help = "File path to the grammar json file", nargs = '?', const = 1, type = str, default = "sample-grammar.json")
    
    args = arg_parser.parse_args()
    
    try:
    # define a grammar
        document_filename = args.document_file
        grammar_filename = args.grammar_file_json
        
        print(str(grammar_filename))
        with open(grammar_filename) as grammar_file:
            grammar = json.load(grammar_file)
            
        with open(document_filename, "r") as f:
            document = f.read()
        
        parse(document, grammar)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Error while parsing document")
        print(e)

if __name__ == '__main__':
    main()
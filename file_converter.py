import markdown
import sys
import os

def main():
    if len(sys.argv) < 4:
        print("Error: Invalid number of arguments")
        sys.exit(1)

    command = sys.argv[1]
    inputpath = sys.argv[2]
    outputpath = sys.argv[3]

    if not command == "markdown":
        print("Error: Invalid command")
        sys.exit(1)

    if not inputpath.endswith(".md"):
        print("Error: Input file must be a markdown file")
        sys.exit(1)

    if not outputpath.endswith(".html"):
        print("Error: Output file must be an HTML file")
        sys.exit(1)

    with open(inputpath, "r") as infile:
        markdown_content = infile.read()
        html_content = markdown.markdown(markdown_content)

    with open(outputpath, "w") as outfile:
        outfile.write(html_content)
    
if __name__ == "__main__":
    main()
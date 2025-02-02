import re


def main():
    html = input("HTML: ")
    print(parse(html))


def parse(s):
    if link := re.search(r"<iframe src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>", s):
        return f"https://youtu.be/{link.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()

from urllib.parse import urlparse, unquote


def parse_after_question_mark(url):
    url = unquote(url)
    parsed_url = urlparse(url)
    params = parsed_url.query.split("&")

    dictionary = {}
    for param in params:
        if param != '':
            dictionary.update({param.split("=")[0] : param.split("=")[1]})
    return dictionary


def parse_between_quotes(pattern, url):
    url1 = unquote(pattern)
    parsed_url1 = urlparse(url1)
    url2 = unquote(url)
    parsed_url2 = urlparse(url2)

    path1 = parsed_url1.path
    path2 = parsed_url2.path

    path1_parts = list(filter(None, path1.split("/")))
    path2_parts = list(filter(None, path2.split("/")))

    dictionary = {}
    for i in range(len(path1_parts)):
        if path1_parts[i].startswith("<") and path1_parts[i].endswith(">"):
            if i < len(path2_parts):
                dictionary.update({path1_parts[i].strip("<>"):path2_parts[i]})
            else:
                dictionary.update({path1_parts[i].strip("<>"):None})
    return dictionary


if __name__ == "__main__":
    pattern = "/main/accounts/<id>/<name>"
    url = "/main/accounts/10/John?name=John&age=25"
    print(parse_after_question_mark(url))
    print(parse_between_quotes(pattern, url))
    # {'name': 'John', 'age': '25'}
    # {'id': '10', 'name': 'John'}

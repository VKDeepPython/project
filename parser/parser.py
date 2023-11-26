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
            sep = path1_parts[i][1:-1].split(":")
            try:
                if i < len(path2_parts):
                    if sep[0] == path1_parts[i][1:-1]:
                        dictionary.update({sep[0]:str(path2_parts[i])})
                    else:
                        if sep[1] == "str":
                            dictionary.update({sep[0]:str(path2_parts[i])})
                        elif sep[1]  == "int":
                            dictionary.update({sep[0]:int(path2_parts[i])})
                        else:
                            raise ValueError("Invalid format")
                else:
                    dictionary.update({sep[0]:None})
            except:
                raise ValueError("Invalid format")

    return dictionary


if __name__ == "__main__":
    pattern = "/main/accounts/<id:int>/<name:str>"
    url = "/main/accounts/10/John?name=John&age=25"
    print(parse_after_question_mark(url))
    print(parse_between_quotes(pattern, url))
    # {'name': 'John', 'age': '25'}
    # {'id': 10, 'name': 'John'}

import hypothesis


def make_annotation(username: str, token: str) -> str:
    h = hypothesis.Hypothesis(username=username, token=token)  # your h username and api token (from https://hypothes.is/account/developer)

    url = 'https://github.com/SemanticBeeng/Hypothesis'
    exact = 'annotation'
    prefix = ''
    suffix = ''
    title = 'title of the web page'
    tags = ["tag1", "tag2"]
    text = "found it"

    payload = {
        "uri": url,
        "target":
            [{
                "source": [url],
                "selector":
                    [{
                        "type": "TextQuoteSelector",
                        "prefix": prefix,
                        "exact": exact,
                        "suffix": suffix
                    }]
            }],
        "tags": tags,
        "text": text,
        "document": {
            "title": [title]
        },
        "permissions": h.permissions,
        "group": h.group
    }

    r = h.post_annotation(payload)
    # #print(r.status_code)
    return "abs"


def main():
    make_annotation("nickdsc", "6879-kqqV-XH4sr4nWjozKuohjb7bwKVBjzQhGVtptcjwsuk")


if __name__ == "__main__":
    main()

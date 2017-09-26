import hypothesis


def make_annotation(username: str, token: str, group: str) -> None:

    # your h username and api token (from https://hypothes.is/account/developer)
    h = hypothesis.Hypothesis(username=username, token=token, group=group)

    print('Permissions = ' + str(h.permissions))
    print('Group = ' + h.group)

    url = 'https://github.com/SemanticBeeng/Hypothesis'
    text2Match = 'wrapper'
    prefix = ''
    suffix = ''
    title = 'a match'
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
                        "exact": text2Match,
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
    print(r.status_code)


def main():
    make_annotation(username="nickdsc", token="6879-kqqV-XH4sr4nWjozKuohjb7bwKVBjzQhGVtptcjwsuk", group="ekcgroup")


if __name__ == "__main__":
    main()

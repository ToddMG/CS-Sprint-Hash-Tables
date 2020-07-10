# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # paths = []
    #
    # for query in queries:
    #     for filepath in files:
    #         print(f'query: {query}, filepath: {filepath}')
    #         if query in filepath:
    #             paths.append(filepath)
    #             print(filepath)
    # return paths
    #
    # grab the end of each filepath and make it a key whose values are the filepaths

    hash = {}
    paths = []

    for filepath in files:
        key = filepath.split('/')[-1]
        hash.setdefault(key, []).append(str(filepath))

    for query in queries:
        if query in hash:
            for value in hash[query]:
                paths.append(value)

    return paths


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

#!/python/usr/python3

if __name__ == "__main__":
    """print variable in hidden_4"""
    import hidden_4

    var = dir(hidden_4)
    for i in var:
        if i[0] == '_' and i[1] == '_':
            continue
        else:
            print(i)

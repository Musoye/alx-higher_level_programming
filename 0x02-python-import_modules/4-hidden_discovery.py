#!/python/usr/python3

if __name__ == "__main__":
    """print variable in hidden_4"""
    import hidden_4

    var = dir(hidden_4)
    for i in var:
        if i[:2] != "__":
            print(i)

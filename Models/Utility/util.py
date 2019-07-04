def removeInsideBrackets(item):
    start = item.find('(')

    if start == -1:
        return None

    end = item.find(')')

    return item[: start] + item[end + 1::]

def getInsideBrackets(item):
    start = item.find('[')

    if start == -1:
        return None

    end = item.find(']')

    return item[start + 1: end]


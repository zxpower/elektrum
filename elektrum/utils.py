  
def extract_one(text, start_str, end_str, offset = 0, inclusive = True):
    start = text.find(start_str, offset)
    end = text.find(end_str, start + len(start_str)) + len(end_str)
    if start < 0 or end < 0:
        return None, -1, -1
    if inclusive:
        return text[start:end], start, end
    else:
        return text[start+len(start_str):end-len(end_str)], start, end


def extract_all(text, start_str, end_str, offset = 0, inclusive = True):
    result = []
    while True:
        tmp, start, end = extract_one(text, start_str, end_str, offset, inclusive)
        if tmp == None:
            break
        result.append(tmp)
        offset = end
    return result

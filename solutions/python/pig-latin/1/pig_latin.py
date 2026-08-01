def translate(text):
    if " " in text:
        return " ".join(translate(word) for word in text.split())
    
    vowels = "aeiou"

    if text[0] in vowels or text[:2] == "xr" or text[:2] == "yt":
        return text + "ay"


    for i in range(len(text)):
        if text[i] in vowels:
            if text[i] == "u" and text[i-1] == "q":
                i+=1
            return text[i:] + text[:i] + "ay"
        if text[i] == "y" and i > 0:
            return text[i:] + text[:i] + "ay"

    return text + "ay"


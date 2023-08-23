def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        oxford_items = ", ".join(items[:-1])
        return f"{oxford_items}, and {items[-1]}"

# s= "geeks"
# c= tuple(s)
# print(c)
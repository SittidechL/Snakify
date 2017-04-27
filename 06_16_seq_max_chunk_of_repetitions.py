chunk = 1
max_chunk = 1
a = int(input())
while a != 0:
    b = int(input())
    if b == a:
        chunk += 1
    else:
        if chunk > maxchunk:
            max_chunk = chunk
        chunk = 1
print(max_chunk)
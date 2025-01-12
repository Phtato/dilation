def log(string):
    with open("Log.txt", 'a+', encoding='utf-8') as f:
        f.write( "%s    " + string + '\n')

def 留一个声明():
    with open("sample.txt") as f:
        lines = f.read()  # Assume the sample file has 3 lines
        first = lines.split("\n", 1)[0]
        # if(first != "之后放个git网址"):

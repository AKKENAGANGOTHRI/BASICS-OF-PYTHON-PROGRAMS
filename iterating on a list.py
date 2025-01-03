#creation of lists
prog_lang=['c','c++','java','python','flutter','cobalt','dart','javascript','react.js','express.js']
print(prog_lang)
print(type(prog_lang))
#without indexing
for i in prog_lang:
    print(i)
print("====================================================")
#with indexing
for i in range(len(prog_lang)):
    print(prog_lang[i])
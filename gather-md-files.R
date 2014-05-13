x = system("ls -d $(find .) | grep .md$", intern = TRUE) # read files with pathes
x = gsub("./", "", x, fixed = TRUE) # remove heading ./
cat(x, file = "markdown_files.txt", sep = " ")
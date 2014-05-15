import os
import re
from flask import Flask, request, render_template, url_for
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer, guess_lexer_for_filename

app = Flask(__name__)
app.debug = False

# get all the markdown files located in the working directory
# and all subdirectories
file_list = {}
for root, dirs, files in os.walk("."):
  for file in files:
    if (file.endswith(".md") or file.endswith(".markdown")):
      route = os.path.join(root, file)
      file_list[route] = os.path.abspath(route)
      print(os.path.abspath(file))


# def replace_codeblock(codeblock):
#   #print(codeblock.group(0))
#   codeblock = codeblock.group(0) # get entire match as string
#   codeblock = re.sub(r"```.+(\s)?", "", codeblock)
#   print("REPLACING")
#   return highlight(codeblock, lexer, HtmlFormatter())


# f = open("README.md")
# fc = f.read()
# subs = re.findall(r"```[a-zA-z]+\s.*```", fc, re.S)
# subs = subs[0].replace("```", "")
# print(subs)
# lang = re.findall(r"^[a-zA-z]+\s", subs)[0]
# lang = lang[0:(len(lang)-1)]
# lexer = get_lexer_by_name(lang)
# regex = re.compile(r"```[a-zA-z]+\s.*```", re.S)
# fc = re.sub(regex, replace_codeblock, fc)
# print("DONE!!!")
# print(fc)


@app.route('/')
@app.route('/<markdown>')
def hello(markdown = None):
  return render_template('preview.html', name = "Jakob", file_list = file_list)

@app.route('/preview')
def preview():
  # get request param
  file = request.args.get('markdown', '')
  # debug
  #print("Fetching file " + file)
  # open file and return content
  f = open(file)
  fc = f.read()

  #FIXME: this is so unbelievably ugly
  subs = re.findall(r"```[a-zA-z]+\s.*```", fc, re.S)
  if (len(subs) == 0):
    return fc
  subs = subs[0].replace("```", "")
  #print("FOUND following:")
  #print(subs)
  lang = re.findall(r"^[a-zA-z]+\s", subs)[0]
  lang = lang[0:(len(lang)-1)]
  lexer = get_lexer_by_name(lang)
  #print(lexer)
  def replace_codeblock(codeblock):
    #print(codeblock.group(0))
    codeblock = codeblock.group(0) # get entire match as string
    codeblock = re.sub(r"```.*(\s)?", "", codeblock)
    print("REPLACING")
    return highlight(codeblock, lexer, HtmlFormatter())

  regex = re.compile(r"```[a-zA-z]+\s.*```\s", re.S)
  print(re.findall(regex, fc))
  fc = re.sub(regex, replace_codeblock, fc)
  #print("DONE!!!")
  #print(fc)

  return fc

if __name__ == "__main__":
    app.run()

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
def getMarkdownFiles(source_dir = "."):
  file_list = {}
  for root, dirs, files in os.walk(source_dir):
    for file in files:
      if (file.endswith(".md") or file.endswith(".markdown")):
        route = os.path.join(root, file)[2:]
        file_list[route] = os.path.abspath(route)
  return file_list

def highlight_codeblocks(sourcecode):
  #FIXME: this is so unbelievably ugly
  subs = re.findall(r"```[a-zA-z]+\s.*```", sourcecode, re.S)
  if (len(subs) == 0):
    return sourcecode
  subs = subs[0].replace("```", "")
  #print(subs)
  lang = re.findall(r"^[a-zA-z]+\s", subs)[0]
  lang = lang[0:(len(lang)-1)]
  lexer = get_lexer_by_name(lang)
  #print(lexer)
  def replace_codeblock(codeblock):
    codeblock = codeblock.group(0) # get entire match as string
    codeblock = re.sub(r"```.*(\s)?", "", codeblock)
    return highlight(codeblock, lexer, HtmlFormatter())

  regex = re.compile(r"```[a-zA-Z]+\s.*?```", re.S)
  sourcecode = re.sub(regex, replace_codeblock, sourcecode)
  return sourcecode

@app.route('/')
def hello(markdown = None):
  file_list = getMarkdownFiles()
  return render_template('preview.html', file_list = file_list)

@app.route('/preview')
def preview():
  # get request param
  file = request.args.get('markdown', '')
  # open file and return content
  f = open(file)
  fc = f.read()

  # pygmentize source code blocks
  result = highlight_codeblocks(fc)

  return result

if __name__ == "__main__":
    app.run()

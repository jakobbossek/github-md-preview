import os
from flask import Flask, request, render_template, url_for

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


@app.route('/')
@app.route('/<markdown>')
def hello(markdown = None):
  return render_template('preview.html', name = "Jakob", file_list = file_list)

@app.route('/preview')
def preview():
  # get request param
  file = request.args.get('markdown', '')
  # debug
  print("Fetching file " + file)
  # open file and return content
  a_file = open(file)
  return a_file.read()

if __name__ == "__main__":
    app.run()

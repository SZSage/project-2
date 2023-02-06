"""
Simon Zhao's Flask API."
"""

import os
import configparser
from flask import Flask, send_from_directory, abort


app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World!"

@app.route("/<path:request>")
def send_file(request): 

    file_path = os.path.join("pages/", request) # added file_path variable to allow for subdirectories in web/pages folder

    if "~" in request or ".." in request: 
        return abort(403) 

    elif os.path.isfile(file_path) and os.access(file_path, os.R_OK): 
        return file_found(request) # added function to return file found 
    else: 
        return abort(404) 

@app.errorhandler(404) 
# added 404 error handler
def error_404(e): 
    return send_from_directory("pages/", "404.html"), 404 

@app.errorhandler(403) 
# added 403 error handler
def error_403(e): 
    return send_from_directory("pages/", "403.html"), 403

def file_found(filename): 
    # added function to return file found
    return send_from_directory("pages/", filename), 200
 
def parse_config(config_paths): 
    # added function to parse config file
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config
 
config = parse_config(["credentials.ini", "default.ini"])
config_port = config["SERVER"]["PORT"]
debug_config = config["SERVER"]["DEBUG"]

if __name__ == "__main__":
    print("Running on port:", config_port) 
    app.run(debug=debug_config, host="0.0.0.0", port=int(config_port))   # type: ignore
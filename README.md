# $ jinja2
A CLI interface to Jinja2
```
$ jinja2 helloworld.tmpl data.json --format=json
$ cat data.json | jinja2 helloworld.tmpl
$ curl -s http://httpbin.org/ip | jinja2 helloip.tmpl
$ curl -s http://httpbin.org/ip | jinja2 helloip.tmpl > helloip.html
```

## Install
`$ pip install jinja2-cli`

## Usage
```
Usage: jinja2 [options] <input template> <input data> [<input data>, <input data>, ...]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  --format=FORMAT       format of input variables: auto, ini, json,
                        querystring, yaml, yml
  -e EXTENSIONS, --extension=EXTENSIONS
                        extra jinja2 extensions to load
  -D key=value          Define template variable in the form of key=value
  -s SECTION, --section=SECTION
                        Use only this section from the configuration
  --strict              Disallow undefined variables to be used within the
                        template
```

## Optional YAML support
If `PyYAML` is present, you can use YAML as an input data source.

`$ pip install jinja2-cli[yaml]`

## Optional TOML support
If `toml` is present, you can use TOML as an input data source.

`$ pip install jinja2-cli[toml]`

## Optional XML support
If `xmltodict` is present, you can use XML as an input data source.

`$ pip install jinja2-cli[xml]`

## Optional support for Markdown Jinja2 filter
If you have the `Markdown` python package installed you can use the Markdown Jinja2 filter:

```
$ cat md.j2
{{ content|markdown }}

$ cat var.json
{"content": "#this is markdown"}

$ jinja2 -M md.j2 var.json
<h1>this is markdown</h1>
```

## Support for a special "Include" key
Trough the command line option `--include <include_key>` you can define a key name to be used to define a list of data files to include:

```
$ cat tests/files/template1.j2
var1: {{ var1 }}
var2: {{ var2 }}

arr1:
{% for var in arr1 %}
    {{ var }}: {{ arr1[var] }}
{% endfor %}

var10: {{ var10 }}

$ cat tests/files/test.json
{ "_include": ["tests/files/included.json"],
  "var1": "val1",
  "var2": "val2",
  "arr1": {
        "arr_var1": "arr_var1",
        "arr_var2": true
  }
}

$ cat tests/files/included.json
{
    "var1": "new_var1",
    "var10": "val 10"
}

$ python jinja2cli/cli.py --include _include tests/files/template1.j2 tests/files/test.json
var1: new_var1
var2: val2

arr1:

    arr_var1: arr_var1

    arr_var2: True


var10: val 10
```

## TODO
 [] Refactor the file inclusions and multiple data file
 [] Variable inheritance and overrides
 [] Tests!

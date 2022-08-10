import json, glob, os, re
from json import JSONDecodeError
import jstyleson

SOURCE_PATH = r'D:\vivaldi-source_5.4.2753\vivaldi-source'

def getAllApiDefsInSourceBundle():
    return glob.glob(os.path.join(SOURCE_PATH, 'extensions/schema/*.json'))

def processApiDef(filename):
    with open(filename) as jsonfile:
        return jstyleson.load(jsonfile)

def getDescription(name, typeDict, paragraph=True):
    para = '<p>' if paragraph else ''
    if 'description' in typeDict:
        return para + str(typeDict['description'])
    else:
        # print("WARNING: No description for "+name)
        return para + " ⚠ NO DESCRIPTION PROVIDED"

def optional(typeDict):
    return '(optional) ' if 'optional' in typeDict and typeDict['optional'] else ''

def typeToHtml(name, prop, makeTopLevel=False):
    # makeTopLevel decides if a linkable anchor ID should be given
    out = ''
    if type(prop) == type(True):
        out += f'''<dl><dt>{name}</dt><dd>'''
        out += '''<pre>True</pre></dd></dl>
        '''
    elif 'enum' in prop: # enum of values
        out += f'''<dl><dt><code>ENUM</code></dt><dd>'''
        out += optional(prop)
        out += getDescription(name, prop)
        for enum in prop['enum']:
            if type(enum) is str:
                out += f'''<li>{enum}'''
            else:
                out += f'''<li>{enum['name']}: {getDescription(enum['name'], enum, False)}'''
        out += '''</ul></dd></dl>
        '''
    elif '$ref' in prop: # referenced to a special vType
        out += f'''<dl><dt>{name}</dt><dd>'''
        out += optional(prop)
        out += f'''<pre><a href="#{prop['$ref']}">{prop['$ref']}</a></pre>'''
        out += getDescription(name, prop)
        out += '''</dd></dl>
        '''
    elif 'choices' in prop: # ?
        for choice in prop['choices']:
            out += typeToHtml(name + " (overloaded)", choice)
        out += '''</dd></dl>
        '''
    elif 'type' in prop and prop['type'] in ['number', 'integer', 'string', 'boolean', 'any', 'binary']:
        out += f'''<dl><dt>{name}</dt><dd>'''
        out += optional(prop)
        out += f'''<pre>{prop['type']}</pre>'''
        out += getDescription(name, prop)
        out += '''</dd></dl>
        '''
    elif 'type' in prop and prop['type'] == 'array':
        out += f'''<dl><dt>{name}</dt><dd>'''
        out += optional(prop)
        out += getDescription(name, prop)
        out += '''<p><code>Array</code> of:
        <ul>'''
        for listtypekey, listtypeval in prop['items'].items():
            out += f'''<li>{listtypeval}'''
        if 'minItems' in prop:
            out += 'Minimum items: ' + str(prop['minItems'])
        if 'maxItems' in prop:
            out += 'Maximum items: ' + str(prop['maxItems'])
        out += '''</ul></dd></dl>
        '''
    elif 'type' in prop and prop['type'] == 'object':
        out += f'''<dl><dt>{name}</dt><dd>'''
        out += optional(prop)
        if 'isInstanceOf' in prop:
            out += f'''<pre>{prop['type']} : {prop['isInstanceOf']}</pre>'''
        else:
            out += f'''<pre>{prop['type']}</pre>'''
        out += getDescription(name, prop)
        out += '''<p>Object Properties:'''
        if 'isInstanceOf' in prop:
            out += '⚠ Additional Properties extending type: ' + str(prop['additionalProperties'])
            print("Warning: Extended type, documentation not supported for " + name)
        if 'properties' in prop:
            for key, val in prop['properties'].items():
                out += typeToHtml(key, val)
        if 'additionalProperties' in prop:
            for key, val in prop['additionalProperties'].items():
                out += typeToHtml(key, val)
        out += '''</dd></dl>
        '''
    elif ('type' in prop and prop['type'] == 'function') or (name == 'reset' and 'parameters' in prop):
        if makeTopLevel:
            out += f'''<h3 id='{name}'><a href='#{name}'>#</a>{name}</h3>'''
        else:
            out += f'''<dl><dt>{name}</dt><dd>'''
        out += getDescription(name, prop)
        if 'parameters' in prop and len(prop['parameters']) > 0:
            out += '''<p>Parameters:'''
            for param in prop['parameters']:
                out += typeToHtml(param['name'], param)
        if not makeTopLevel:
            out += '''</dd></dl>
            '''
    elif prop == 'any':
        out += f'''<dl><dt>{name}</dt><dd>'''
        out += optional(prop)
        out += getDescription(name, prop)
        out += '''<pre>any</pre></dd></dl>
        '''
    else:
        raise Exception('BAD vTYPE PROP TYPE '+prop['type'])
    return out


def convertVivaldiTypeToHtml(api):
    out = ''
    out += f'''<h3 id='{api['id']}'><a href='#{api['id']}'>#</a>{api['id']}</h3>'''
    if 'properties' in api:
        out += getDescription(api['id'], api)
        out += '''<p>Properties:<dl>'''
        for id, val in api['properties'].items():
            out += typeToHtml(id, val)
        out+='''</dl>
        '''
    else:
        out += typeToHtml(api['id'], api)
    return out

def convertListenerToHtml(api):
    if 'type' not in api or api['type'] != 'function':
        print("WARNING! Listener is not a function type: " + api['name'])
        return "<dl><dt>api['name']</dt><dd>⚠ WARNING! Failed to get info as type not provided</dd></dl>\n"
    return typeToHtml(api['name'], api, True)

def convertMethodToHtml(api):
    if 'type' not in api or api['type'] != 'function':
        if api['name'] == 'reset':
            return typeToHtml(api['name'], api, True)
        print("WARNING! Method is not a function type: " + api['name'])
        return "<dl><dt>api['name']</dt><dd>⚠ WARNING! Failed to get info as type not provided</dd></dl>\n"
    return typeToHtml(api['name'], api, True)

def makeNav(apis):
    out = '''<nav class='side'>
    <img src="IDR_PRODUCT_LOGO.png">
    <p>Vivaldi Modders API
    <br />Internal Documentation
    <br /><ul>
    '''
    for api in apis:
        out += f'''<li><a href="{api['namespace']}.html">{api['namespace']}</a></li>'''
    out += f'''<li><a href="preferenceDefinitions.html">Preference Definitions</a></li>
    <li><a href="everything.html">Search Everything</a></li>
    </ul><footer>Generated from official <a href="https://vivaldi.com/source">Sources</a>
    <p>Version {version()}, by LonMcGregor.
    <p>This website is not affiliated with vivaldi.
    <p><a href="https://github.com/LonMcGregor/VivaldiModdersAPI">Discuss this project on GitHub</a></footer></nav>
    '''
    return out

def makeContents(types, listeners, methods):
    out = '''<nav class='contents' id='top'>
    <h2>Navigation</h2>
    <h3>Types</h3>
    <ul>'''
    for vtype in types:
        out += f'''<li><a href='#{vtype['id']}'>{vtype['id']}</a>'''
    out += '''</ul>
    <h3>Listeners</h3>
    <ul>'''
    for vtype in listeners:
        out += f'''<li><a href='#{vtype['name']}'>{vtype['name']}</a>'''
    out += '''</ul>
    <h3>Methods</h3>
    <ul>'''
    for vtype in methods:
        out += f'''<li><a href='#{vtype['name']}'>{vtype['name']}</a>'''
    out += '''</ul></nav>'''
    return out

def convertDefsToHtml(api, sidebar):
    apiname = api['namespace']
    # get all types
    types = api['types'] if 'types' in api else []
    # get all listeners
    listeners = api['events'] if 'events' in api else []
    # get all methods
    methods = api['functions'] if 'functions' in api else []
    out = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>vivaldi.{apiname}</title>
    <link rel="stylesheet" href="style.css">
    <link href="IDR_PRODUCT_LOGO.png" rel="icon">
    </head>
    <body>
    {sidebar}
    <main>
    <a id="backToTop" href="#top">Go back to top</a>
    <h1>vivaldi.{apiname} Modders API Reference</h1>
    <p>{api['description']}
    {makeContents(types, listeners, methods)}
    '''
    if len(types) > 0:
        out += f'''
        <h2>Types</h2>
        '''
        for vtype in types:
            out += convertVivaldiTypeToHtml(vtype)
    if len(listeners) > 0:
        out += f'''
        <h2>Listeners</h2>
            <details>
            <summary>
                <h3 id="listenerHelp">How to use listeners</h2>
            </summary>
            <p>Each listener type has the same functions, used for each listener API in the same way:</p>
            <div class="method">
                <h4>.addListener(<code>function</code> callback)</h4>
                <p>Adds a function to a listener for an event</p>
            </div>
            <div class="method">
                <h4>.removeListener(<code>function</code> callback)</h4>
                <p>Removes a function to a listener for an event</p>
            </div>
            <div class="method">
                <h4>.hasListener(<code>function</code> callback)</h4>
                <p>Returns a boolean if a function is attached to a listener for an event</p>
            </div>
            <div class="method">
                <h4>.hasListeners()</h4>
                <p>Returns a boolean if a listener has any attached functions</p>
            </div>
            <div class="method">
                <h4>.dispatch()</h4>
                <p>Returns array of promises dispatched to the listener</p>
            </div>
        </details>
        '''
        for vlist in listeners:
            out += convertListenerToHtml(vlist)
    if len(methods) > 0:
        out += f'''
        <h2>Methods</h2>
        '''
        for vmeth in methods:
            out += convertMethodToHtml(vmeth)
    out += '</main></body></html>'
    return out

def prefContents(data):
    out = '''<nav class='contents' id='top'><h2>Navigation</h2><ul>'''
    for k, v in data['vivaldi'].items():
        out += f'''<li><a href='#{k}'>{k}</a>'''
    out += '''<li><a href="#cprefs">Chromium Prefs</a></li></ul></nav>'''
    return out

def doAPref(path, k, v, out):
    out.write(f'''<dl id="{path[:-1]}"><dt><a href="#{path[:-1]}">#</a>{path[:-1]}</dt><dd>''') # trim off the trailing path dot
    out.write(getDescription(path, v))
    out.write(f'''<pre>`{v['type']}`</pre>''')
    if v['type'] == 'enum':
        out.write('<ul>')
        for ek, ev in v['enum_values'].items():
            out.write(f'''<li>{ek}{' (Default)' if ek == v['default'] else ''}</li>''')
    elif v['type'] == 'dictionary':
        out.write('<p>Default: %s\n' % str(v['default']))
    elif v['type'] in ['string', 'integer', 'boolean', 'double', 'list', 'file_path']:
        if v['default'] == '':
            out.write('''<p>Default: ''\n''')
        else:
            out.write('<p>Default: %s\n' % v['default'])
    else:
        print("WARNING! unknown type: %s" % v['type'])
        out.write("⚠ WARNING! unknown type: %s" % v['type'])
    out.write('</dd></dl>')

def doAChromePref(k, v, out):
    out.write(f'''<dl><dt>{v['path']}</dt><dd>''')
    out.write(f'''<pre>`{v['type']}`</pre>''')
    out.write(f'''<p>Internal key: {k}</dd></dl>''')

def doPrefs(path, k, v, out, depth=0):
    if depth == 0:
        out.write(f'''<h3 id="{k}"><a href="#{k}">#</a>{k}</h3>''')
    if 'type' in v:
        doAPref(path, k, v, out)
    else:
        for subk, subv in v.items():
            doPrefs(path + subk + '.', subk, subv, out, depth+1)

def processPreferences(sidebar):
    prefDefs = json.load(open(os.path.join(SOURCE_PATH, 'vivapp/src/prefs_definitions.json'), 'r'))
    with open('preferenceDefinitions.html', 'w', encoding='utf-8') as out:
        out.write(f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>vivaldi preferences</title>
        <link rel="stylesheet" href="style.css">
        <link href="IDR_PRODUCT_LOGO.png" rel="icon">
        </head>
        <body>
        {sidebar}
        <main>
        <a id="backToTop" href="#top">Go back to top</a>
        <h1>vivaldi preferences Modders API Reference</h1>
        {prefContents(prefDefs)}
        ''')

        out.write('<h2 id="vprefs">Vivaldi Prefs</h2>')
        for k, v in prefDefs['vivaldi'].items():
            doPrefs('vivaldi.'+k+'.', k, v, out)

        out.write('<h2 id="cprefs">Chromium Prefs</h2>')
        for k, v in prefDefs['chromium'].items():
            doAChromePref(k, v, out)
        for k, v in prefDefs['chromium_local'].items():
            doAChromePref(k, v, out)

        out.write('</main></body></html>')

def prepareEverythingFile(sidebar):
    everythingfile = open('everything.html', 'w', encoding='utf-8')
    everythingfile.write(f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Search whole Vivaldi API</title>
        <link rel="stylesheet" href="style.css">
        <link href="IDR_PRODUCT_LOGO.png" rel="icon">
        </head>
        <body>
        {sidebar}
        <main>
        <a id="backToTop" href="#top">Go back to top</a>''')
    return everythingfile

def getContentOnlyForEverythingFile(deftoHtml, apiname):
    start = deftoHtml.find('</ul></nav>')+len('</ul></nav>')
    end = deftoHtml.find('</main>')
    content = deftoHtml[start:end]
    anchorre = '''<a href='#(\w+)'>'''
    anchorsub = f'''<a href='{apiname}.html#\\1'>'''
    resetAnchors = re.sub(anchorre, anchorsub, content)
    wholefile = f'''<h1><a href='{apiname}.html'>{apiname}</a></h1>\n''' + resetAnchors
    return wholefile

def writeAllToFile():
    files = getAllApiDefsInSourceBundle()
    apiDefs = [processApiDef(file) for file in files]
    # they are all 1 level deep, move them up
    extractedApiDefs = []
    for apis in apiDefs:
        for api in apis:
            extractedApiDefs.append(api)
    sidebar = makeNav(extractedApiDefs)
    everythingfile = prepareEverythingFile(sidebar)
    for api in extractedApiDefs:
        with open(api['namespace']+'.html', "w", encoding='utf-8') as outfile:
            defToHtml = convertDefsToHtml(api, sidebar)
            outfile.write(defToHtml)
            everythingContent = getContentOnlyForEverythingFile(defToHtml, api['namespace'])
            everythingfile.write(everythingContent)
    processPreferences(sidebar)
    with open('preferenceDefinitions.html', 'r', encoding='utf-8') as prefsfile:
        prefscontent = prefsfile.read()
        everythingContent = getContentOnlyForEverythingFile(defToHtml, 'preferenceDefinitions')
        everythingfile.write(everythingContent)
    everythingfile.write('''</main></body></html>''')
    everythingfile.close()

def version():
    with open(os.path.join(SOURCE_PATH, 'VIVALDI_VERSION'), 'r') as f:
        major = f.readline()[len('VIVALDI_MAJOR='):].strip()
        minor = f.readline()[len('VIVALDI_MINOR='):].strip()
    return str(major)+'.'+str(minor)

writeAllToFile()

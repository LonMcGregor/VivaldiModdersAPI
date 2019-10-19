import json

file = open('/mnt/c/Users/L/AppData/Local/VivaldiStable/Application/2.8.1664.40/resources/vivaldi/prefs_definitions.json')
data = json.load(file)
mds = '# Prefs Definitions\n'
with open('./prefs.md', 'w') as md:
    def doAPref(path, k, v):
        md.write('### %s\n' % path[:-1]) # trim off the trailing path dot
        if 'description' in v:
            md.write('%s\n\n' % v['description'])
        md.write('Type: `%s`\n\n' % v['type'])
        if v['type'] == 'enum':
            md.write('Enum|Notes\n')
            md.write('---|---\n')
            for ek, ev in v['enum_values'].items():
                if ek == v['default']:
                    md.write('%s|*Default*\n' % ek)
                else:
                    md.write('%s|\n' % ek)
        elif v['type'] == 'dictionary':
            md.write('Default: %s\n' % str(v['default']))
        elif v['type'] in ['string', 'integer', 'boolean', 'double', 'list', 'file_path']:
            if v['default'] == '':
                md.write('''Default: ''\n''')
            else:
                md.write('Default: %s\n' % v['default'])
        else:
            print("unknown type: %s" % v['type'])
        md.write('\n')

    def doAChromePref(k, v):
        md.write('### %s\n' % v['path'])
        md.write('Type: `%s`\n\n' % v['type'])
        md.write('Internal key: *%s*\n\n' % k)

    def doPrefs(path, k, v):
        if 'type' in v:
            doAPref(path, k, v)
        else:
            for subk, subv in v.items():
                doPrefs(path + subk + '.', subk, subv)

    md.write('## Vivaldi Prefs\n')
    for k, v in data['vivaldi'].items():
        doPrefs('vivaldi.'+k+'.', k, v)

    md.write('## Chromium Prefs\n')
    for k, v in data['chromium'].items():
        doAChromePref(k, v)
    for k, v in data['chromium_local'].items():
        doAChromePref(k, v)

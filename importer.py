from glob import glob
import json
import yaml

def old_post_handler(filename):
    """returns dict of data plus text"""
    data_lines = []
    markdown_lines = []
    seperated = False
    with open(filename) as f:
        for line in f.readlines():
            if seperated == False and line.startswith('---'):
                seperated = True
            elif seperated == False:
                data_lines.append(line)
            elif seperated == True:
                markdown_lines.append(line)

    return json.loads(''.join(data_lines)), ''.join(markdown_lines)

def new_post_builder(filename, data, markdown):
    new_filename = filename.replace('../mountain/', 'blog/')
    data['published'] = True
    data['date'] = data['date'].split()[0]
    data['timeToRead'] = round(len(markdown.split()) / 200)
    data['time_to_read'] = round(len(markdown.split()) / 200)
    with open(new_filename, 'w') as f:
        f.write('---\n')
        f.write(yaml.dump(data))
        # for key, value in data.items():
        #     if key == 'tags':
        #         f.write(f'{key}:\n')
        #         for entry in value:
        #             f.write(f'  - {entry}\n')
        #     else:
        #         f.write(f'{key}: "{value}"\n')
        f.write('---\n\n')
        f.write(markdown)
    print(new_filename)


for filename in glob('../mountain/posts*/*.md'):
    print(filename)
    data, markdown = old_post_handler(filename)
    new_post_builder(filename, data, markdown)
    
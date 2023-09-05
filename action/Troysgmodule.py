import requests

# Method to get surge module content
def get_module_content(module_urls):
    config_dict = dict()
    for module_url in module_urls:
        module_text = requests.get(module_url).text
        section_key = ''
        for raw_line in module_text.split('\n'):
            if raw_line.startswith('#'):
                pass
            elif raw_line.startswith('['):
                section_key = raw_line.rstrip()
                if section_key not in config_dict:
                    config_dict[section_key] = list()
            else:
                line_content = raw_line.rstrip()
                if line_content:
                    if section_key:
                        if line_content not in config_dict[section_key]:
                            config_dict[section_key].append(line_content + '\n')
                        else:
                            print(line_content + ' is duplicated')
                    else:
                        print(line_content + ' has no section_key')
    return config_dict


sgmodules = ['https://raw.githubusercontent.com/Peng-YM/Sub-Store/master/config/Surge.sgmodule',
             'https://raw.githubusercontent.com/mieqq/mieqq/master/skip-proxy-lists.sgmodule']

config_combine = get_module_content(sgmodules)


config_combine = get_module_content(sgmodules)


# write to file
with open('./sgmodule/Troy.sgmodule', 'w') as f:
    f.writelines(['#!name=Troy@Surge\n', '#!desc=Some thing.\n', '\n'])
    for section_key in config_combine:
        f.write(section_key + '\n')
        if section_key == '[MITM]':
            f.write('hostname = %APPEND%' + ','.join(
                [item.split('%APPEND%')[-1].rstrip() for item in config_combine[section_key]]) + '\n')
        else:
            f.writelines(config_combine[section_key])
        f.write('\n')

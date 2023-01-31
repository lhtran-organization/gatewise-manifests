#!/bin/python
from ruamel.yaml import YAML

with open('images', 'r') as image_file:
    deploy_image = image_file.readline().strip()

with open('deployment.yaml', 'r') as yaml_file:
    yaml=YAML(typ='rt')
    data = list(yaml.load_all(yaml_file))
    for doc in data:
        if doc['kind'] == 'Deployment':
            for container in doc['spec']['template']['spec']['containers']:
                if container['image'].startswith('longhtran91/gatewise'):
                    container['image'] = deploy_image
                    break
            break

with open('deployment.yaml', 'w') as dump_file:
    yaml.dump_all(data, dump_file)

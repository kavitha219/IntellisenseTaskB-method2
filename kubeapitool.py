#!/usr/bin/env python3
#
# Intellisense DevOps Test B
#
# Notes
# -----------------
# Images of each deployment I understand that as a number of replicas available on the deployment, if we want to know the images of each deployment [pod list, and then image]
# Date of deployment was updated. I understood that as the last time the deployment got an update in the pod count, pod restarted or whatever. 

import argparse
import tabulate
from kubernetes import client, config

# Create new parser
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--namespace", type=str, help="The specific namespace we want to list", default='all')
parser.add_argument("-c", "--config", type=str, help="Use specific kubeconfig file", default='~/.kube/config')
args = parser.parse_args()

# Create the layout of table.
headers = ['Deployment', 'Namespace', 'Replicas', 'Avaliabe Replicas', 'Unavailable Replicas', 'Created', 'Last Update']
rows = []

# Configs can be set in Configuration class directly or by using helper utility
# By default it will read the ~/.kube/config configuration file.
config.load_kube_config(config_file=args.config)
apps = client.AppsV1Api()
if args.namespace == "all":
    deployments = apps.list_deployment_for_all_namespaces(watch=False)
else:
    deployments = apps.list_namespaced_deployment(args.namespace,watch=False)
for i in deployments.items:
    if i.status.unavailable_replicas == None:
        i.status.unavailable_replicas = 0
    rows.append([i.metadata.name, i.metadata.namespace, i.status.replicas, i.status.available_replicas, i.status.unavailable_replicas, i.metadata.creation_timestamp, i.status.conditions[1].last_update_time])

print(tabulate.tabulate(rows, headers, tablefmt="grid")) 
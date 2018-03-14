#!/usr/bin/env python

from __future__ import print_function

import jinja2
import sys

tf_cluster_template_file = 'tf_cluster_template.yaml.jinja'
tf_single_template_file = 'tf_single_template.yaml.jinja'

if len(sys.argv) != 4 and len(sys.argv) != 6:
    print(
        "Distributed tensorflow job usage: python render_template.py [project_name] [single] [ps_task_number] [worker_task_number]",
        file=sys.stderr)
    print(
        "Single tensorflow job usage: python render_template.py [project_name] [cluster] [ps_task_number] [worker_task_number]",
        file=sys.stderr)
    sys.exit(1)

mode = sys.argv[1]

if mode == 'single':
    template_file = tf_single_template_file
    project_name = sys.argv[3]
    with open(template_file, "r") as f:
        print(jinja2.Template(f.read()).render(project_name=project_name))
elif mode == 'cluster':
    template_file = tf_cluster_template_file
    project_name = sys.argv[3]
    ps_replicas = sys.argv[4]
    worker_replicas = sys.argv[5]
    with open(template_file, "r") as f:
        print(jinja2.Template(f.read()).render(project_name=project_name, ps_replicas=ps_replicas,
                                               worker_replicas=worker_replicas))
else:
    print("Distributed tensorflow job usage: python render_template.py [project_name] [single] [ps_task_number] [worker_task_number]", file=sys.stderr)
    print("Single tensorflow job usage: python render_template.py [project_name] [cluster] [ps_task_number] [worker_task_number]", file=sys.stderr)
    sys.exit(1)

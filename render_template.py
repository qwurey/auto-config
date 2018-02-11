#!/usr/bin/env python

from __future__ import print_function

import jinja2
import sys


if len(sys.argv) != 5:
    print("usage: {} [template-file] [project_name] [ps_task_number] [worker_task_number]".format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)
template_file = sys.argv[1]
project_name = sys.argv[2]
ps_replicas = sys.argv[3]
worker_replicas = sys.argv[4]
with open(template_file, "r") as f:
    print(jinja2.Template(f.read()).render(project_name=project_name, ps_replicas=ps_replicas, worker_replicas=worker_replicas))
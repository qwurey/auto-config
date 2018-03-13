#### Introduction

Start a tensorflow job on kubernetes by auto configuration.



#### Usage

command:

```shell
python render_template.py tfcluster_template_v0.yaml.jinja boc-web-predict 1 2 > tfcluster_job1.yaml
```



instructions：

```shell
render_template.py: is a render script which task is to transform confiuration commands to a complete kubernetes' yaml configuration file.
tfcluster_template_v0.yaml.jinja: is a typical configuration template file about a distributed tensorflow job on k8s.
boc-web-predict: distributed tensorflow project name
1: ps task number
2: worker task number
```


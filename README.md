#### I. Introduction
1. Create kubernetes' configuration yaml file according to target template.

2. There are typical two template file, one is for single tensorflow job, the other is for distributed tensorflow job.

  ```shell
  single tensorflow job: tf_single_template.yaml.jinja
  distributed tensorflow job: tf_cluster_template.yaml.jinja
  ```

3. And before create, you need to choose one template file and edit this file according to your specific tensorflow job configuration.



<br>

#### II. Single Tensorflow Job Usage

1. Edit this file to config train_data_file_name, train_code_file_name, model_name, image if necessary.

  ```shell
  vim tf_single_template_v0.yaml.jinja
  ```

  ​

  A kubenetes' job name is like: {{ project_name }}-{{ model_name }}

  For example：boc-web-predict-ckpt-198d-8f-322



2. Upload corresponding files to NFS(192.168.210.19).

  ```shell
  mkdir -p /dcdp/src/{{ project_name }}
  mkdir -p /dcdp/data/{{ project_name }}

  upload {{ train_data_file }} to /dcdp/data/{{ project_name }}
  upload {{ train_code_file }} to /dcdp/src/{{ project_name }}
  ```

  ​


3. Create a kubernetes' configuration file about the target tensorflow job.

  ```shell
  python render_template.py {{ mode }} {{ template_file_name }} {{ project_name }} > {{ target_configuration_file }}
  ```

  For example:

  ```shell
  python render_template.py single tf_single_template.yaml.jinja boc-web-predict > tf_single_job_1.yaml
  ```

  ​

  Tips:

  1> mode: single -> single tensorflow job

  2> template_file_name: tf_single_template.yaml.jinja -> your template file after edited specially

  3> project_name: boc-web-predict -> your target project name

  4> target_configuration_file: tf_single_job_1.yaml -> your target configuration file name
  ​

4. Submit the kubernetes' configuration file.

  ```shell
  kubectl create -f {{ target_configuration_file }}
  ```

  For example: 

  ```shell
  kubectl create -f tf_single_job_1.yaml
  ```


5. If necessary, delete the target job.

  ```shell
  kubectl delete jobs {{ project_name }}-{{ model_name }} --namespace=dcdp
  ```

  For example:

  ```shell
  kubectl delete jobs boc-web-predict --namespace=dcdp
  ```



<br>

#### III. Distributed Tensorflow Job Usage

Need to update...



Distributed mode is similar to single except that two points:

1.  One is that you need to edit tf_cluster_template.yaml.jinja template file instead of tf_single_template.yaml.jinja template file.
2.  The other is that your training code file need to be written by target distributed style of tensorflow.



<br>

#### IV. Architecture

Kubernetes: 1.8.5
Tensorflow: 1.4.0
NFS
Python: 3.x
Jinja2
Docker
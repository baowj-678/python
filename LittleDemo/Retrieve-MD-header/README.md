# Github Markdown爬虫
## 简介
爬取github页面下所有markdown文件的**url和title**(h1标题)，并输出为markdown文档格式，例如：
~~~ markdown
* [DEMO - Speed Up Accessing Remote Files](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/accelerate_data_accessing.md)
* [DEMO - Speed Up Accessing HDFS Client Files](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/accelerate_data_accessing_by_hdfs.md)
* [Demo - Accelerate PVC with Fluid](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/accelerate_pvc.md)
* [DEMO - Speed Up Accessing Minio Files](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/accelerate_s3_minio.md)
* [Demo - How to ensure the completion of Fluid's serverless tasks](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/application_controller.md)
* [Demo - Using Fluid on ARM64 platform](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/arm64.md)
* [Demo - Set Dataset Access Mode](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/data_accessmodes.md)
* [DEMO - Cache Co-locality for Workload Scheduling](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/data_co_locality.md)
* [Demo - Data Preloading](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/data_warmup.md)
* [Demo - How to use Fuse NodeSelector](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/fuse_affinity.md)
* [Demo - Set FUSE clean policy](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/fuse_clean_policy.md)
* [Demo - How to enable FUSE auto-recovery](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/fuse_recover.md)
* [](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/gcs_configuration.md)
* [示例 - 使用Fluid加速主机目录](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/hostpath.md)
* [image pull secrets](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/image_pull_secrets.md)
* [DEMO - How to sync data of S3 using JuiceFS in Fluid](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/juicefs_for_s3.md)
* [DEMO - How to use JuiceFS in Fluid](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/juicefs_runtime.md)
* [Steps to build Juicefs open source environment](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/juicefs_setup.md)
* [DEMO - Accelerate Machine Learning Training with Fluid](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/machinelearning.md)
* [DEMO - Single-Machine Multiple-Dataset Speed Up Accessing Remote Files](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/multi_dataset_same_node_accessing.md)
* [Example - Using Fluid to access non-root user's data](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/nonroot_access.md)
* [](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/s3_configuration.md)
* [Demo - Alluxio Tieredstore Configuration](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/tieredstore_config.md)
* [DEMO - Use Secret to configure Dataset sensitive information](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/use_encryptoptions.md)
~~~

## 使用
命令行：
~~~ shell
python main.py [github-page-url]
~~~

## 示例
执行：
~~~ shell
python main.py https://github.com/fluid-cloudnative/fluid/tree/master/docs/en/samples
~~~

输出：
~~~ shell
❯ python main.py https://github.com/fluid-cloudnative/fluid/tree/master/docs/en/samples
got: 1/24
got: 2/24
got: 3/24
got: 4/24
got: 5/24
got: 6/24
got: 7/24
got: 8/24
got: 9/24
got: 10/24
got: 11/24
got: 12/24
url:https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/gcs_configuration.md has no head.
got: 13/24
got: 14/24
got: 15/24
got: 16/24
got: 17/24
got: 18/24
got: 19/24
got: 20/24
got: 21/24
url:https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/s3_configuration.md has no head.
got: 22/24
got: 23/24
got: 24/24
* [DEMO - Speed Up Accessing Remote Files](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/accelerate_data_accessing.md)
* [DEMO - Speed Up Accessing HDFS Client Files](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/accelerate_data_accessing_by_hdfs.md)
* [Demo - Accelerate PVC with Fluid](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/accelerate_pvc.md)
* [DEMO - Speed Up Accessing Minio Files](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/accelerate_s3_minio.md)
* [Demo - How to ensure the completion of Fluid's serverless tasks](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/application_controller.md)
* [Demo - Using Fluid on ARM64 platform](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/arm64.md)
* [Demo - Set Dataset Access Mode](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/data_accessmodes.md)
* [DEMO - Cache Co-locality for Workload Scheduling](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/data_co_locality.md)
* [Demo - Data Preloading](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/data_warmup.md)
* [Demo - How to use Fuse NodeSelector](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/fuse_affinity.md)
* [Demo - Set FUSE clean policy](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/fuse_clean_policy.md)
* [Demo - How to enable FUSE auto-recovery](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/fuse_recover.md)
* [](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/gcs_configuration.md)
* [示例 - 使用Fluid加速主机目录](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/hostpath.md)
* [image pull secrets](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/image_pull_secrets.md)
* [DEMO - How to sync data of S3 using JuiceFS in Fluid](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/juicefs_for_s3.md)
* [DEMO - How to use JuiceFS in Fluid](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/juicefs_runtime.md)
* [Steps to build Juicefs open source environment](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/juicefs_setup.md)
* [DEMO - Accelerate Machine Learning Training with Fluid](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/machinelearning.md)
* [DEMO - Single-Machine Multiple-Dataset Speed Up Accessing Remote Files](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/multi_dataset_same_node_accessing.md)
* [Example - Using Fluid to access non-root user's data](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/nonroot_access.md)
* [](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/s3_configuration.md)
* [Demo - Alluxio Tieredstore Configuration](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/tieredstore_config.md)
* [DEMO - Use Secret to configure Dataset sensitive information](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/samples/use_encryptoptions.md)
~~~
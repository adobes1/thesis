# Python Helm Chart

This repository contains a Helm chart for deploying Django web applications on OpenShift 4 cluster. This Chart also makes it possible to deploy a PostgreSQL database which will connect to your web application.
Aside from Django applications, it can also be used to deploy other Python applications.
As a demonstration of the capabilities of this Helm Chart, this repo also includes two sample django applcations - static hello world page and a dynamic library app using PostgreSQL.

## Repository Structure
```
.
├── django-apps
│   ├── hello-world-django
│   │   ├── manage.py
│   │   ├── pages
│   │   │   ├── ...
│   │   ├── project
│   │   │   ├── ...
│   │   └── requirements.txt
│   └── libraryproject
│       ├── library
│       │   └── ...
│       ├── libraryproject
│       │   ├── ...
│       ├── manage.py
│       └── requirements.txt
├── python-chart
|   ├── OWNERS
|   └── src
|       ├── Chart.yaml
|       ├── templates
|       │   ├── ...
|       │   └── tests
|       │       └── test.yaml
|       └── values.yaml
└── README.md
```

-   **`charts/`**: Contains the actual Helm chart for deploying Django-based applications
-   **`django-apps/`**: Contains two example Django applications (`hello-world-django` and `libraryproject`)

## Prerequisites

Before trying to install the Helm chart make sure you have the following prerequisites:
-   You are logged into an OCPv4 cluster
-   Helm installed

## Working with the Helm Chart

### Package the Helm Chart
To package the Helm chart run the following:
```
$ helm package python-chart/src
```
This will package the `python-chart` into a tarball (ending in `.tgz`)

### Installing the Helm Chart to cluster
To install the Helm chart to your cluster run the following:
```
$ helm install <release-name> <tarball-path>
```
However, you will probably want to override some of the default values set in values.yaml (meaning of these values is explained in the table below).
To install the helm package with your custom values you can run:
```
$ helm install <release-name> <tarball-path> -f <your-custom-values>
```
Where `<your-custom-values>` is a yaml file containing overrides for some (or all) of the values

Alternatively you can also use:
```
$ helm install <release-name> <tarball-path> --set key1=value1,key2=value2
```
Example:
```
$ helm install <release-name> <tarball-path> --set name=db.enabled=true,name=my-django-app
```
Both of these approaches can be combined in which case values set with `--set` will override those in your custom values yaml.

### Running Helm Tests
After you have deployed the chart, it is possible to run the tests included in the chart itself.

Helm offers a built-in testing feature that can validate the deployment once the resources are live. To run tests:
```
helm test <release-name>
```

### Uninstall the Helm Chart
To uninstall the Helm Chart, simply run
```
$ helm uninstall <release-name>
```

## Chart Values
Here's a table explaining each field in `values.yaml` file along with their default values:

| Parameter                     | Description                                                                                                    | Default Value         |
|-------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------|
| **app_file**                  | Path to your Python script. Leave empty if you want to use this chart with a Django application                | `''`                  |
| **app_config**                | Path to a Python file with valid Gunicorn configuration (if your project uses Gunicorn)                        | `''`                  |
| **application_domain**        | Domain name for the Django application. If not set, uses default cluster domain settings                       | `''`                  |
| **context_dir**               | Directory within the repository to use as the application context (should contain `manage.py` for Django apps) | `.`                   |
| **create_output_imagestream** | Specifies whether to create an ImageStream in your cluster where the application image will be pushed to       | `true`                |
| **app_imagestream**           | Name of the ImageStream to push your application image to if `create_output_imagestream` is `false`            | `''`                  |
| **db.enabled**                | Enables database support for the application                                                                   | `false`               |
| **db.deploy_new**             | Deploys a new database instance if set to `true`; otherwise, connects to an existing one                       | `false`               |
| **db.name**                   | Name of the database                                                                                           | `db`                  |
| **db.password**               | Password for the database user                                                                                 | `password`            |
| **db.host**                   | Host address for an external database (can be left empty if deploying a new database instance)                 | `''`                  |
| **db.service_name**           | Name used for the OpenShift database service and deployment                                                    | `postgresql`          |
| **db.user**                   | Username for the database                                                                                      | `user`                |
| **db.memory_limit**           | Memory limit for the database container                                                                        | `521Mi`               |
| **db.volume_capacity**        | Persistent volume capacity for the database                                                                    | `1Gi`                 |
| **django_secret_key**         | Secret key for Django applications                                                                             | `''`                  |
| **github_webhook_secret**     | Secret for GitHub webhooks for triggering builds                                                               | `fake-gh-secret`      |
| **memory_limit**              | Memory limit for the application container                                                                     | `512Mi`               |
| **name**                      | Name of the application (also used for various resources like BuildConfig and app Deployment)                  | `django-app`          |
| **namespace**                 | Namespace where Python and Postgresql imagestreams reside                                                      | `openshift`           |
| **pip_index_url**             | URL of custom PyPi repository index                                                                            | `''`                  |
| **postgresql_version**        | PostgreSQL version used when deploying a new database                                                          | `'15-el9'`            |
| **python_version**            | Python version to use for the application                                                                      | `3.9-ubi9`            |
| **source_repository_ref**     | Branch, tag, or commit to use from the source repository                                                       | `''`                  |
| **source_repository_url**     | URL of the application's source repository                                                                     | `''`                  |
| **port**                      | Port exposed by the application's service                                                                      | `8080`                |
| **target_port**               | Internal port within the application container to forward traffic to (the app listens on this port)            | `8080`                |


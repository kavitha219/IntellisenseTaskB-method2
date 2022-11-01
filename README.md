# IntellisenseTestB-method2
Accomplishing the test B by using a generic setup. 

This is a simple command line tool that provides a tabular output which includes the following details:
* Name of deployments
* Images of each deployment
* Date of deployment updated

We can run this application on docker or in our local machine with Windows.

### Pre - requisites:

 * Python 3.9 and all the dependencies
```
pip install -r requirements.txt
```
 * Kubectl installation, or a working kubeconfig file, by default this code will use the ~/.kube/config

### Commands :

for all namespaces:
```
python3 main.py
```

Specific namespace:
```
python3 main.py -n subsonic
```

Specific namespace & custom configfile:
```
python3 main.py -n subsonic -c kubeconfig
```

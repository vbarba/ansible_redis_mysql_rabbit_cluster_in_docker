# Introduction
This repository contains 3 ansible playbooks for deploying redis, mysql and rabbit clusters in docker containers.

All the logic is has been implemented in the ansible files and therefore the docker containers image only contains a minimal ubuntu systemd sandbox.

Each playbook run the docker containers with the parameters needed for persist data in `/mnt` directory inside docker host. 

A Vagrant file is provided in order to test the playbooks in a VM with docker installed.

## Redis playbook
This playbook run 6 containers (3 master and 3 slave nodes) and uses the ansible galaxy role `idealista.redis_role` for install a redis cluster.
### Usage
The following command will boot a VM with docker inside and launch the redis playbook.
```
vagrant up --provision-with docker,redis
```
### Test
You can run the following commands to check the cluster status:
```
vagrant ssh -c "docker exec redis-1 redis-cli cluster nodes"
vagrant ssh -c "docker exec redis-1 redis-cli cluster info"
```
In order to check de data persistence in docker host you can insert data, remove the containers and re-launch the containers again. At the end you can check that the data is still available in the clusterr.
```
vagrant ssh -c "docker exec redis-3 redis-cli set foo bar"
vagrant ssh -c "docker rm -f redis-1 redis-2 redis-3 redis-4 redis-5 redis-6"
vagrant provision --provision-with redis
vagrant ssh -c "docker exec redis-4 redis-cli get foo"
``` 
### Clean
Run the following command for stop the VM
```
vagrant destroy
```
## MySQL playbook
This playbook run 2 containers (1 master and 1 slave) and uses the ansible galaxy role `geerlingguy.mysql`for install the mysql servers.
### Usage
The following command will boot a VM with docker inside and launch the mysql playbook.
```
vagrant up --provision-with docker,mysql
```
### Test
You can run the following command to check the replication:
````
vagrant ssh -c "docker exec mysql-slave mysql -e 'show slave status\G'"
````

And you can check the following commands to check the data persistence. This will create a database, a table and insert data on the table. Then the docker containers are removed and re-launch. You can query again the data and check that still exist on the cluster.
```
vagrant ssh -c "docker exec mysql-master mysql -e 'create database dummy'"
vagrant ssh -c "docker exec mysql-master mysql --database dummy -e 'CREATE TABLE t (c CHAR(20) CHARACTER SET utf8 COLLATE utf8_bin)'"
vagrant ssh -c "docker exec mysql-master mysql --database dummy -e 'insert into t(c) values (\"hello\")'"
vagrant ssh -c "docker exec mysql-slave mysql --database dummy -e 'select * from t'"
vagrant ssh -c "docker rm -f mysql-master mysql-slave"
vagrant provision --provision-with mysql
vagrant ssh -c "docker exec mysql-slave mysql --database dummy -e 'select * from t'"
```
### Clean
Run the following command for stop the VM
```
vagrant destroy
```
## RabbitMQ playbook
This playbook run 3 containers and uses the ansible galaxy role `marcobellaccini.ansible-rabbitmq-minimalistic` install the rabbitmq cluster.
The role has been changed to avoid reset the data on every run. 
### Usage
The following command will boot a VM with docker inside and launch the mysql playbook.
```
vagrant up --provision-with docker,rabbitmq
```
### Test
You can run the following command to check the cluster status:
```
vagrant ssh -c "docker exec rabbitmq-1 rabbitmqctl cluster_status"
```
### Clean
Run the following command for stop the VM
```
vagrant destroy
```
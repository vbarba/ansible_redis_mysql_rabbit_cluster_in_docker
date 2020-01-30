ansible-rabbitmq-minimalistic
=============================
[![Build Status](https://travis-ci.org/marcobellaccini/ansible-rabbitmq-minimalistic.svg?branch=master)](https://travis-ci.org/marcobellaccini/ansible-rabbitmq-minimalistic)

Minimalistic, yet powerful and clustering-enabled RabbitMQ Ansible role.

Written for Debian 10 (may work on other versions and distributions too - in case, please let me know).

Role Variables
--------------
Apart from role defaults (for which you can refer to
[this file](https://github.com/marcobellaccini/ansible-rabbitmq-minimalistic/blob/master/defaults/main.yml)),
you'll probably want to deploy your custom *rabbitmq.conf* file to the servers.

You can make the role generate and deploy your *rabbitmq.conf* file by defining the *rabbitmq_conf_template* variable:

    rabbitmq_conf_template: "path/to/rabbitmq.conf.j2"

The path is relative to the playbook directory.

In this way, you can also deploy a RabbitMQ cluster just by leveraging the
[cluster_formation.classic_config.nodes](https://www.rabbitmq.com/configure.html#config-items) server variable in *rabbitmq.conf*.

For example, you can use a *rabbitmq.conf.j2* template like this:

    {% for host in ansible_play_hosts_all %}
    cluster_formation.classic_config.nodes.{{ loop.index }} = rabbit@{{ hostvars[host]['inventory_hostname'] }}
    {% endfor %}

In order to enable clustering, you will have to setup the hosts with the same [erlang cookie](https://www.rabbitmq.com/clustering.html#erlang-cookie).

For this, you can use the *rabbitmq_erlang_cookie* variable (please consider using
[Ansible Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html) to encrypt the cookie).

When clustering, you will also have to set *serial: 1* in your playbook (otherwise nodes may experience problems when trying to form the cluster).

You can also enable RabbitMQ plugins by simply specifying and deploying a
RabbitMQ [enabled_plugins file](https://www.rabbitmq.com/plugins.html#ways-to-enable-plugins) from a template:

    rabbitmq_enabled_plugins_template: "path/to/enabled_plugins.j2"

Again, the path is relative to the playbook directory.

For other variables, see [Role Defaults](https://github.com/marcobellaccini/ansible-rabbitmq-minimalistic/blob/master/defaults/main.yml).

This role aims to be minimalistic: in order to perform advanced configurations, you can use
[Ansible RabbitMQ Modules](https://docs.ansible.com/ansible/latest/modules/list_of_messaging_modules.html).

Example Playbook
----------------

    - hosts: msgservers
      serial: 1  # this is required only if you deploy a RabbitMQ cluster
      roles:
         - ansible-rabbitmq-minimalistic
      vars:
        rabbitmq_conf_template: "my_rabbit_conf/rabbitmq.conf.j2"  # this is optional
        rabbitmq_enabled_plugins_template: "my_rabbit_conf/enabled_plugins.j2"  # this is optional
        rabbitmq_erlang_cookie: "XXXXXXXXXXXXXXXXXXXX"  # Required for clustering. NOTE: this is just an example: please use Ansible Vault!

License
-------

Apache License 2.0

Author Information
------------------

Marco Bellaccini - marco.bellaccini[at!]gmail.com

[https://github.com/marcobellaccini](https://github.com/marcobellaccini)

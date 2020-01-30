import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rmq_conf_file(host):
    conf_file = host.file('/etc/rabbitmq/rabbitmq.conf')

    assert conf_file.exists

Vagrant.configure("2") do |config|
  config.vm.box = "elegoev/ubuntu-18.04-docker"
  config.vm.provider "virtualbox" do |v|
    v.memory = 4096
    v.cpus = 4
  end
  config.vm.provision  "docker", type:"ansible_local" do |ansible|
    ansible.playbook = "docker.yml"
    ansible.extra_vars = { ansible_python_interpreter:"auto" }
  end
  config.vm.provision  "redis", type:"ansible_local" do |ansible|
    ansible.playbook = "redis.yml"
    ansible.limit = "all"
    ansible.extra_vars = { ansible_python_interpreter:"auto" }
    ansible.galaxy_role_file = "requirements-redis.yml"
  end
  config.vm.provision  "mysql", type:"ansible_local" do |ansible|
    ansible.playbook = "mysql.yml"
    ansible.limit = "all"
    ansible.extra_vars = { ansible_python_interpreter:"auto" }
    ansible.galaxy_role_file = "requirements-mysql.yml"
  end
  config.vm.provision  "rabbitmq", type:"ansible_local" do |ansible|
    ansible.playbook = "rabbitmq.yml"
    ansible.limit = "all"
    ansible.extra_vars = { ansible_python_interpreter:"auto" }
  end
end


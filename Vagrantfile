require 'yaml'

net = YAML.load_file('network.yml')
VAGRANTFILE_API_VERSION = 2

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    # -------- GLOBAL CONFIGURATION --------
    
    # Provider configuration
    config.vm.provider "docker" do |container|
        container.create_args = ['--cpuset-cpus=2']
        container.create_args = ['--memory=2g']
        container.remains_running = true
        container.has_ssh = true
    end

    # Provisionner configuration
    config.vm.provision "ansible" do |ansible|
        ansible.verbose = "v"
        ansible.playbook = "playbooks/setup.yml"
    end

    config.vm.synced_folder '.', '/vagrant', disabled: true

    # -------- CONTAINERS DEFINITION --------

    config.vm.define "drone" do |config|
        config.vm.network "private_network", ip: net['drone']['eth1'], netmask: 24
        config.vm.network "private_network", ip: net['drone']['eth2'], netmask: 24
        config.vm.network "private_network", ip: net['drone']['eth3'], netmask: 24
        config.vm.network "private_network", ip: net['drone']['eth4'], netmask: 24
        config.vm.network "private_network", ip: net['drone']['eth5'], netmask: 24
        config.vm.provider "docker" do |d|
            d.name = "drone"
            d.image = "vagrant-ubuntu-22.04"
            d.create_args = ["--hostname", "drone", "--cap-add=NET_ADMIN"]
            d.env = {"INFLUXDB_IP" => net['influxdb']['eth1']}
        end
    end

    config.vm.define "router" do |config|
        config.vm.network "private_network", ip: net['router']['eth1'], netmask: 24
        config.vm.network "private_network", ip: net['router']['eth2'], netmask: 24
        config.vm.network "private_network", ip: net['router']['eth3'], netmask: 24
        config.vm.network "private_network", ip: net['router']['eth4'], netmask: 24
        config.vm.network "private_network", ip: net['router']['eth5'], netmask: 24
        config.vm.network "private_network", ip: net['router']['eth6'], netmask: 24
        config.vm.provider "docker" do |d|
            d.name = "router"
            d.image = "vagrant-ubuntu-22.04"
            d.create_args = ["--hostname", "router", "--cap-add=NET_ADMIN"]
            d.env = {"INFLUXDB_IP" => net['influxdb']['eth1']}
        end
    end

    config.vm.define "server" do |config|
        config.vm.network "private_network", ip: net['server']['eth1'], netmask: 24
        config.vm.network "private_network", ip: net['server']['eth2'], netmask: 24
        config.vm.provider "docker" do |d|
            d.name = "server"
            d.image = "vagrant-ubuntu-22.04"
            d.create_args = ["--hostname", "server", "--cap-add=NET_ADMIN"]
            d.env = {"INFLUXDB_IP" => net['influxdb']['eth1']}
        end
    end

    # -------- MONITORING --------

    config.vm.define "influxdb" do |config|
        config.vm.network "forwarded_port", host: net['influxdb']['host_port'], guest: net['influxdb']['guest_port']
        config.vm.network "private_network", ip: net['influxdb']['eth1'], netmask: 24
        config.vm.provider "docker" do |d|
            d.name = "influxdb"
            d.build_dir = "./docker/influxdb"
            d.build_args = ["--tag", "influxdb"]
            d.create_args = ["--hostname", "influxdb"]
            d.env = {"INFLUXDB_IP" => net['influxdb']['eth1']}
            d.has_ssh = false
        end
    end

    config.vm.define "grafana" do |config|
        config.vm.network "forwarded_port", host: net['grafana']['host_port'], guest: net['grafana']['guest_port']
        config.vm.network "private_network", ip: net['grafana']['eth1'], netmask: 24
        config.vm.provider "docker" do |d|
            d.name = "grafana"
            d.build_dir = "./docker/grafana"
            d.build_args = ["--tag", "grafana"]
            d.create_args = ["--hostname", "grafana"]
            d.env = {"INFLUXDB_IP" => net['influxdb']['eth1']}
            d.has_ssh = false
        end
    end

end
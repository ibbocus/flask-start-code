# Install required plugins
required_plugins = ["vagrant-hostsupdater"]
required_plugins.each do |plugin|
    exec "vagrant plugin install #{plugin}" unless Vagrant.has_plugin? plugin
end

Vagrant.configure("2") do |config|


  config.vm.define "app" do |app|
    app.vm.box = "bento/ubuntu-20.04"
    app.vm.network "private_network", ip: "192.168.10.100"
    app.hostsupdater.aliases = ["flask.local"]
    app.vm.synced_folder "app", "/home/ubuntu/app"
    app.vm.provision "shell", path: "environment/provisions.sh", privileged: false
  end

end

# Puppet command for prepare the servers
exec { 'Sys update':
  command  => 'sudo apt-get -y update',
  provider => shell
}
exec { 'Install NGINX':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
  require  => Exec['Sys update']
}
exec { 'Create path':
  command  => 'sudo mkdir -p /data/web_static/shared/',
  provider => shell,
  require  => Exec['Install NGINX']
}
exec { 'test path':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => shell,
  require  => Exec['Create path']
}
exec { 'HTML file':
  command  => 'echo "FakeHTML" | sudo tee /data/web_static/releases/test/index.html',
  provider => shell,
  require  => Exec['test path'],
  returns  => [0, 1]
}
exec { 'Sym link':
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
  require  => Exec['HTML file']
}
exec { 'Permissions':
  command  => 'sudo chown -R ubuntu:ubuntu /data/',
  provider => shell,
  require  => Exec['Sym link']
}
exec { 'create location':
  command  => 'sudo sed -i "29i\\\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default',
  provider => shell,
  require  => Exec['Permissions']
}
exec { 'Restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
  require  => Exec['create location']
}

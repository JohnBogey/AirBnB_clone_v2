#installs nginx if not there
package { 'nginx':
}

#nginx get through firewall port 80
exec { 'ufw':
  command => 'sudo ufw allow \'Nginx HTTP\'',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
}

#create proj dirs tree
$proj_dirs = [ '/data/', '/data/web_static/',
              '/data/web_static/shared/',
              '/data/web_static/releases/',
              '/data/web_static/releases/test/' ]
file { $proj_dirs:
    ensure => 'directory',
  }

#create test index.html
$index="<html>
  <head>
  </head>
  <body>
     Holberton School
  </body>
</html>"
file { '/data/web_static/releases/test/index.html':
    content => $index,
}

#create sym link
file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test/',
    force  => true,
  }

#execs chown
exec { 'chown -R ubuntu:ubuntu /data/':
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
}

#execs sed thing
$location='location /hbnb_static/ { alias /data/web_static/current/; autoindex off; }'
exec { 'sed':
  command => 'sudo sed -i "/listen \[::\]:80 default_server;/a $location" /etc/nginx/sites-enabled/default',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
}

#execs nginx restart to load changes
exec { 'sudo service nginx restart':
  path => '/usr/sbin/service',
}

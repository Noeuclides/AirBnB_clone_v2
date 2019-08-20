#create a file in /tmp
file { '/tmp/holberton':
  ensure  => 'present',
  replace => 'no',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  mode    => '0744',
} }

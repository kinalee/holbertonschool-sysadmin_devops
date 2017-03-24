# Using Puppet, create a file
file { 'holberton':
     path => '/tmp/'
     mode => 0744,
     owner => 'www-data',
     group => 'www-data',
     content => 'I love Puppet',
}

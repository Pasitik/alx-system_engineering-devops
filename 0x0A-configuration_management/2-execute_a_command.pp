# killing a process(cmd execution)

exec{ 'pkill':
  command => '/usr/bin/pkill -f "killmenow"',
  path    => '/usr/bin',
}


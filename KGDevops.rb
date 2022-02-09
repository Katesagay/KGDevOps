package 'httpd' do
    action :install
end

service 'httpd' do
    action [:enable, :start]
end

file '/etc/motd' do
    owner 'root'
    group 'root'
    mode '0644'
    content 'Hello world'
    action :create
end

user 'kate.sagay' do
    comment  'creates a user'
    uid 1234
    gid 'groupUnixname'
    home '/home/UnixUsers'
    shell '/bin/bash'
end

cron 'noop' do
    hour '5'
    minute '45'
    command 'echo "Hello world!"'
end

timezone "Set the host's timezone to Europe/London" do
    timezone 'Europe/London'
end  


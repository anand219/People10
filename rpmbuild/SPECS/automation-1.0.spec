Name:           automation-1.0
Version:        1
Release:        1%{?dist}
Summary:        Test

License:        GPS
URL:            https://github.com
Source0:        automation-1.0.tar.gz

BuildRequires:  Apache
Requires:       Apache

%description    


%prep
yum -y install redhat-lsb-core
sudo mkdir -p /var/www/html/operations var/www/html/website

#!/bin/bash
if [ "`lsb_release -is`" == "Ubuntu" ] || [ "`lsb_release -is`" == "Debian" ]
then
    sudo apt-get -y install apache2; 
    sudo chmod 755 -R /var/www/;
    sudo service apache2 restart;

elif [ "`lsb_release -is`" == "CentOS" ] || [ "`lsb_release -is`" == "RedHat" ]
then
    sudo yum -y install httpd;
    sudo service httpd restart;
    sudo chkconfig httpd on;

else
    echo "Unsupported Operating System";
fi
%setup -q


%build
%configure
make %{?_smp_mflags}


%_install

rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc



%changelog

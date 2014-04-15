Name:          xdmod
Version:       3.5.0
Release:       1%{?dist}
Summary:       Data warehouse and web portal for mining statistical data from resource managers
URL:           http://xdmod.sourceforge.net/
Group:         Applications/Internet
License:       LGPLv3+
Source:        %{name}-%{version}.tar.gz
BuildRoot:     %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:     noarch
BuildRequires: php-cli
Requires:      httpd
#Requires:      mysql >= 5.1
Requires:
Requires:      php >= 5.3 php-cli php-mysql php-pdo
Requires:      php-pear-Log php-pear-MDB2 php-pear-MDB2-Driver-mysql
Requires:      java-1.7.0-openjdk java-1.7.0-openjdk-devel
Requires:      cronie
Requires:      logrotate
Requires:      php-Zendframework

%description
XDMoD is a data warehouse and web portal for mining statistical data
from resource managers in high-performance computing environments.
XDMoD presents resource utilization over set time periods and provides
detailed interactive charts, graphs, and tables.

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT ./install \
    --quiet \
    --bindir=%{_bindir} \
    --libdir=%{_libdir}/%{name} \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --datadir=%{_datadir}/%{name} \
    --docdir=%{_docdir}/%{name}-%{version} \
    --logdir=%{_localstatedir}/log/%{name} \
    --httpdconfdir=%{_sysconfdir}/httpd/conf.d \
    --logrotatedconfdir=%{_sysconfdir}/logrotate.d \
    --crondconfdir=%{_sysconfdir}/cron.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}-*
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_docdir}/%{name}-%{version}/

%attr(0775,root,apache) %dir %{_localstatedir}/log/%{name}

%config(noreplace) %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/cron.d/%{name}

%changelog
* Mon Nov 18 2013 Jeffrey T. Palmer <jtpalmer@ccr.buffalo.edu> 3.5.0-1
- Initial public release

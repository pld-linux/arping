
Summary:	ARPing
Summary(pl):	ARPing
Name:		arping
Version:	2.04
Release:	0.1
License:	GPL
Group:		Networking/Admin
Source0:	ftp://ftp.habets.pp.se/pub/synscan/%{name}-%{version}.tar.gz
# Source0-md5:	5fbf10272dcb5040cbfb4d540179fb99
BuildRequires:	linux-libc-headers
BuildRequires:	libnet-devel
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
- arping Ping <address> on device <interface> by ARP packets, using
  source address <source>,

%description -l pl
- arping Pinguje <adres> na interfejsie <interfejs> wysy³aj±c pakiety
  ARP,

%prep
%setup -q

%build

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_sbindir}
install -d -m 755 $RPM_BUILD_ROOT%{_usr}/doc
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man8
install -c arping $RPM_BUILD_ROOT%{_sbindir}/arping
install -c arping $RPM_BUILD_ROOT%{_sbindir}/arping-scan-net.sh
install -c README $RPM_BUILD_ROOT%{_usr}/doc/README
install -c arping.8 $RPM_BUILD_ROOT%{_mandir}/man8/arping.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(4754,root,adm) %{_sbindir}/arping
%attr(754,root,adm) %{_sbindir}/arping-scan-net.sh
%{_mandir}/man8/arping.8*
%doc %{_usr}/doc/*

Summary:	ARPing - ping an address by ARP packets
Summary(pl.UTF-8):	ARPing - pingowanie adresów pakietami ARP
Name:		arping
Version:	2.12
Release:	2
License:	GPL v2
Group:		Networking/Admin
Source0:	http://www.habets.pp.se/synscan/files/%{name}-%{version}.tar.gz
# Source0-md5:	47e0db7fed9f1297c598a24cd476911d
URL:		http://www.habets.pp.se/synscan/programs.php?prog=arping
BuildRequires:	libnet-devel > 1.1
BuildRequires:	libpcap-devel
BuildRequires:	sed >= 4.0
Requires:	bc
Obsoletes:	iputils-arping
Conflicts:	iputils <= 1:ss021109-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
arping pings given address on given device by ARP packets, using given
source address.

%description -l pl.UTF-8
arping pinguje podany adres na podanym interfejsie wysyłając pakiety
ARP.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install extra/arping-scan-net.sh \
	$RPM_BUILD_ROOT%{_sbindir}/arping-scan-net.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(4754,root,adm) %{_sbindir}/arping
%attr(754,root,adm) %{_sbindir}/arping-scan-net.sh
%{_mandir}/man8/arping.8*

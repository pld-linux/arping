# TODO: optflags
Summary:	ARPing - ping an address by ARP packets
Summary(pl):	ARPing - pingowanie adres�w pakietami ARP
Name:		arping
Version:	2.05
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	ftp://ftp.habets.pp.se/pub/synscan/%{name}-%{version}.tar.gz
# Source0-md5:	96e7c2ce8ae09046e264a314eeaac4dd
URL:		http://www.habets.pp.se/synscan/programs.php?prog=arping
BuildRequires:	libnet-devel
BuildRequires:	libpcap-devel
BuildRequires:	sed >= 4.0
Provides:	arping
Obsoletes:	arping
Obsoletes:	iputils-arping
Conflicts:	iputils <= 1:ss021109-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
arping pings given address on given device by ARP packets, using given
source address.

%description -l pl
arping pinguje podany adres na podanym interfejsie wysy�aj�c pakiety
ARP.

%prep
%setup -q
sed '/CC.*arping-2/s/-g/$(CFLAGS)/' \
	-i Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install arping $RPM_BUILD_ROOT%{_sbindir}/arping
install arping-scan-net.sh \
	$RPM_BUILD_ROOT%{_sbindir}/arping-scan-net.sh
install arping.8 $RPM_BUILD_ROOT%{_mandir}/man8/arping.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(4754,root,adm) %{_sbindir}/arping
%attr(754,root,adm) %{_sbindir}/arping-scan-net.sh
%{_mandir}/man8/arping.8*

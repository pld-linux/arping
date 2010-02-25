Summary:	ARPing - ping an address by ARP packets
Summary(pl.UTF-8):	ARPing - pingowanie adresów pakietami ARP
Name:		arping
Version:	2.08
Release:	2
License:	GPL v2
Group:		Networking/Admin
Source0:	ftp://ftp.habets.pp.se/pub/synscan/%{name}-%{version}.tar.gz
# Source0-md5:	36dba82f8a6084b634aa6f4aac6225c6
URL:		http://www.habets.pp.se/synscan/programs.php?prog=arping
BuildRequires:	libnet-devel
BuildRequires:	libpcap-devel
BuildRequires:	sed >= 4.0
Requires:	bc
Provides:	arping
Obsoletes:	arping
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

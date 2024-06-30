Summary:	ARPing - ping an address by ARP packets
Summary(pl.UTF-8):	ARPing - pingowanie adresów pakietami ARP
Name:		arping
Version:	2.25
Release:	1
License:	GPL v2
Group:		Networking/Admin
Source0:	https://www.habets.pp.se/synscan/files/%{name}-%{version}.tar.gz
# Source0-md5:	af8a72c8d83bc9b3b0979475b084ed24
Patch0:		%{name}-nolibs.patch
URL:		https://www.habets.pp.se/synscan/programs_arping.html
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	libcap-devel
BuildRequires:	libnet-devel > 1.1
BuildRequires:	libpcap-devel
BuildRequires:	libseccomp-devel
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
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p extra/arping-scan-net.sh \
	$RPM_BUILD_ROOT%{_sbindir}/arping-scan-net.sh

# interfaces not accessible in binary package
%{__rm} $RPM_BUILD_ROOT%{_includedir}/arping.h

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(4754,root,adm) %{_sbindir}/arping
%attr(754,root,adm) %{_sbindir}/arping-scan-net.sh
%{_mandir}/man8/arping.8*

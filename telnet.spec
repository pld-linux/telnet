Summary:	Client for the telnet remote login protocol
Summary(de):	Client für das entfernte Login-Protokoll 'telnet'
Summary(fr):	Client pour le protocole de connexion telnet
Summary(pl):	Klient protoko³u telnet
Summary(tr):	Telnet uzak baðlantý protokolü için istemci ve sunucu
Name:		telnet
Version:	0.17
Release:	12
Group:		Networking
Group(de):	Netzwerkwesen
Group(es):	Red
Group(pl):	Sieciowe
Group(pt_BR):	Rede
License:	BSD
Source0:	ftp://ftp.linux.org.uk/pub/linux/Networking/netkit/netkit-%{name}-%{version}.tar.gz
Source1:	%{name}d.inetd
Source2:	%{name}.desktop
Patch0:		netkit-%{name}-ipv6.patch
Patch1:		netkit-%{name}-fixes.patch
Patch2:		netkit-%{name}-ayt.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Telnet is a popular protocol for remote logins across the Internet.
This package provides a command line telnet client.

%description -l de
Telnet ist ein beliebtes Protokoll für entfernte Logins über das
Internet. Dieses Paket enthält einen Befehlszeilen-Telnet-Client.

%description -l fr
telnet est un protocole très utilisé pour les logins distants sur
l'Internet. Ce paquetage offre un client telnet

%description -l pl
Telnet jest popularnym protoko³em umo¿liwiaj±cym logowanie siê na
zdalnym komputerze w sieci internet i 6bone. Pakiet zawiera klienta
us³ugi telnet.

%description -l tr
Telnet, Internet üzerinden uzak kullanýcý baðlantýlarý için popüler
bir protokoldur. Bu paket, bir komut satýrý istemcisi ile birlikte bir
sunucu süreci içerir. Sunucu sürecin çalýþtýðý makinaya uzak
kullanýcýlarýn baðlanabilir.

%package -n telnetd
Summary:	Server for the telnet remote login protocol
Summary(de):	Server für das entfernte Login-Protokoll 'telnet'  
Summary(fr):	Serveur pour le protocole de connexion distante telnet
Summary(pl):	Serwer us³ugi telnet
Summary(tr):	Telnet uzak baðlantý protokolü için istemci ve sunucu
Group:		Networking
Group(de):	Netzwerkwesen
Group(es):	Red
Group(pl):	Sieciowe
Group(pt_BR):	Rede
Requires:	inetdaemon
Requires:	login
Prereq:		rc-inetd >= 0.8
Obsoletes:	telnet-server

%description -n telnetd
Telnet is a popular protocol for remote logins across the Internet.
This package provides telnet daemon which allows remote logins into
the machine it is running on.

%description -l de -n telnetd
Telnet ist ein beliebtes Protokoll für entfernte Logins über das
Internet. Dieses Paket enthält einen Telnet-Dämon, der entfernte
Logins auf dem Rechner, auf dem er läuft, zuläßt. Der Telnet- Dämon
ist standardmäßig aktiviert.

%description -l fr -n telnetd
telnet est un protocole très utilisé pour les logins distants sur
l'Internet. Ce paquetage offre démon telnet permettant des logins
distants sur la machine sur laquelle il tourne.

%description -l tr -n telnetd
Telnet, Internet üzerinden uzak kullanýcý baðlantýlarý için popüler
bir protokoldur. Bu paket, bir komut satýrý istemcisi ile birlikte bir
sunucu süreci içerir. Sunucu sürecin çalýþtýðý makinaya uzak
kullanýcýlarýn baðlanabilir.

%description -l pl -n telnetd
Telnet jest popularnym protoko³em umo¿liwiaj±cym logowanie siê na
zdalnym komputerze w sieci internet i 6bone. Pakiet zawiera serwer
us³ugi telnet.

%prep
%setup -q -n netkit-%{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# don't use configure macro
CC=gcc
CFLAGS="%{rpmcflags} -DINET6" \
./configure \
	--with-c-compiler=gcc \
	--prefix=%{_prefix}

%{__make} OPT="%{rpmcflags} -D__USE_UNIX98"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,5,8}} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Network,/etc/sysconfig/rc-inetd}

%{__make} INSTALLROOT=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/telnetd
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Network

rm -f 	$RPM_BUILD_ROOT%{_mandir}/man8/*
install telnetd/*.8 $RPM_BUILD_ROOT%{_mandir}/man8

rm -f $RPM_BUILD_ROOT%{_sbindir}/*
install telnetd/telnetd $RPM_BUILD_ROOT%{_sbindir}

gzip -9nf BUGS README

%clean
rm -rf $RPM_BUILD_ROOT

%post -n telnetd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%postun -n telnetd
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/rc-inetd ]; then
		/etc/rc.d/init.d/rc-inetd reload 1>&2
	fi
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/telnet.desktop
%{_mandir}/man1/*

%files -n telnetd
%defattr(644,root,root,755)
%doc {BUGS,README}.gz
%attr(640,root,root) %config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/rc-inetd/telnetd

%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[58]/*

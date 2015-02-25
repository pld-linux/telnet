Summary:	Client for the telnet remote login protocol
Summary(de.UTF-8):	Client für das entfernte Login-Protokoll 'telnet'
Summary(es.UTF-8):	Cliente para el protocolo telnet de login remoto
Summary(fr.UTF-8):	Client pour le protocole de connexion telnet
Summary(pl.UTF-8):	Klient protokołu telnet
Summary(pt_BR.UTF-8):	Cliente para o protocolo telnet de login remoto
Summary(tr.UTF-8):	Telnet uzak bağlantı protokolü için istemci ve sunucu
Name:		telnet
Version:	0.17
Release:	34
License:	BSD
Group:		Networking/Utilities
Source0:	ftp://ftp.linux.org.uk/pub/linux/Networking/netkit/netkit-%{name}-%{version}.tar.gz
# Source0-md5:	d6beabaaf53fe6e382c42ce3faa05a36
Source1:	%{name}d.inetd
Source2:	%{name}.desktop
Source3:	%{name}.png
Source4:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source4-md5:	a1e67907c855b6f596321f2cc8318e1a
Patch0:		netkit-%{name}-ipv6.patch
Patch1:		netkit-%{name}-fixes.patch
Patch2:		netkit-%{name}-ayt.patch
Patch3:		netkit-%{name}-issue.patch
Patch4:		netkit-%{name}-cpp.patch
Patch5:		netkit-%{name}-pld_man.patch
Patch6:		netkit-%{name}-tinfo.patch
Patch7:		netkit-%{name}-format-security.patch
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	rpmbuild(macros) >= 1.268
Obsoletes:	heimdal-telnet
Obsoletes:	inetutils-telnet
Obsoletes:	krb5-telnet
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Telnet is a popular protocol for remote logins across the Internet.
This package provides a command line telnet client.

%description -l de.UTF-8
Telnet ist ein beliebtes Protokoll für entfernte Logins über das
Internet. Dieses Paket enthält einen Befehlszeilen-Telnet-Client.

%description -l es.UTF-8
Telnet es un protocolo popular para logins remotos a través de la
Internet. Este paquete ofrece un cliente telnet en la línea de
comando.

%description -l fr.UTF-8
telnet est un protocole très utilisé pour les logins distants sur
l'Internet. Ce paquetage offre un client telnet

%description -l pl.UTF-8
Telnet jest popularnym protokołem umożliwiającym logowanie się na
zdalnym komputerze w sieci Internet i 6bone. Pakiet zawiera klienta
usługi telnet.

%description -l pt_BR.UTF-8
O telnet é um protocolo popular para logins remotos através da
Internet. Este pacote fornece um cliente telnet na linha de comando.

%description -l tr.UTF-8
Telnet, Internet üzerinden uzak kullanıcı bağlantıları için popüler
bir protokoldur. Bu paket, bir komut satırı istemcisi ile birlikte bir
sunucu süreci içerir. Sunucu sürecin çalıştığı makinaya uzak
kullanıcıların bağlanabilir.

%package -n telnetd
Summary:	Server for the telnet remote login protocol
Summary(de.UTF-8):	Server für das entfernte Login-Protokoll 'telnet'
Summary(es.UTF-8):	Servidor para el protocolo telnet de login remoto
Summary(fr.UTF-8):	Serveur pour le protocole de connexion distante telnet
Summary(pl.UTF-8):	Serwer usługi telnet
Summary(pt_BR.UTF-8):	Servidor para o protocolo telnet de login remoto
Summary(tr.UTF-8):	Telnet uzak bağlantı protokolü için istemci ve sunucu
Group:		Networking
Requires:	inetdaemon
Requires:	login
Requires:	rc-inetd >= 0.8
Obsoletes:	inetutils-telnetd
Obsoletes:	telnet-server

%description -n telnetd
Telnet is a popular protocol for remote logins across the Internet.
This package provides telnet daemon which allows remote logins into
the machine it is running on.

%description -n telnetd -l de.UTF-8
Telnet ist ein beliebtes Protokoll für entfernte Logins über das
Internet. Dieses Paket enthält einen Telnet-Dämon, der entfernte
Logins auf dem Rechner, auf dem er läuft, zuläßt. Der Telnet- Dämon
ist standardmäßig aktiviert.

%description -n telnetd -l es.UTF-8
Telnet es un protocolo popular para logins remotos a través de la
Internet. Este paquete ofrece un servidor telnet que permite login
remoto dentro de la máquina en que se está ejecutando. editándose
/etc/inetd.conf.

%description -n telnetd -l fr.UTF-8
telnet est un protocole très utilisé pour les logins distants sur
l'Internet. Ce paquetage offre démon telnet permettant des logins
distants sur la machine sur laquelle il tourne.

%description -n telnetd -l pl.UTF-8
Telnet jest popularnym protokołem umożliwiającym logowanie się na
zdalnym komputerze w sieci Internet i 6bone. Pakiet zawiera serwer
usługi telnet.

%description -n telnetd -l pt_BR.UTF-8
O telnet é um protocolo popular para logins remotos através da
Internet. Este pacote fornece um servidor telnet que permite login
remoto dentro da máquina em que ele está rodando.

%description -n telnetd -l tr.UTF-8
Telnet, Internet üzerinden uzak kullanıcı bağlantıları için popüler
bir protokoldur. Bu paket, bir komut satırı istemcisi ile birlikte bir
sunucu süreci içerir. Sunucu sürecin çalıştığı makinaya uzak
kullanıcıların bağlanabilir.

%prep
%setup -q -n netkit-%{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
# don't use configure macro
CFLAGS="%{rpmcflags} -DINET6" \
CXXFLAGS="%{rpmcflags} -DINET6" \
LDFLAGS="%{rpmldflags}" \
./configure \
	--with-c-compiler="%{__cc}" \
	--with-c++-compiler="%{__cxx}" \
	--prefix=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,5,8}} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT/etc/sysconfig/rc-inetd

%{__make} install \
	INSTALLROOT=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/telnetd
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

rm -f 	$RPM_BUILD_ROOT%{_mandir}/man8/*
install telnetd/*.8 $RPM_BUILD_ROOT%{_mandir}/man8

rm -f $RPM_BUILD_ROOT%{_sbindir}/*
install telnetd/telnetd $RPM_BUILD_ROOT%{_sbindir}

bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
rm -f $RPM_BUILD_ROOT%{_mandir}/*/*/*.old

%clean
rm -rf $RPM_BUILD_ROOT

%post -n telnetd
%service -q rc-inetd reload

%postun -n telnetd
if [ "$1" = "0" ]; then
	%service -q rc-inetd reload
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/telnet.desktop
%{_pixmapsdir}/telnet.png
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(ko) %{_mandir}/ko/man1/*

%files -n telnetd
%defattr(644,root,root,755)
%doc BUGS README
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/telnetd
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[58]/*
%lang(es) %{_mandir}/es/man[58]/*
%lang(fr) %{_mandir}/fr/man[58]/*
%lang(ja) %{_mandir}/ja/man[58]/*
%lang(ko) %{_mandir}/ko/man[58]/*
%lang(pl) %{_mandir}/pl/man[58]/*

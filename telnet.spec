Summary:	Client for the telnet remote login protocol
Summary(de):	Client f�r das entfernte Login-Protokoll 'telnet'
Summary(es):	Cliente para el protocolo telnet de login remoto
Summary(fr):	Client pour le protocole de connexion telnet
Summary(pl):	Klient protoko�u telnet
Summary(pt_BR):	Cliente para o protocolo telnet de login remoto
Summary(tr):	Telnet uzak ba�lant� protokol� i�in istemci ve sunucu
Name:		telnet
Version:	0.17
Release:	21
Group:		Networking
License:	BSD
Source0:	ftp://ftp.linux.org.uk/pub/linux/Networking/netkit/netkit-%{name}-%{version}.tar.gz
Source1:	%{name}d.inetd
Source2:	%{name}.desktop
Patch0:		netkit-%{name}-ipv6.patch
Patch1:		netkit-%{name}-fixes.patch
Patch2:		netkit-%{name}-ayt.patch
Patch3:		netkit-%{name}-issue.patch
Patch4:		netkit-%{name}-cpp.patch
Patch5:		netkit-%{name}-pld_man.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Telnet is a popular protocol for remote logins across the Internet.
This package provides a command line telnet client.

%description -l de
Telnet ist ein beliebtes Protokoll f�r entfernte Logins �ber das
Internet. Dieses Paket enth�lt einen Befehlszeilen-Telnet-Client.

%description -l es
Telnet es un protocolo popular para logins remotos a trav�s de la
Internet. Este paquete ofrece un cliente telnet en la l�nea de
comando.

%description -l fr
telnet est un protocole tr�s utilis� pour les logins distants sur
l'Internet. Ce paquetage offre un client telnet

%description -l pl
Telnet jest popularnym protoko�em umo�liwiaj�cym logowanie si� na
zdalnym komputerze w sieci internet i 6bone. Pakiet zawiera klienta
us�ugi telnet.

%description -l pt_BR
O telnet � um protocolo popular para logins remotos atrav�s da
Internet. Este pacote fornece um cliente telnet na linha de comando.

%description -l tr
Telnet, Internet �zerinden uzak kullan�c� ba�lant�lar� i�in pop�ler
bir protokoldur. Bu paket, bir komut sat�r� istemcisi ile birlikte bir
sunucu s�reci i�erir. Sunucu s�recin �al��t��� makinaya uzak
kullan�c�lar�n ba�lanabilir.

%package -n telnetd
Summary:	Server for the telnet remote login protocol
Summary(de):	Server f�r das entfernte Login-Protokoll 'telnet'
Summary(es):	Servidor para el protocolo telnet de login remoto
Summary(fr):	Serveur pour le protocole de connexion distante telnet
Summary(pl):	Serwer us�ugi telnet
Summary(pt_BR):	Servidor para o protocolo telnet de login remoto
Summary(tr):	Telnet uzak ba�lant� protokol� i�in istemci ve sunucu
Group:		Networking
Requires:	inetdaemon
Requires:	login
Prereq:		rc-inetd >= 0.8
Obsoletes:	telnet-server

%description -n telnetd
Telnet is a popular protocol for remote logins across the Internet.
This package provides telnet daemon which allows remote logins into
the machine it is running on.

%description -n telnetd -l de
Telnet ist ein beliebtes Protokoll f�r entfernte Logins �ber das
Internet. Dieses Paket enth�lt einen Telnet-D�mon, der entfernte
Logins auf dem Rechner, auf dem er l�uft, zul��t. Der Telnet- D�mon
ist standardm��ig aktiviert.

%description -n telnetd -l es
Telnet es un protocolo popular para logins remotos a trav�s de la
Internet. Este paquete ofrece un servidor telnet que permite login
remoto dentro de la m�quina en que se est� ejecutando. edit�ndose
/etc/inetd.conf.

%description -n telnetd -l fr
telnet est un protocole tr�s utilis� pour les logins distants sur
l'Internet. Ce paquetage offre d�mon telnet permettant des logins
distants sur la machine sur laquelle il tourne.

%description -n telnetd -l pl
Telnet jest popularnym protoko�em umo�liwiaj�cym logowanie si� na
zdalnym komputerze w sieci internet i 6bone. Pakiet zawiera serwer
us�ugi telnet.

%description -n telnetd -l pt_BR
O telnet � um protocolo popular para logins remotos atrav�s da
Internet. Este pacote fornece um servidor telnet que permite login
remoto dentro da m�quina em que ele est� rodando.

%description -n telnetd -l tr
Telnet, Internet �zerinden uzak kullan�c� ba�lant�lar� i�in pop�ler
bir protokoldur. Bu paket, bir komut sat�r� istemcisi ile birlikte bir
sunucu s�reci i�erir. Sunucu s�recin �al��t��� makinaya uzak
kullan�c�lar�n ba�lanabilir.

%prep
%setup -q -n netkit-%{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

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
%doc BUGS README
%attr(640,root,root) %config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/rc-inetd/telnetd

%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[58]/*

Summary:	Client and server for the telnet remote login protocol IPv6
Summary(de):	Client und Server für das entfernte Login-Protokoll 'telnet'
Summary(fr):	Client et serveur pour le protocole de connexion telnet.
Summary(pl):	Klient i serwer telnet ze wspomaganiem dla IPv6
Summary(tr):	Telnet uzak baðlantý protokolü için istemci ve sunucu
Name:		telnet
Version:	0.10
Release:	15
Group:		Networking
Group(pl):	Sieciowe
Copyright:	BSD
URL:		ftp://sunsite.unc.edu/pub/Linux/system/network/daemons
Source0:	netkit-telnet-%{version}.tar.gz
#Source1:	%{name}.wmconfig
Source2:	%{name}.rc-inetd
Patch0:		netkit-telnet-ipv6.patch
Patch1:		netkit-telnet-ptmx.patch
Patch2:		netkit-telnet-fixes.patch
Patch3:		netkit-telnet-c++.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
Telnet is a popular protocol for remote logins across the Internet. This
package provides a command line telnet client as well as a telnet daemon
which allows remote logins into the machine it is running on. The telnet
daemon is enabled by default, and may be disabled by editing /etc/inetd.conf.

%description -l de
Telnet ist ein beliebtes Protokoll für entfernte Logins über das Internet.
Dieses Paket enthält einen Befehlszeilen-Telnet-Client und einen Telnet-Dämon,
der entfernte Logins auf dem Rechner, auf dem er läuft, zuläßt. Der Telnet-
Dämon ist standardmäßig aktiviert. Sie können ihn deaktivieren, indem Sie die
Datei /etc/inetd.conf. ändern.

%description -l fr
telnet est un protocole très utilisé pour les logins distants sur l'Internet.
Ce paquetage offre un client telnet en ligne de commande et un démon telnet
permettant des logins distants sur la machine sur laquelle il tourne. Le
démon est activé par défaut et peut être désactivé en éditant /etc/inetd.conf.

%description -l tr
Telnet, Internet üzerinden uzak kullanýcý baðlantýlarý için popüler bir
protokoldur. Bu paket, bir komut satýrý istemcisi ile birlikte bir sunucu
süreci içerir. Sunucu sürecin çalýþtýðý makinaya uzak kullanýcýlarýn
baðlanabilir.

%description -l pl
Telnet jest popularnym protoko³em umo¿liwiaj±cym logowanie siê na zdalnym
komputerze w sieci internet i 6bone. Pakiet zawiera klienta i demona telnetd.

%package -n	telnetd
Summary:	Server for the telnet remote login protocol
Summary(de):	Server für das entfernte Login-Protokoll 'telnet'  
Summary(fr):	Serveur pour le protocole de connexion distante telnet
Summary(pl):	Serwer us³ugi telnet
Summary(tr):	Telnet uzak baðlantý protokolü için istemci ve sunucu
Group:		Networking
Group(pl):	Sieciowe
Requires:	inetdaemon

%description -n telnetd
Telnet is a popular protocol for remote logins across the Internet. This
package provides a command line telnet client as well as a telnet daemon
which allows remote logins into the machine it is running on. The telnet
daemon is enabled by default, and may be disabled by editing /etc/inetd.conf.

%description -l de -n telnetd
Telnet ist ein beliebtes Protokoll für entfernte Logins über das Internet.
Dieses Paket enthält einen Befehlszeilen-Telnet-Client und einen Telnet-Dämon,
der entfernte Logins auf dem Rechner, auf dem er läuft, zuläßt. Der Telnet-
Dämon ist standardmäßig aktiviert. Sie können ihn deaktivieren, indem Sie die
Datei /etc/inetd.conf. ändern.

%description -l fr -n telnetd
telnet est un protocole très utilisé pour les logins distants sur l'Internet.
Ce paquetage offre un client telnet en ligne de commande et un démon telnet
permettant des logins distants sur la machine sur laquelle il tourne. Le
démon est activé par défaut et peut être désactivé en éditant /etc/inetd.conf.

%description -l tr -n telnetd
Telnet, Internet üzerinden uzak kullanýcý baðlantýlarý için popüler bir
protokoldur. Bu paket, bir komut satýrý istemcisi ile birlikte bir sunucu
süreci içerir. Sunucu sürecin çalýþtýðý makinaya uzak kullanýcýlarýn
baðlanabilir.

%description -l pl -n telnetd
Telnet jest popularnym protoko³em umo¿liwiaj±cym logowanie siê na zdalnym
komputerze w sieci internet i 6bone. Pakiet zawiera klienta i demona telnetd.

%prep
%setup -q -n netkit-telnet-0.10
%patch0 -p1 
%patch1 -p1 
%patch2 -p1 
%patch3 -p1 

%build
# don't use configure macro
./configure --prefix=/usr

make OPT="$RPM_OPT_FLAGS -D__USE_UNIX98"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,5,8}

make INSTALLROOT=$RPM_BUILD_ROOT install

#install -d $RPM_BUILD_ROOT/etc/X11/wmconfig/
#install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/telnet

install -d $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/telnet

rm -f 	$RPM_BUILD_ROOT%{_mandir}/man8/*
install telnetd/*.8 $RPM_BUILD_ROOT%{_mandir}/man8

rm -f 	$RPM_BUILD_ROOT%{_sbindir}/*
install -s telnetd/telnetd $RPM_BUILD_ROOT%{_sbindir}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[158]/*
gzip -9nf BUGS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%config(missingok) /etc/X11/wmconfig/telnet

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files -n telnetd
%defattr(644,root,root,755)
%doc {BUGS,README}.gz
%attr(640,root,root) /etc/sysconfig/rc-inetd/telnet

%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[58]/*

Summary:	Client and server for the telnet remote login protocol IPv6
Summary(de):	Client und Server für das entfernte Login-Protokoll 'telnet'
Summary(fr):	Client et serveur pour le protocole de connexion telnet.
Summary(pl):	Klient i serwer telnet ze wspomaganiem dla IPv6
Summary(tr):	Telnet uzak baðlantý protokolü için istemci ve sunucu
Name:		telnet
Version:	0.14
Release:	1
Group:		Networking
Group(pl):	Sieciowe
Copyright:	BSD
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/daemons/netkit-telnet-%{version}.tar.gz
Source2:	telnetd.inetd
Patch0:		netkit-telnet-ipv6.patch
Patch1:		netkit-telnet-ptmx.patch
Patch2:		netkit-telnet-fixes.patch
Patch3:		netkit-telnet-c++.patch
Patch4:		netkit-telnet-openpty.patch
Patch5:		telnet-maint.patch
Patch6:		telnet-utmp.patch
Patch7:		telnetd-term.patch
BuildRequires:	ncurses-devel >= 5.0
Prereq:		rc-inetd >= 0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
# don't use configure macro
CFLAGS="RPM_OPT_FLAGS"; export CFLAGS
./configure \
	--prefix=%{_prefix}

make OPT="$RPM_OPT_FLAGS -D__USE_UNIX98"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,5,8}}

make INSTALLROOT=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/telnetd

rm -f 	$RPM_BUILD_ROOT%{_mandir}/man8/*
install telnetd/*.8 $RPM_BUILD_ROOT%{_mandir}/man8

rm -f 	$RPM_BUILD_ROOT%{_sbindir}/*
install -s telnetd/telnetd $RPM_BUILD_ROOT%{_sbindir}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[158]/* \
	BUGS README

%clean
rm -rf $RPM_BUILD_ROOT

%post -n telnetd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%postun -n telnetd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%files
%defattr(644,root,root,755)
#%config(missingok) /etc/X11/wmconfig/telnet

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files -n telnetd
%defattr(644,root,root,755)
%doc {BUGS,README}.gz
%attr(640,root,root) %config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/rc-inetd/telnetd

%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[58]/*

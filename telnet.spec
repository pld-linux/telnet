Summary:	Client and server for the telnet remote login protocol IPv6
Summary(de):	Client und Server f�r das entfernte Login-Protokoll 'telnet'
Summary(fr):	Client et serveur pour le protocole de connexion telnet.
Summary(pl):	Klient i serwer telnet ze wspomaganiem dla IPv6
Summary(tr):	Telnet uzak ba�lant� protokol� i�in istemci ve sunucu
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
Telnet ist ein beliebtes Protokoll f�r entfernte Logins �ber das Internet.
Dieses Paket enth�lt einen Befehlszeilen-Telnet-Client und einen Telnet-D�mon,
der entfernte Logins auf dem Rechner, auf dem er l�uft, zul��t. Der Telnet-
D�mon ist standardm��ig aktiviert. Sie k�nnen ihn deaktivieren, indem Sie die
Datei /etc/inetd.conf. �ndern.

%description -l fr
telnet est un protocole tr�s utilis� pour les logins distants sur l'Internet.
Ce paquetage offre un client telnet en ligne de commande et un d�mon telnet
permettant des logins distants sur la machine sur laquelle il tourne. Le
d�mon est activ� par d�faut et peut �tre d�sactiv� en �ditant /etc/inetd.conf.

%description -l tr
Telnet, Internet �zerinden uzak kullan�c� ba�lant�lar� i�in pop�ler bir
protokoldur. Bu paket, bir komut sat�r� istemcisi ile birlikte bir sunucu
s�reci i�erir. Sunucu s�recin �al��t��� makinaya uzak kullan�c�lar�n
ba�lanabilir.

%description -l pl
Telnet jest popularnym protoko�em umo�liwiaj�cym logowanie si� na zdalnym
komputerze w sieci internet i 6bone. Pakiet zawiera klienta i demona telnetd.

%package -n	telnetd
Summary:	Server for the telnet remote login protocol
Summary(de):	Server f�r das entfernte Login-Protokoll 'telnet'  
Summary(fr):	Serveur pour le protocole de connexion distante telnet
Summary(pl):	Serwer us�ugi telnet
Summary(tr):	Telnet uzak ba�lant� protokol� i�in istemci ve sunucu
Group:		Networking
Group(pl):	Sieciowe
Requires:	inetdaemon

%description -n telnetd
Telnet is a popular protocol for remote logins across the Internet. This
package provides a command line telnet client as well as a telnet daemon
which allows remote logins into the machine it is running on. The telnet
daemon is enabled by default, and may be disabled by editing /etc/inetd.conf.

%description -l de -n telnetd
Telnet ist ein beliebtes Protokoll f�r entfernte Logins �ber das Internet.
Dieses Paket enth�lt einen Befehlszeilen-Telnet-Client und einen Telnet-D�mon,
der entfernte Logins auf dem Rechner, auf dem er l�uft, zul��t. Der Telnet-
D�mon ist standardm��ig aktiviert. Sie k�nnen ihn deaktivieren, indem Sie die
Datei /etc/inetd.conf. �ndern.

%description -l fr -n telnetd
telnet est un protocole tr�s utilis� pour les logins distants sur l'Internet.
Ce paquetage offre un client telnet en ligne de commande et un d�mon telnet
permettant des logins distants sur la machine sur laquelle il tourne. Le
d�mon est activ� par d�faut et peut �tre d�sactiv� en �ditant /etc/inetd.conf.

%description -l tr -n telnetd
Telnet, Internet �zerinden uzak kullan�c� ba�lant�lar� i�in pop�ler bir
protokoldur. Bu paket, bir komut sat�r� istemcisi ile birlikte bir sunucu
s�reci i�erir. Sunucu s�recin �al��t��� makinaya uzak kullan�c�lar�n
ba�lanabilir.

%description -l pl -n telnetd
Telnet jest popularnym protoko�em umo�liwiaj�cym logowanie si� na zdalnym
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

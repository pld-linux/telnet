Summary:     Client and server for the telnet remote login protocol
Summary(de): Client und Server für das entfernte Login-Protokoll 'telnet'
Summary(fr): Client et serveur pour le protocole de connexion distante telnet.
Summary(pl): Telnet - klient
Summary(tr): Telnet uzak baðlantý protokolü için istemci ve sunucu
Name:        telnet
Version:     0.10
Release:     7
Copyright:   BSD
Group:       Networking
Source0:     ftp://sunsite.unc.edu/pub/Linux/system/network/daemons/netkit-%{name}-%{version}.tar.gz
Source1:     telnet.wmconfig
Patch:       netkit-telnet-misc.patch
Requires:    inetd
Buildroot:   /tmp/%{name}-%{version}-root

%description
Telnet is a popular protocol for remote logins across the Internet. This
package provides a command line telnet.

%description -l pl
Telnet jest popularnym protoko³em umo¿liwiaj±cym logowanie siê na zdalnym
komputerze w sieci internet i 6bone. Pakiet zawiera aplakcjê klienck±.

%package -n telnetd
Summary:     Server for the telnet remote login protocol
Summary(de): Server für das entfernte Login-Protokoll 'telnet'  
Summary(fr): Serveur pour le protocole de connexion distante telnet
Summary(pl): Serwer us³ugi telnet
Summary(tr): Telnet uzak baðlantý protokolü için istemci ve sunucu
Group:       Networking

%description -n telnetd
Telnet is a popular protocol for remote logins across the Internet. This
package provides a telnet daemon which allows remote logins into the machine
it is running on.

%description -n telnetd -l pl
Telnet jest popularnym protoko³em umo¿liwiaj±cym logowanie siê na zdalnym
komputerze w sieci internet i 6bone. Pakiet zawiera klienta i demona telnetd.

%prep
%setup -q -n netkit-%{name}-%{version}
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/{bin,sbin,man/man{1,5,8}}}

make INSTALLROOT=$RPM_BUILD_ROOT install
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/telnet

rm -rf $RPM_BUILD_ROOT/usr/man/man8/telnetd.8
echo ".so in.telnetd.8" > $RPM_BUILD_ROOT/usr/man/man8/telnetd.8
gzip -9nf $RPM_BUILD_ROOT/usr/man/man{1,5,8}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(644, root, root) %config(missingok) /etc/X11/wmconfig/telnet
%attr(755, root, root) /usr/bin/telnet
%attr(644, root,  man) /usr/man/man1/*

%files -n telnetd
%attr(755, root, root) /usr/sbin/in.telnetd
%attr(644, root,  man) /usr/man/man5/*
%attr(644, root,  man) /usr/man/man8/*

%changelog
* Mon Dec  9 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.10-7]
- added gzipping man pages,
- telnetd(8) man page is now maked as nroff include to
  in.telnetd(8) instead making sym link to in.telnetd.8 
  (this allow compress man pages),
- removed CC=egcs make parameter.

* Wed Nov 13 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.10-6]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- fixed passing $RPM_OPT_FLAGS,
- telnet damon in separated package,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Sun Jul 05 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- added pl translation.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 24 1998 Cristian Gafton <gafton@redhat.com>
- compile C++ code using egcs

* Tue Apr 14 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build

Summary:	POP3 mail client
Summary(pl):	Klient POP3
Name:		fetchpop
Version:	1.9
Release:	4
Copyright:	GPL
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Source0		ftp://tsx-11.mit.edu/pub/linux/sources/usr.bin/%{name}%{version}.tar.gz
Source1:	fetchpop.wmconfig
Patch0:		fetchpop-make.patch
Patch1:		fetchpop-fetch.patch
Patch2:		fetchpop-pop.patch
Requires:	smtpdaemon
BuildRoot:	/tmp/%{name}-%{version}-root

%description
By default, fetchpop retrieves new mail from the remote pop mail
server and appends it to your mailbox file, using information in the
file ~/.fetchhost.  Fetchpop has many options to change its default
behavior.     

%description -l pl
Domy¶lnie fetchpop ¶ci±ga pocztê ze zdalnego serwera poczty i wrzuca j±
do twojej skrzynki u¿ywaj±c informacji z pliku ~/.fetchhost. Fetchpop
posiada wiele opcji mog±cych zmieniæ jego domy¶lne zachowanie.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1 
%patch1 -p1
%patch2 -p1

%build
make all CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make install INSTALL_DIR=$RPM_BUILD_ROOT
make install.truncate INSTALL_DIR=$RPM_BUILD_ROOT 

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/fetchpop

strip $RPM_BUILD_ROOT%{_bindir}/{fetchpop,truncate}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README RFC1225 TODO FAQ.fetchpop

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr (644,root,root,755)
%doc {README,RFC1225,TODO,FAQ.fetchpop}.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%changelog
* Thu Apr 15 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [1.9-4]
- removed man group from man pages
- cosmetic changes
  
* Mon Feb  8 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [1.9-3]
- added gzipping documentation
- added LDFLAGS=-s
- cosmetic changes

* Thu Jan 28 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [1.9-2]
- added wmconfig,
- added pl translations,
- changed BuildRoot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added using "install -d" in %install,
- added gzipping man pages,
- changed patches names,
- deleted one patch,
- added full %attr description in %files.

* Mon Aug 17 1998 Michael Maher <mike@redhat.com>
- Built package from contrib package

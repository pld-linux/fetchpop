Summary:	POP3 mail client
Summary(pl):	Klient POP3
Name:		fetchpop
Version:	1.9
Release:	2d
Source:		ftp://tsx-11.mit.edu/pub/linux/sources/usr.bin/%{name}%{version}.tar.gz
Copyright:	GPL
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
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
CFLAGS="$RPM_OPT_FLAGS"
make all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/bin/,usr/man/man1}

make install INSTALL_DIR=$RPM_BUILD_ROOT
make install.truncate INSTALL_DIR=$RPM_BUILD_ROOT 

strip $RPM_BUILD_ROOT/usr/bin/{fetchpop,truncate}

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/*

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr (644,root,root,755)
%doc README RFC1225 TODO FAQ.fetchpop
%attr(755,root,root) /usr/bin/*
%attr(644,root, man) /usr/man/man1/*

%changelog
* Wed Jan 20 1999 Micha³ Kuratczyk <kurkens@polbox.com> [1.9-2]
  [1.9-12]
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

Summary:	POP3 mail client
Summary(pl):	Klient POP3
Name:		fetchpop
Version:	1.9
Release:	4
License:	GPL
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Source0 	ftp://tsx-11.mit.edu/pub/linux/sources/usr.bin/%{name}%{version}.tar.gz
Source1:	%{name}.wmconfig
Patch0:		%{name}-make.patch
Patch1:		%{name}-fetch.patch
Patch2:		%{name}-pop.patch
Requires:	smtpdaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
By default, fetchpop retrieves new mail from the remote pop mail
server and appends it to your mailbox file, using information in the
file ~/.fetchhost. Fetchpop has many options to change its default
behavior.

%description -l pl
Domy¶lnie fetchpop ¶ci±ga pocztê ze zdalnego serwera poczty i wrzuca
j± do twojej skrzynki u¿ywaj±c informacji z pliku ~/.fetchhost.
Fetchpop posiada wiele opcji mog±cych zmieniæ jego domy¶lne
zachowanie.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1 
%patch1 -p1
%patch2 -p1

%build
%{__make} all CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}/X11/wmconfig}

%{__make} install install.truncate \
	INSTALL_DIR=$RPM_BUILD_ROOT \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/fetchpop

gzip -9nf README RFC1225 TODO FAQ.fetchpop

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,RFC1225,TODO,FAQ.fetchpop}.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

Summary:	POP3 mail client
Summary(pl):	Klient POP3
Name:		fetchpop
Version:	1.9
Release:	8
License:	GPL
Group:		Applications/Mail
Source0:	ftp://tsx-11.mit.edu/pub/linux/sources/usr.bin/%{name}%{version}.tar.gz
# Source0-md5:	0c9b186791ea1e3da1b28f4f6094ca01
Source1:	%{name}.desktop
Patch1:		ftp://tsx-11.mit.edu/pub/linux/sources/usr.bin/%{name}%{version}.patch1
Patch2:		ftp://tsx-11.mit.edu/pub/linux/sources/usr.bin/%{name}%{version}.patch2
Requires:	smtpdaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
By default, fetchpop retrieves new mail from the remote pop mail
server and appends it to your mailbox file, using information in the
file ~/.fetchhost. Fetchpop has many options to change its default
behavior.

%description -l pl
Domy�lnie fetchpop �ci�ga poczt� ze zdalnego serwera poczty i wrzuca
j� do twojej skrzynki u�ywaj�c informacji z pliku ~/.fetchhost.
Fetchpop posiada wiele opcji mog�cych zmieni� jego domy�lne
zachowanie.

%prep
%setup -q -n %{name}%{version}
%patch1 -p1
%patch2 -p1

%build
%{__make} all CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_desktopdir}}

%{__make} install install.truncate \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README RFC1225 TODO FAQ.fetchpop

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_desktopdir}/*.desktop

Summary:	Font configuration and customization library
Summary(pl):	Biblioteka do konfigurowania font�w
Summary(pt_BR):	Fontconfig � uma biblioteca para configura��o e customiza��o do acesso a fontes
Name:		fontconfig
Version:	2.2.92
Release:	2
Epoch:		1
License:	MIT
Group:		Libraries
# Source0:	http://fontconfig.org/release/%{name}-%{version}.tar.gz
Source0:	http://pdx.freedesktop.org/~fontconfig/release/%{name}-%{version}.tar.gz
# Source0-md5:	45c4f2bac99b74fea693eda28fe30c45
Patch0:		%{name}-blacklist.patch
Patch1:		%{name}-date.patch
Patch2:		%{name}-defaultconfig.patch
Patch3:		%{name}-freetype-includes.patch
URL:		http://fontconfig.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-utils >= 0.6.13-3
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	ed
BuildRequires:	expat-devel
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	libtool
Requires(post):	/sbin/ldconfig
Provides:	%{name}-realpkg = %{epoch}:%{version}-%{release}
Provides:	XFree86-fontconfig
Obsoletes:	XFree86-fontconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fontconfig is designed to locate fonts within the system and select
them according to requirements specified by applications.

%description -l pl
Fontconfig jest biblioteka przeznaczon� do lokalizowania font�w w
systemie i wybierania ich w zale�no�ci od potrzeb aplikacji.

%description -l pt_BR
Fontconfig � uma biblioteca para configura��o e customiza��o do acesso
a fontes.

%package devel
Summary:	Font configuration and customization library
Summary(pl):	Biblioteka do konfigurowania font�w
Summary(pt_BR):	Fontconfig � uma biblioteca para configura��o e customiza��o do acesso a fontes
Group:		Development/Libraries
Requires:	%{name}-realpkg = %{epoch}:%{version}
Requires:	expat-devel
Requires:	freetype-devel
Provides:	%{name}-devel-realpkg = %{epoch}:%{version}-%{release}
Provides:	XFree86-fontconfig-devel
Obsoletes:	XFree86-fontconfig-devel

%description devel
Fontconfig is designed to locate fonts within the system and select
them according to requirements specified by applications.

This package contains the header files needed to develop programs that
use these fontconfig.

%description devel -l pl
Fontconfig jest biblioteka przeznaczon� do lokalizowania font�w w
systemie i wybierania ich w zale�no�ci od potrzeb aplikacji.

Ten pakiet zawiera pliki nag��wkowe potrzebne do kompilowania
program�w korzystaj�cych z biblioteki fontconfig.

%description devel -l pt_BR
Fontconfig � uma biblioteca para configura��o e customiza��o do acesso
a fontes.

%package static
Summary:	Static font configuration and customization library
Summary(pl):	Statyczna biblioteka do konfigurowania font�w
Group:		Development/Libraries
Requires:	%{name}-devel-realpkg = %{epoch}:%{version}
Provides:	XFree86-fontconfig-static
Obsoletes:	XFree86-fontconfig-static

%description static
This package contains static version of fontconfig library.

%description static -l pl
Ten pakiet zawiera statyczn� wersj� biblioteki fontconfig.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-docs
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,3,5}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
install doc/*.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
HOME=/root %{_bindir}/fc-cache -f 2> /dev/null

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%dir %{_sysconfdir}/fonts
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/fonts/fonts.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/fonts/local.conf
%{_sysconfdir}/fonts/fonts.dtd
%attr(755,root,root) %{_bindir}/fc-*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*

%files devel
%defattr(644,root,root,755)
%doc doc/fontconfig-devel/*.html
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/fontconfig
%{_pkgconfigdir}/fontconfig.pc
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
